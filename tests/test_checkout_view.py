import unittest

from src.checkout_view import checkout_lines


class CheckoutViewTest(unittest.TestCase):
    def test_regular_quote(self):
        self.assertEqual(
            checkout_lines({"subtotal": 80, "shipping": 5, "total": 85}),
            ["Subtotal: 80", "Shipping: 5", "Total: 85"],
        )


if __name__ == "__main__":
    unittest.main()
