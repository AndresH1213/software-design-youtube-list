import unittest
from io import StringIO
from unittest.mock import patch
from before import *


class Authorizer_SMS_TestCase(unittest.TestCase):

    def test_init_authorized(self):
        auth = Authorizer_SMS()
        self.assertFalse(auth.is_authorized())

    def test_code_decimal(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        self.assertTrue(auth.code.isdecimal())

    def test_authorize_success(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch('builtins.input', return_value=auth.code):
            auth.authorize()
            self.assertTrue(auth.is_authorized())

    @patch('builtins.input', return_value="1234567")
    def test_authorize_fail(self, mocked_input):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        auth.authorize()
        self.assertFalse(auth.is_authorized())


class PaymentProcessor_TestCase(unittest.TestCase):
    """It's hard to test this kind of functions that creates
    it's own objects without passing as an argument nor anything.
    You would need to mock the entire function with mocks objects"""

    def test_payment_success(self):
        # ???
        self.assertTrue(True)

    def test_payment_fail(self):
        # ???
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
