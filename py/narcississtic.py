def is_narcissistic(num):
    num_str = str(num)
    num_digits = len(num_str)
    return num == sum(int(digit) ** num_digits for digit in num_str)

narcissistic_numbers = [i for i in range(100, 1000) if is_narcissistic(i)]
print(narcissistic_numbers)
