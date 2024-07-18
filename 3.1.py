num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Помилка: ділення на нуль неможливе!"
    else:
        result = num1 / num2
else:
    result = "Невірна операція!"

print(f"Результат: {result}")
