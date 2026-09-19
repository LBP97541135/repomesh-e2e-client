"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def checkout_lines(quote: dict[str, int]) -> list[str]:
    lines = [
        f"Subtotal: {quote['subtotal']}",
    ]
    free_shipping = quote.get("free_shipping", False)
    if free_shipping:
        lines.append("Shipping: FREE")
    else:
        lines.append(f"Shipping: {quote['shipping']}")

    discount = quote.get("discount_amount", 0)
    if discount:
        lines.append(f"Discount: {discount}")
    lines.append(f"Total: {quote['total']}")
    return lines
