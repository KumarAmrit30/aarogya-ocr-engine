"""Dataset-level lineage DAG."""

from __future__ import annotations

from aarogya_core.types.data_platform import DatasetLineageGraph, LineageEdge
from aarogya_core.types.ids import DatasetId


def empty_graph(dataset_id: DatasetId) -> DatasetLineageGraph:
    return DatasetLineageGraph(dataset_id=dataset_id, nodes=[], edges=[])


def add_edge(
    graph: DatasetLineageGraph,
    from_node: str,
    to_node: str,
    relation: str = "derived",
) -> DatasetLineageGraph:
    nodes = list(dict.fromkeys([*graph.nodes, from_node, to_node]))
    edges = list(graph.edges) + [
        LineageEdge(from_node=from_node, to_node=to_node, relation=relation)  # type: ignore[arg-type]
    ]
    return graph.model_copy(update={"nodes": nodes, "edges": edges})
