#!/usr/bin/env python3
"""Validate standalone pick-relevant-ideas pack (stdlib only)."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "references" / "graph.yaml"
FACETS = ROOT / "references" / "facet-seeds.yaml"
PRINCIPLES = ROOT / "principles"

EDGE_TYPES = {"co-applies", "complements", "requires", "tension"}
WEIGHTS = {"strong", "med", "weak"}

EDGE_RE = re.compile(
    r"^\s*-\s*\[([^,\]]+),\s*([^,\]]+),\s*([^,\]]+),\s*([^,\]]+)\]\s*$"
)
FACET_KEY_RE = re.compile(r"^  ([a-z0-9-]+):\s*$")
SEED_RE = re.compile(r"^\s+-\s+([a-z0-9-]+)\s*$")
CLUSTER_KEY_RE = re.compile(r"^  ([a-z0-9-]+):\s*$")


def parse_edges(text: str) -> list[tuple[str, str, str, str]]:
    edges: list[tuple[str, str, str, str]] = []
    in_edges = False
    for line in text.splitlines():
        if line.startswith("edges:"):
            in_edges = True
            continue
        if in_edges:
            if line and not line[0].isspace() and not line.startswith("#"):
                if not line.startswith("edges:"):
                    in_edges = False
            m = EDGE_RE.match(line)
            if m:
                a, b, typ, w = (x.strip().strip("\"'") for x in m.groups())
                edges.append((a, b, typ, w))
    return edges


def parse_facets(text: str) -> dict[str, list[str]]:
    facets: dict[str, list[str]] = {}
    in_facets = False
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("facets:"):
            in_facets = True
            continue
        if not in_facets:
            continue
        if (
            line
            and not line[0].isspace()
            and not line.startswith("#")
            and not line.startswith("facets:")
        ):
            break
        mk = FACET_KEY_RE.match(line)
        if mk:
            current = mk.group(1)
            facets.setdefault(current, [])
            continue
        ms = SEED_RE.match(line)
        if ms and current:
            facets[current].append(ms.group(1))
    return facets


def parse_cluster_members(text: str) -> dict[str, list[str]]:
    clusters: dict[str, list[str]] = {}
    in_clusters = False
    current: str | None = None
    in_members = False
    for line in text.splitlines():
        if line.startswith("clusters:"):
            in_clusters = True
            continue
        if not in_clusters:
            continue
        if line.startswith("must_keep") or (
            line
            and not line[0].isspace()
            and not line.startswith("#")
            and not line.startswith("clusters:")
        ):
            break
        mk = CLUSTER_KEY_RE.match(line)
        if mk and "members" not in line:
            current = mk.group(1)
            clusters.setdefault(current, [])
            in_members = False
            continue
        if current and line.strip() == "members:":
            in_members = True
            continue
        if in_members and current:
            ms = SEED_RE.match(line)
            if ms:
                clusters[current].append(ms.group(1))
            elif line.strip() and not line.strip().startswith("-") and not line.strip().startswith("#"):
                if CLUSTER_KEY_RE.match(line):
                    in_members = False
    return clusters


def body_index() -> dict[str, Path]:
    out: dict[str, Path] = {}
    if not PRINCIPLES.is_dir():
        return out
    for p in PRINCIPLES.rglob("*.md"):
        if p.name in ("INDEX.md", "README.md", "THROUGH-LINE.md", "PREAMBLE.md"):
            continue
        out[p.stem] = p
    return out


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    required = [
        ROOT / "SKILL.md",
        ROOT / "README.md",
        GRAPH,
        FACETS,
        ROOT / "references" / "details.md",
        ROOT / "references" / "through-line.md",
        PRINCIPLES / "INDEX.md",
    ]
    for p in required:
        if not p.is_file():
            errors.append(f"missing required file: {p.relative_to(ROOT)}")

    gtext = GRAPH.read_text(encoding="utf-8") if GRAPH.is_file() else ""
    ftext = FACETS.read_text(encoding="utf-8") if FACETS.is_file() else ""

    edges = parse_edges(gtext)
    if GRAPH.is_file() and not edges:
        errors.append("graph.yaml: no edges parsed")

    nodes: set[str] = set()
    for i, (a, b, typ, w) in enumerate(edges):
        nodes.add(a)
        nodes.add(b)
        if typ not in EDGE_TYPES:
            errors.append(f"edge[{i}] {a}-{b}: bad type {typ!r}")
        if w not in WEIGHTS:
            errors.append(f"edge[{i}] {a}-{b}: bad weight {w!r}")
        if w == "weak":
            warnings.append(f"edge[{i}]: authored weak {a}-{b}")

    clusters = parse_cluster_members(gtext)
    for name, members in clusters.items():
        for m in members:
            if m not in nodes:
                warnings.append(
                    f"cluster {name}: member {m!r} never appears as edge endpoint"
                )

    facets = parse_facets(ftext)
    if FACETS.is_file() and not facets:
        errors.append("facet-seeds.yaml: no facets parsed")

    seed_nodes: set[str] = set()
    for facet, seeds in facets.items():
        if not seeds:
            errors.append(f"facet {facet}: empty seeds")
            continue
        if len(seeds) > 4:
            warnings.append(f"facet {facet}: {len(seeds)} seeds (prefer ≤4)")
        for s in seeds:
            seed_nodes.add(s)
            if s not in nodes:
                warnings.append(f"facet {facet}: seed {s!r} has no graph edges")

    bodies = body_index()
    needed = nodes | seed_nodes
    for i in sorted(needed):
        if i not in bodies:
            errors.append(f"missing principle body for id {i!r} under principles/")

    # standalone: ban external / foreign toolkit leakage in public surfaces
    ban = (
        "malaysian-engineering",
        "Malaysian Engineering",
        "me-principles",
        "skills/_shared/principles",
        "~/.agents/skills/_shared",
    )
    for rel in (
        "SKILL.md",
        "README.md",
        "principles/README.md",
        "references/details.md",
        "references/graph.yaml",
    ):
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for bad in ban:
            if bad in text:
                errors.append(f"{rel} contains banned token: {bad}")

    deg: Counter[str] = Counter()
    for a, b, _, _ in edges:
        deg[a] += 1
        deg[b] += 1
    top = deg.most_common(8)

    print(f"edges: {len(edges)}")
    print(f"nodes (edge endpoints): {len(nodes)}")
    print(f"clusters: {len(clusters)}")
    print(f"facets: {len(facets)}")
    print(f"unique seeds: {len(seed_nodes)}")
    print(f"principle bodies: {len(bodies)}")
    print(f"ids needing bodies: {len(needed)}")
    print("top degree:", ", ".join(f"{n}={c}" for n, c in top))

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERR: {e}")

    if errors:
        return 1
    print("OK (standalone)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
