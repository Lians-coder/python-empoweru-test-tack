import random

def main():
    number = random.randint(1, 100)
    attempts = 7
    print(f"Вітаю! Я загадав число від 1 до 100. Спробуй вгадати його за {attempts} спроб.")
    
    for _ in range(attempts):
        guess = input("Введи своє припущення: ")
        try:
            g_int = int(guess.strip())
        except (ValueError, TypeError):
            print(f"'{guess}' не вдалося конвертувати у число. Будь ласка, спробуй ще раз.")
            continue
        if g_int == number:
            print(f"Ти відгадав! Це число {number}.\nСпробуй ще раз!")
            main()
        elif g_int < number:
            print("Занадто маленьке!")
        else:
            print("Занадто велике!")
    print(f"Сумно, ти не відгадав... Це число {number}. Спробуй ще раз!")
    main()         

if __name__ == "__main__":
    main()
    