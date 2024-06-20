from colorama import init, Fore, Style
import random
import time
import os

init(autoreset=True)

current_family = "Ваша семья"
respected_families = [
    {"name": "Семья 1", "influence": 50, "members": 20},
    {"name": "Семья 2", "influence": 40, "members": 15},
    {"name": "Семья 3", "influence": 60, "members": 25}
]
player_respect = 0
player_money = 100

# Constants for robbery and deal outcomes
min_money_robbery = 15000
max_money_robbery = 20000
respect_gain_robbery = 15
respect_loss_robbery = 5
respect_gain_deal = 20
respect_loss_deal = 0

# Business constants
businesses = {
    "Ювелирная": {"cost": 350000, "min_income": 5000, "max_income": 7000, "upgrade_costs": [10000, 20000, 25000, 30000, 50000, 65000, 74000, 85000, 100000]},
    "Магазин": {"cost": 500000, "min_income": 8000, "max_income": 12000, "upgrade_costs": [15000, 25000, 35000, 50000, 75000, 100000, 120000, 150000]},
    "Заправка": {"cost": 1000000, "min_income": 12000, "max_income": 18000, "upgrade_costs": [30000, 50000, 70000, 100000, 150000, 200000, 250000, 300000]}
}

# House constants
houses = {
    "Бедный район": {"cost": 75000, "tax_per_minute": 10, "upgrade_cost": 30000},
    "Нормальный район": {"cost": 150000, "tax_per_minute": 50, "upgrade_cost": 60000},
    "Богатый район": {"cost": 2500000, "tax_per_minute": 150, "upgrade_cost": 1000000}
}

current_house = None
current_house_level = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = [
        "                  █───███─███─███─────────",
        "                  █────█──█───█───────────",
        "                  █────█──███─███─────────",
        "                  █────█──█───█───────────",
        "                  ███─███─█───███─────────",
        "                  ───█───█─████─███─███─████",
        "                  ───██─██─█──█─█────█──█──█",
        "                  ───█─█─█─████─███──█──████",
        "                  ───█───█─█──█─█────█──█──█",
        "                  ───█───█─█──█─█───███─█──█"
    ]
    for line in banner:
        print(Fore.RED + "\033[38;5;214m" + line + "\033[0m")

def print_menu():
    print_banner()
    print(Fore.CYAN + Style.BRIGHT + f"\n                  Добро пожаловать в мир мафии!")
    print(Fore.GREEN + Style.BRIGHT + f"Текущее уважение: {player_respect}")
    print(Fore.GREEN + Style.BRIGHT + f"Деньги в кошельке: ${player_money}")
    print(Fore.MAGENTA + Style.BRIGHT + f"Влиятельность вашей семьи: {get_family_influence(current_family)}")
    print(Fore.MAGENTA + Style.BRIGHT + f"Количество членов вашей семьи: {get_family_members_count(current_family)}")
    print(Fore.WHITE + Style.BRIGHT + f"------------------------------- MENU ------------------------------")
    print(Fore.WHITE + Style.BRIGHT + "1. Ограбление казино")
    print(Fore.WHITE + Style.BRIGHT + "2. Заключить сделку с другой семьёй")
    print(Fore.WHITE + Style.BRIGHT + "3. Открыть бизнес в городе")
    print(Fore.WHITE + Style.BRIGHT + "4. Купить дом в городе")
    print(Fore.WHITE + Style.BRIGHT + "5. Проверить какие бизнесы открыты в городе")
    print(Fore.WHITE + Style.BRIGHT + "6. Сохранить и выйти")

def commit_casino_robbery():
    global player_money, player_respect
    print(Fore.CYAN + Style.BRIGHT + f"\nВы решили ограбить казино...")
    time.sleep(1)
    success_chance = random.randint(1, 100)
    if success_chance <= 70:
        money_gained = random.randint(min_money_robbery, max_money_robbery)
        player_money += money_gained
        print(Fore.GREEN + Style.BRIGHT + f"Вы успешно ограбили казино и заработали ${money_gained}!")
        player_respect += respect_gain_robbery
    else:
        print(Fore.RED + Style.BRIGHT + "Ограбление не удалось. Вы сбежали, но без добычи.")
        player_respect -= respect_loss_robbery

def make_deal_with_family():
    global player_respect
    print(Fore.CYAN + Style.BRIGHT + "\nВы решили заключить сделку с другой семьёй...")
    time.sleep(1)
    success_chance = random.randint(1, 100)
    if success_chance <= 60:
        chosen_family = random.choice(respected_families)
        print(Fore.GREEN + f"Сделка с семьёй {chosen_family['name']} заключена успешно!")
        player_respect += respect_gain_deal
        chosen_family['influence'] += 10  # Увеличиваем влиятельность выбранной семьи после сделки
        chosen_family['members'] += 5  # Увеличиваем количество членов семьи после сделки
    elif success_chance <= 90:
        print(Fore.YELLOW + Style.BRIGHT + "Сделка была заключена, но без особых выгод.")
        player_respect += 5
    else:
        print(Fore.RED + Style.BRIGHT + "Сделка не состоялась. Отношения могут ухудшиться.")
        player_respect -= respect_loss_deal

def open_business():
    global player_money, current_business, current_business_level
    print(Fore.CYAN + Style.BRIGHT + "\nВы решили открыть бизнес в городе...")
    print(Fore.WHITE + Style.BRIGHT + "Доступные бизнесы:")
    for idx, business in enumerate(businesses.keys(), start=1):
        print(f"{idx}. {business}")

    choice = input(Fore.CYAN + Style.BRIGHT + "\nВыберите бизнес для открытия (1-3): ")
    if choice == '1':
        current_business = "Ювелирная"
    elif choice == '2':
        current_business = "Магазин"
    elif choice == '3':
        current_business = "Заправка"
    else:
        print(Fore.RED + "Неверный выбор. Возврат в меню.")
        return

    if player_money >= businesses[current_business]['cost']:
        player_money -= businesses[current_business]['cost']
        print(Fore.GREEN + Style.BRIGHT + f"Вы успешно открыли бизнес '{current_business}'!")
    else:
        print(Fore.RED + Style.BRIGHT + "У вас недостаточно денег для открытия бизнеса.")
        current_business = None
        return

    current_business_level = 1
    print(Fore.WHITE + Style.BRIGHT + f"Уровень бизнеса: {current_business_level}")

def buy_house():
    global player_money, current_house, current_house_level
    print(Fore.CYAN + Style.BRIGHT + "\nВы решили купить дом в городе...")
    print(Fore.WHITE + Style.BRIGHT + "Доступные районы для покупки дома:")
    for idx, house in enumerate(houses.keys(), start=1):
        print(f"{idx}. {house} (${houses[house]['cost']})")

    choice = input(Fore.CYAN + Style.BRIGHT + "\nВыберите район для покупки дома (1-3): ")
    if choice == '1':
        current_house = "Бедный район"
    elif choice == '2':
        current_house = "Нормальный район"
    elif choice == '3':
        current_house = "Богатый район"
    else:
        print(Fore.RED + "Неверный выбор. Возврат в меню.")
        return

    if player_money >= houses[current_house]['cost']:
        player_money -= houses[current_house]['cost']
        print(Fore.GREEN + Style.BRIGHT + f"Вы успешно купили дом в '{current_house}'!")
    else:
        print(Fore.RED + Style.BRIGHT + "У вас недостаточно денег для покупки дома.")
        current_house = None
        return

    current_house_level = 1
    print(Fore.WHITE + Style.BRIGHT + f"Уровень дома: {current_house_level}")

def check_open_businesses():
    print(Fore.CYAN + Style.BRIGHT + "\nОткрытые бизнесы в городе:")
    for business, details in businesses.items():
        print(f"{business}: Уровень {current_business_level} (Доход: ${details['min_income']}-${details['max_income']})")

def save_and_exit():
    print(Fore.YELLOW + Style.BRIGHT + "\nИгра сохранена. До новых встреч!")
    exit()

def get_family_influence(family_name):
    for family in respected_families:
        if family['name'] == family_name:
            return family['influence']
    return 0

def get_family_members_count(family_name):
    for family in respected_families:
        if family['name'] == family_name:
            return family['members']
    return 0

def main():
    while True:
        clear_screen()
        print_menu()
        choice = input(Fore.CYAN + Style.BRIGHT + "\nВыберите действие (1-6): ")
        
        if choice == '1':
            clear_screen()
            commit_casino_robbery()
        elif choice == '2':
            clear_screen()
            make_deal_with_family()
        elif choice == '3':
            clear_screen()
            open_business()
        elif choice == '4':
            clear_screen()
            buy_house()
        elif choice == '5':
            clear_screen()
            check_open_businesses()
        elif choice == '6':
            clear_screen()
            save_and_exit()
        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")

        input(Fore.YELLOW + "\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
