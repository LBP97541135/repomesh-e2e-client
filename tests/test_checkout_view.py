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

    def test_quote_with_tax(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 80, "shipping": 5, "tax": 8, "total": 93}
            ),
            ["Subtotal: 80", "Shipping: 5", "Tax: 8", "Total: 93"],
        )

    def test_quote_with_tax_and_discount(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 80, "shipping": 5, "tax": 8, "discount_amount": 10, "total": 83}
            ),
            ["Subtotal: 80", "Shipping: 5", "Tax: 8", "Discount: 10", "Total: 83"],
        )

    def test_zero_tax_omitted(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 80, "shipping": 5, "tax": 0, "total": 85}
            ),
            ["Subtotal: 80", "Shipping: 5", "Total: 85"],
        )


if __name__ == "__main__":
    unittest.main()
