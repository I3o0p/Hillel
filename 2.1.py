
number = int(input("Введіть 4-х значне число: "))

thousands, remainder = divmod(number, 1000)
hundreds, remainder = divmod(remainder, 100)
tens, units = divmod(remainder, 10)

print(thousands)
print(hundreds)
print(tens)
print(units)
