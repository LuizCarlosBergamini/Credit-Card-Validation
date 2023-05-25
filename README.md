# Credit Card Validation

This Python program performs credit card validation based on the Luhn algorithm. It allows users to input a credit card number and checks its validity. Additionally, it identifies the type of credit card (AMEX, MASTERCARD, or VISA) based on the first two digits of the card number.

## How it Works

1. The program prompts the user to input a credit card number as an integer.
2. The entered credit card number is then validated using the Luhn algorithm, which ensures that the number is mathematically consistent.
3. If the credit card number is valid, the program determines its type by comparing the first two digits to predefined patterns for AMEX, MASTERCARD, and VISA.
4. The program then outputs the detected card type ("AMEX", "MASTERCARD", or "VISA") or "INVALID" if the card number is not valid.

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Run the `main()` function in the Python script.
3. Enter a credit card number when prompted.
4. The program will validate the number and display the detected card type if valid.
5. If the credit card number is invalid, it will display "INVALID".

## Requirements

- Python 3.x

