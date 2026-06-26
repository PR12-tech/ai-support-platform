from rank_bm25 import BM25Okapi

bm25_index = None

DOCUMENTS = []


def create_bm25_index(documents: list):

    global bm25_index
    global DOCUMENTS

    DOCUMENTS = documents

    tokenized_documents = [
        document.lower().split()
        for document in documents
    ]

    bm25_index = BM25Okapi(
        tokenized_documents
    )

def search_bm25(
        query: str,
        k: int = 10
):

    tokenized_query = (
        query.lower().split()
    )

    scores = bm25_index.get_scores(
        tokenized_query
    )

    ranked_results = sorted(
        zip(
            DOCUMENTS,
            scores
        ),
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_results[:k]