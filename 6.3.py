user_input = int(input("Введіть ціле число: "))

num = abs(user_input)

while num > 9:
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    num = product

print(num)
