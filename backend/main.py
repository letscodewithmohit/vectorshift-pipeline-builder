from fastapi import FastAPI
from pydantic import BaseModel
from collections import defaultdict
from fastapi.middleware.cors import CORSMiddleware


def is_dag(nodes, edges):
    graph = defaultdict(list)

    for edge in edges:
        source = edge["source"]
        target = edge["target"]

        graph[source].append(target)

    visited = set()
    visiting = set()

    def dfs(node):
        if node in visiting:
            return False

        if node in visited:
            return True

        visiting.add(node)

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False

        visiting.remove(node)
        visited.add(node)

        return True

    for node in nodes:
        node_id = node["id"]

        if node_id not in visited:
            if not dfs(node_id):
                return False

    return True

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Ping": "Pong"}


class PipelineData(BaseModel):
    nodes: list
    edges: list



@app.post("/pipelines/parse")
def parse_pipeline(pipeline: PipelineData):
    dag = is_dag(
        pipeline.nodes,
        pipeline.edges
    )

    return {
        "num_nodes": len(pipeline.nodes),
        "num_edges": len(pipeline.edges),
        "is_dag": dag
    }