def main():
    while True:
        try:
            creditcard_num = int(input("Credit Card: "))
            break
        except ValueError:
            print("Thats, not an integer.")

    if bool(check_card(creditcard_num)):

        # To interact with number more easily we'll turn into a str
        creditcard = str(creditcard_num)

        amexList = ['37', '34']
        mastercardList = ['51', '52', '53', '54', '55']
        
        first_two_digits = creditcard[:2]
        if first_two_digits in amexList:
            print("AMEX")
        elif first_two_digits in mastercardList:
            print("MASTERCARD")
        else:
            print("VISA")

    else:
        print("INVALID")

def check_card(creditcard_num):
    card_length = len(str(creditcard_num))
    multiplied_numbers = []
    for i in range(1, card_length, 2):
        digit_tm = get_digit(creditcard_num, i)
        digit_tm *= 2
        if digit_tm > 9:
            digit_tm = (digit_tm // 10) + (digit_tm % 10)
        multiplied_numbers.append(digit_tm)

    for i in range(0, card_length, 2):
        digit_nm = get_digit(creditcard_num, i)
        multiplied_numbers.append(digit_nm)

    numbers_sum = sum(multiplied_numbers)
    if numbers_sum % 10 == 0:
        return True

    return False

def get_digit(number, n):
    return (number // 10**n) % 10

main()
