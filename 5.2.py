while True:
    try:
        num1 = float(input("Введіть перше число: "))
        operation = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Ділення на нуль!")
                continue
        else:
            print("Неправильна операція!")
            continue

        print(f"Результат: {result}")

    except ValueError:
        print("Введено некоректне число!")
        continue

    continue_calculation = input("(y/yes для продовження): ").strip().lower()
    if continue_calculation not in ('y', 'yes'):
        print("Робота калькулятора завершена.")
        break
