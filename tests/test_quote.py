import unittest

from src.api.quote import calculate_quote


class QuoteCalculationTest(unittest.TestCase):
    def test_regular_quote(self):
        """小计未满200，收取运费"""
        items = [{'price': 80, 'quantity': 1}]
        result = calculate_quote(items)
        self.assertEqual(result, {
            'subtotal': 80,
            'shipping': 10,
            'discount_amount': 0,
            'total': 90,
        })

    def test_free_shipping_at_threshold(self):
        """小计达到200时，免运费"""
        items = [{'price': 200, 'quantity': 1}]
        result = calculate_quote(items)
        self.assertEqual(result, {
            'subtotal': 200,
            'shipping': 0,
            'discount_amount': 0,
            'total': 200,
        })

    def test_free_shipping_above_threshold(self):
        """小计超过200时，免运费"""
        items = [{'price': 350, 'quantity': 1}]
        result = calculate_quote(items)
        self.assertEqual(result, {
            'subtotal': 350,
            'shipping': 0,
            'discount_amount': 0,
            'total': 350,
        })

    def test_quote_with_discount(self):
        """有折扣时，小计达到200仍免运费"""
        items = [{'price': 100, 'quantity': 1}]
        result = calculate_quote(items, discount_amount=50)
        self.assertEqual(result, {
            'subtotal': 100,
            'shipping': 10,
            'discount_amount': 50,
            'total': 60,
        })

    def test_multiple_items_free_shipping(self):
        """多商品合计达到200，免运费"""
        items = [
            {'price': 100, 'quantity': 1},
            {'price': 50, 'quantity': 2},
        ]
        result = calculate_quote(items)
        self.assertEqual(result, {
            'subtotal': 200,
            'shipping': 0,
            'discount_amount': 0,
            'total': 200,
        })


if __name__ == "__main__":
    unittest.main()
