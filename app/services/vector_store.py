import faiss
import numpy as np
from pathlib import Path

index = None

def create_index(embedding_dimension: int):

    global index

    index = faiss.IndexFlatIP(
        embedding_dimension
    )

def add_embedding(embeddings):

    vectors = np.array(
        embeddings,
        dtype=np.float32
    )

    faiss.normalize_L2(
        vectors
    )

    index.add(
        vectors
    )

def search(
        query_embedding,
        k: int = 10
):

    query = np.array(
        [query_embedding],
        dtype=np.float32
    )

    faiss.normalize_L2(
        query
    )

    scores, indices = index.search(
        query,
        k
    )

    return scores, indices

def save_index(file_name: str = "vector.index"):

    faiss.write_index(
        index,
        file_name
    )

def load_index(file_name: str = "vector.index"):

    global index

    if Path(file_name).exists():

        index = faiss.read_index(
            file_name
        )

        return True

    return False