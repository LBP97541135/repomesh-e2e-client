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

    def test_free_shipping_quote(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 500, "shipping": 0, "free_shipping": True, "total": 500}
            ),
            ["Subtotal: 500", "Shipping: FREE", "Total: 500"],
        )

    def test_free_shipping_with_discount(self):
        self.assertEqual(
            checkout_lines(
                {
                    "subtotal": 600,
                    "shipping": 0,
                    "free_shipping": True,
                    "discount_amount": 100,
                    "total": 500,
                }
            ),
            ["Subtotal: 600", "Shipping: FREE", "Discount: 100", "Total: 500"],
        )


if __name__ == "__main__":
    unittest.main()
