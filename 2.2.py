number = int(input("Введіть 5-значне число: "))

ten_thousands, remainder = divmod(number, 10000)
thousands, remainder = divmod(remainder, 1000)
hundreds, remainder = divmod(remainder, 100)
tens, units = divmod(remainder, 10)

print(ten_thousands)
print(thousands)
print(hundreds)
print(tens)
print(units)
