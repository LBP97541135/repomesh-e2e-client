"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def checkout_lines(quote: dict[str, int]) -> list[str]:
    lines = [
        f"Subtotal: {quote['subtotal']}",
        f"Shipping: {quote['shipping']}",
    ]
    
    # Display free shipping indicator when free_shipping_1200 is true
    if quote.get("free_shipping_1200"):
        lines.append("满1200免运费")
    
    discount = quote.get("discount_amount", 0)
    if discount:
        lines.append(f"Discount: {discount}")
    lines.append(f"Total: {quote['total']}")
    return lines
