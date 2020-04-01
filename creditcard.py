#! /usr/bin/env python3

'''
    Verify a credit card number:

    The formula verifies a number against its included check digit, which is 
    usually appended to a partial account number to generate the full account 
    number. This number must pass the following test:

    From the rightmost digit (excluding the check digit) and moving left, 
    double the value of every second digit. The check digit is neither doubled 
    nor included in this calculation; the first digit doubled is the digit 
    located immediately left of the check digit. If the result of this doubling 
    operation is greater than 9 (e.g., 8 × 2 = 16), then add the digits of the 
    result (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or, alternatively, the same 
    final result can be found by subtracting 9 from that result 
    (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).
    Take the sum of all the digits.
    If the total modulo 10 is equal to 0 (if the total ends in zero) then the 
    number is valid according to the Luhn formula; otherwise it is not valid.
    Assume an example of an account number "7992739871" that will have a check 
    digit added, making it of the form 7992739871x:

    Account number        7        9        9        2        7        3        9        8        7        1        x        
    Double every other        7        18        9        4        7        6        9        16        7        2        x
    Sum digits        7        9        9        4        7        6        9        7        7        2        x
    The sum of all the digits in the third row, the sum of the sum digits, is 67.

    The check digit (x) is obtained by computing the sum of the sum digits 
    then computing 9 times that value modulo 10 (in equation form, ((67 × 9) 
    mod 10)). In algorithm form:

    Compute the sum of the sum digits (67).
    Multiply by 9 (603).
    603 mod 10 is then 3, which is the check digit. Thus, x=3.
    (Alternative method) The check digit (x) is obtained by computing the sum 
    of the other digits (third row) then subtracting the units digit from 10 
    (67 => Units digit 7; 10 − 7 = check digit 3). In algorithm form:

    Compute the sum of the sum digits (67).
    Take the units digit (7).
    Subtract the units digit from 10.
    The result (3) is the check digit. In case the sum of digits ends in 0 
    then 0 is the check digit.
    This makes the full account number read 79927398713.

    Each of the numbers 79927398710, 79927398711, 79927398712, 79927398713, 
    79927398714, 79927398715, 79927398716, 79927398717, 79927398718, 
    79927398719 can be validated as follows.

    Double every second digit, from the rightmost: (1×2) = 2, (8×2) = 16, 
    (3×2) = 6, (2×2) = 4, (9×2) = 18
    Sum all the individual digits (digits in parentheses are the products 
    from Step 1): x (the check digit) + (2) + 7 + (1+6) + 9 + (6) + 7 + (4) + 
    9 + (1+8) + 7 = x + 67.
    If the sum is a multiple of 10, the account number is possibly valid. 
    Note that 3 is the only valid digit that produces a sum (70) that is a 
    multiple of 10.
    Thus these account numbers are all invalid except possibly 79927398713 
    which has the correct check digit.
    Alternately, you can use the same checksum creation algorithm, ignoring 
    the checksum already in place as if it had not yet been calculated. Then 
    calculate the checksum and compare this calculated checksum to the original 
    checksum included with the credit card number. If the included checksum 
    matches the calculated checksum, then the number is valid.
'''

def ccverify(cardnumber):
    digits = list(reversed([int(d) for d in str(cardnumber)]))
    sum = 0
    for i in range(1, len(digits), 2):
        d = digits[i] * 2
        while d > 9:
            d -= 9
        sum += d
    for i in range(2, len(digits), 2):
        sum += digits[i]
    newckdigit = (sum * 9) % 10
    if (sum + digits[0]) % 10 == 0 and newckdigit == digits[0]:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        test = input("card number: (0 to end)  ")
        if test == "0":
            break
        print(f"Card: {test} - {ccverify(test)}")
