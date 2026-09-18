"""Quote calculation logic for e-commerce pricing."""

# 满额免运费门槛
FREE_SHIPPING_THRESHOLD = 200

# 默认运费
DEFAULT_SHIPPING_COST = 10


def calculate_quote(items: list[dict], discount_amount: int = 0) -> dict[str, int]:
    """
    计算报价
    
    当小计达到200时，运费免收
    
    Args:
        items: 商品列表，每项包含 price 和 quantity
        discount_amount: 折扣金额
    
    Returns:
        包含 subtotal, shipping, discount_amount, total 的字典
    """
    # 计算小计
    subtotal = sum(item.get('price', 0) * item.get('quantity', 1) for item in items)
    
    # 满200免运费
    if subtotal >= FREE_SHIPPING_THRESHOLD:
        shipping = 0
    else:
        shipping = DEFAULT_SHIPPING_COST
    
    # 计算总价
    total = subtotal + shipping - discount_amount
    
    return {
        'subtotal': subtotal,
        'shipping': shipping,
        'discount_amount': discount_amount,
        'total': total,
    }
