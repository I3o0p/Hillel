number = int(input("Введіть 5-ти значне число: "))

ten_thousands = number // 10000
thousands = (number // 1000) % 10
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

reversed_number = (units * 10000 +
                   tens * 1000 +
                   hundreds * 100 +
                   thousands * 10 +
                   ten_thousands)

print("Перевернуте число:", reversed_number)
