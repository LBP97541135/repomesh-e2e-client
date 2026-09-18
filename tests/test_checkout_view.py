import unittest

from src.checkout_view import checkout_lines


class CheckoutViewTest(unittest.TestCase):
    def test_regular_quote(self):
        self.assertEqual(
            checkout_lines({"subtotal": 80, "shipping": 5, "total": 85}),
            ["Subtotal: 80", "Shipping: 5", "Total: 85"],
        )

    def test_quote_with_discount(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 80, "shipping": 5, "discount_amount": 10, "total": 75}
            ),
            ["Subtotal: 80", "Shipping: 5", "Discount: 10", "Total: 75"],
        )

    def test_zero_discount_omitted(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 80, "shipping": 5, "discount_amount": 0, "total": 85}
            ),
            ["Subtotal: 80", "Shipping: 5", "Total: 85"],
        )

    def test_free_shipping_at_threshold(self):
        """小计达到200时，运费免收并显示已免运费"""
        self.assertEqual(
            checkout_lines({"subtotal": 200, "shipping": 0, "total": 200}),
            ["Subtotal: 200", "Shipping: 已免运费", "Total: 200"],
        )

    def test_free_shipping_above_threshold(self):
        """小计超过200时，运费免收并显示已免运费"""
        self.assertEqual(
            checkout_lines({"subtotal": 350, "shipping": 0, "total": 350}),
            ["Subtotal: 350", "Shipping: 已免运费", "Total: 350"],
        )


if __name__ == "__main__":
    unittest.main()
