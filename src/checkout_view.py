"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def checkout_lines(quote: dict[str, int]) -> list[str]:
    return [
        f"Subtotal: {quote['subtotal']}",
        f"Shipping: {quote['shipping']}",
        f"Total: {quote['total']}",
    ]
