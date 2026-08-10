"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def checkout_lines(quote: dict[str, int]) -> list[str]:
    lines = [
        f"Subtotal: {quote['subtotal']}",
        f"Shipping: {quote['shipping']}",
    ]
    discount = quote.get("discount_amount", 0)
    if discount:
        lines.append(f"Discount: {discount}")
    lines.append(f"Total: {quote['total']}")
    return lines
