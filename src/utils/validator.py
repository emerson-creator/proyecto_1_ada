def validar_orden(
    orden: list[int],
    n: int,
) -> bool:

    if len(orden) != n:
        return False

    return sorted(orden) == list(range(n))