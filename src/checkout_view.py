"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def checkout_lines(quote: dict[str, int]) -> list[str]:
    lines = [
        f"Subtotal: {quote['subtotal']}",
        f"Shipping: {quote['shipping']}",
    ]
    discount = quote.get("discount_amount", 0)
    if discount:
        lines.append(f"Discount: {discount}")
    
    # Show discount hint when subtotal reaches 300
    if quote.get("subtotal", 0) >= 300:
        lines.append("Discount Hint: 已减 30")
    
    lines.append(f"Total: {quote['total']}")
    return lines
