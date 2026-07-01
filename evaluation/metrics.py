def calculate_hit_rate(
    hits: int,
    total: int
):
    return hits / total


def calculate_average_precision(
    total_precision: float,
    total: int
):
    return total_precision / total


def calculate_mrr(
    total_reciprocal_rank: float,
    total: int
):
    return total_reciprocal_rank / total