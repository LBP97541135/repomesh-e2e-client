import unittest

from src.checkout_view import checkout_lines, calculate_quote


class CheckoutViewTest(unittest.TestCase):
    def test_regular_quote(self):
        self.assertEqual(
            checkout_lines({"subtotal": 80, "shipping": 5, "total": 85}),
            ["Subtotal: 80", "Shipping: 5", "Total: 85"],
        )

    def test_quote_with_discount(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 80, "shipping": 5, "discount": 10, "total": 75}
            ),
            ["Subtotal: 80", "Shipping: 5", "Discount: 10", "Total: 75"],
        )

    def test_zero_discount_omitted(self):
        self.assertEqual(
            checkout_lines(
                {"subtotal": 80, "shipping": 5, "discount": 0, "total": 85}
            ),
            ["Subtotal: 80", "Shipping: 5", "Total: 85"],
        )


class CalculateQuoteTest(unittest.TestCase):
    def test_quote_without_discount(self):
        """When subtotal < 300, no discount is applied."""
        items = [{"price": 100, "quantity": 2}]  # subtotal = 200
        quote = calculate_quote(items)
        self.assertEqual(quote["subtotal"], 200)
        self.assertEqual(quote["shipping"], 10)
        self.assertEqual(quote["discount"], 0)
        self.assertEqual(quote["total"], 210)

    def test_quote_with_discount(self):
        """When subtotal >= 300, 30 unit discount is applied."""
        items = [{"price": 100, "quantity": 3}]  # subtotal = 300
        quote = calculate_quote(items)
        self.assertEqual(quote["subtotal"], 300)
        self.assertEqual(quote["shipping"], 10)
        self.assertEqual(quote["discount"], 30)
        self.assertEqual(quote["total"], 280)

    def test_quote_above_threshold(self):
        """Discount applies when subtotal exceeds 300."""
        items = [{"price": 310, "quantity": 1}]  # subtotal = 310
        quote = calculate_quote(items)
        self.assertEqual(quote["subtotal"], 310)
        self.assertEqual(quote["discount"], 30)
        self.assertEqual(quote["total"], 290)

    def test_empty_cart(self):
        """Empty cart results in zero totals."""
        items = []
        quote = calculate_quote(items)
        self.assertEqual(quote["subtotal"], 0)
        self.assertEqual(quote["discount"], 0)
        self.assertEqual(quote["total"], 10)


if __name__ == "__main__":
    unittest.main()
