import unittest

from src.checkout_view import checkout_lines


class CheckoutViewTest(unittest.TestCase):
    def test_regular_quote(self):
        result = checkout_lines({"subtotal": 80, "shipping": 5, "total": 85})
        self.assertEqual(
            result["lines"],
            ["Subtotal: 80", "Shipping: 5", "Total: 85"],
        )
        self.assertFalse(result["free_shipping_200"])

    def test_quote_with_discount(self):
        result = checkout_lines(
            {"subtotal": 80, "shipping": 5, "discount_amount": 10, "total": 75}
        )
        self.assertEqual(
            result["lines"],
            ["Subtotal: 80", "Shipping: 5", "Discount: 10", "Total: 75"],
        )
        self.assertFalse(result["free_shipping_200"])

    def test_zero_discount_omitted(self):
        result = checkout_lines(
            {"subtotal": 80, "shipping": 5, "discount_amount": 0, "total": 85}
        )
        self.assertEqual(
            result["lines"],
            ["Subtotal: 80", "Shipping: 5", "Total: 85"],
        )
        self.assertFalse(result["free_shipping_200"])

    def test_free_shipping_at_200(self):
        result = checkout_lines({"subtotal": 200, "shipping": 0, "total": 200})
        self.assertEqual(
            result["lines"],
            ["Subtotal: 200", "Shipping: 0", "Total: 200", "已免运费"],
        )
        self.assertTrue(result["free_shipping_200"])

    def test_free_shipping_above_200(self):
        result = checkout_lines({"subtotal": 250, "shipping": 0, "total": 250})
        self.assertEqual(
            result["lines"],
            ["Subtotal: 250", "Shipping: 0", "Total: 250", "已免运费"],
        )
        self.assertTrue(result["free_shipping_200"])


if __name__ == "__main__":
    unittest.main()
