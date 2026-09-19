"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def checkout_lines(quote: dict[str, int]) -> list[str]:
    lines = [
        f"Subtotal: {quote['subtotal']}",
        f"Shipping: {quote['shipping']}",
    ]
    tax = quote.get("tax", 0)
    if tax:
        lines.append(f"Tax: {tax}")
    discount = quote.get("discount_amount", 0)
    if discount:
        lines.append(f"Discount: {discount}")
    lines.append(f"Total: {quote['total']}")
    return lines
