"""Checkout view adapter used by the RepoMesh delivery acceptance test."""


def checkout_lines(quote: dict[str, int]) -> list[str]:
    lines = [
        f"Subtotal: {quote['subtotal']}",
    ]
    
    # 满200免运费，展示"已免运费"提示
    if quote.get('shipping', 0) == 0 and quote.get('subtotal', 0) >= 200:
        lines.append("Shipping: 已免运费")
    else:
        lines.append(f"Shipping: {quote['shipping']}")
    
    discount = quote.get("discount_amount", 0)
    if discount:
        lines.append(f"Discount: {discount}")
    lines.append(f"Total: {quote['total']}")
    return lines
