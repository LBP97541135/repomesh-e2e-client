"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def checkout_lines(quote: dict[str, int]) -> dict:
    lines = [
        f"Subtotal: {quote['subtotal']}",
        f"Shipping: {quote['shipping']}",
    ]
    discount = quote.get("discount_amount", 0)
    if discount:
        lines.append(f"Discount: {discount}")
    lines.append(f"Total: {quote['total']}")

    free_shipping_200 = quote.get("subtotal", 0) >= 200
    if free_shipping_200:
        lines.append("已免运费")

    return {
        "lines": lines,
        "free_shipping_200": free_shipping_200,
    }
