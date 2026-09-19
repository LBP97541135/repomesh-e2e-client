"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def calculate_quote(items: list[dict]) -> dict[str, int]:
    """Calculate quote with order-level discount.
    
    When subtotal >= 300, applies a 30 unit discount.
    """
    subtotal = sum(item.get("price", 0) * item.get("quantity", 1) for item in items)
    shipping = 10  # default shipping cost
    
    discount = 0
    if subtotal >= 300:
        discount = 30
    
    total = subtotal + shipping - discount
    
    return {"subtotal": subtotal, "shipping": shipping, "discount": discount, "total": total}


def checkout_lines(quote: dict[str, int]) -> list[str]:
    lines = [
        f"Subtotal: {quote['subtotal']}",
        f"Shipping: {quote['shipping']}",
    ]
    discount = quote.get("discount", 0)
    if discount:
        lines.append(f"Discount: {discount}")
    lines.append(f"Total: {quote['total']}")
    return lines
