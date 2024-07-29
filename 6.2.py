seconds_input = int(input("Введіть число більше або дорівнює 0 і менше ніж 8640000: "))

if 0 <= seconds_input < 8640000:

    days, remaining_seconds = divmod(seconds_input, 86400)
    hours, remaining_seconds = divmod(remaining_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "дні"
    else:
        day_word = "днів"

    print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")

else:
    print("Будь ласка, введіть число від 0 до 8639999.")
