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

    def test_free_shipping_1200_displayed(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 1500, "shipping": 0, "free_shipping_1200": True, "total": 1500}
            ),
            ["Subtotal: 1500", "Shipping: 0", "满1200免运费", "Total: 1500"],
        )


if __name__ == "__main__":
    unittest.main()
