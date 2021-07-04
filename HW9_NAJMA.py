from unittest import mock
from unittest import TestCase, main
# I struggled to import the modules/functions, so I have just imported the whole piece of code for from ATM.py
# see below for my HW9 answers

def verify_pin(pin):
    if pin == '1234':
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("Too many incorrect tries. Could not log in")
    return False

def run_atm(withdrawal_amount):  # this is a 'main' function
    print("Welcome to the ATM!")
    successful_login = log_in()
    balance = None
    if successful_login:
        balance = 100
        try:
            if withdrawal_amount > balance:
                raise ValueError("Insufficient funds on your account")

            balance = balance - withdrawal_amount
            print("Take the money.\n Your new balance is {}".format(balance))

        except ValueError as err:
            raise ValueError(err)

        else:
            print("Thank you for using ATM")
            return balance
    else:
        print("Exiting Program")
        return balance


#run_atm(50)

# Homework 9 starts here
class VerifyPinFunction(TestCase):
# 1st unit test
    def test_incorrect_pin(self):
        expected = False
        result = 0000
        self.assertEqual(expected, result)

# 2nd unit test
    def test_correct_pin(self):
        expected = 1234
        result = 1234
        self.assertEqual(expected, result)

class PinInvalidFunction(TestCase):
# 3rd unit test
    def test_pin_reject(self):
        expected = verify_pin(pin=1234)
        result = verify_pin(pin=1111)
        self.assertEqual(expected, result)

class PinValidFunction(TestCase):
# 4rd unit test
    def test_pin_accept(self):
        expected = verify_pin(pin=1234)
        result = verify_pin(pin=1234)
        self.assertEqual(expected, result)

class InSufficientFunction(TestCase):
# 5th unit test
    def test_insufficient_funds(self):
        expected = "Insufficient funds on your account"
        result = run_atm(50)
        self.assertNotEqual(expected, result)



if __name__ == '__main__':
    main()


