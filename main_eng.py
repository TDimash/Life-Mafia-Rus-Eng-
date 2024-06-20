from colorama import init, Fore, Style
import random
import time
import os

init(autoreset=True)

current_family = "Your Family"
respected_families = [
    {"name": "Family 1", "influence": 50, "members": 20},
    {"name": "Family 2", "influence": 40, "members": 15},
    {"name": "Family 3", "influence": 60, "members": 25}
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
    "Jewelry Store": {"cost": 350000, "min_income": 5000, "max_income": 7000, "upgrade_costs": [10000, 20000, 25000, 30000, 50000, 65000, 74000, 85000, 100000]},
    "Shop": {"cost": 500000, "min_income": 8000, "max_income": 12000, "upgrade_costs": [15000, 25000, 35000, 50000, 75000, 100000, 120000, 150000]},
    "Gas Station": {"cost": 1000000, "min_income": 12000, "max_income": 18000, "upgrade_costs": [30000, 50000, 70000, 100000, 150000, 200000, 250000, 300000]}
}

# House constants
houses = {
    "Poor District": {"cost": 75000, "tax_per_minute": 10, "upgrade_cost": 30000},
    "Middle-class District": {"cost": 150000, "tax_per_minute": 50, "upgrade_cost": 60000},
    "Rich District": {"cost": 2500000, "tax_per_minute": 150, "upgrade_cost": 1000000}
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
    print(Fore.CYAN + Style.BRIGHT + f"\n                  Welcome to the Mafia World!")
    print(Fore.GREEN + Style.BRIGHT + f"Current Respect: {player_respect}")
    print(Fore.GREEN + Style.BRIGHT + f"Money in Wallet: ${player_money}")
    print(Fore.MAGENTA + Style.BRIGHT + f"Your Family's Influence: {get_family_influence(current_family)}")
    print(Fore.MAGENTA + Style.BRIGHT + f"Number of Family Members: {get_family_members_count(current_family)}")
    print(Fore.WHITE + Style.BRIGHT + f"------------------------------- MENU ------------------------------")
    print(Fore.WHITE + Style.BRIGHT + "1. Rob a Casino")
    print(Fore.WHITE + Style.BRIGHT + "2. Make a Deal with Another Family")
    print(Fore.WHITE + Style.BRIGHT + "3. Open a Business in the City")
    print(Fore.WHITE + Style.BRIGHT + "4. Buy a House in the City")
    print(Fore.WHITE + Style.BRIGHT + "5. Check Open Businesses in the City")
    print(Fore.WHITE + Style.BRIGHT + "6. Save and Exit")

def commit_casino_robbery():
    global player_money, player_respect
    print(Fore.CYAN + Style.BRIGHT + f"\nYou decided to rob a casino...")
    time.sleep(1)
    success_chance = random.randint(1, 100)
    if success_chance <= 70:
        money_gained = random.randint(min_money_robbery, max_money_robbery)
        player_money += money_gained
        print(Fore.GREEN + Style.BRIGHT + f"You successfully robbed the casino and earned ${money_gained}!")
        player_respect += respect_gain_robbery
    else:
        print(Fore.RED + Style.BRIGHT + "The robbery failed. You escaped, but without any loot.")
        player_respect -= respect_loss_robbery

def make_deal_with_family():
    global player_respect
    print(Fore.CYAN + Style.BRIGHT + "\nYou decided to make a deal with another family...")
    time.sleep(1)
    success_chance = random.randint(1, 100)
    if success_chance <= 60:
        chosen_family = random.choice(respected_families)
        print(Fore.GREEN + f"A deal with {chosen_family['name']} family has been successfully made!")
        player_respect += respect_gain_deal
        chosen_family['influence'] += 10  # Increase influence of the chosen family after the deal
        chosen_family['members'] += 5  # Increase number of members in the family after the deal
    elif success_chance <= 90:
        print(Fore.YELLOW + Style.BRIGHT + "A deal was made, but without significant gains.")
        player_respect += 5
    else:
        print(Fore.RED + Style.BRIGHT + "The deal failed. Relations may worsen.")
        player_respect -= respect_loss_deal

def open_business():
    global player_money, current_business, current_business_level
    print(Fore.CYAN + Style.BRIGHT + "\nYou decided to open a business in the city...")
    print(Fore.WHITE + Style.BRIGHT + "Available businesses:")
    for idx, business in enumerate(businesses.keys(), start=1):
        print(f"{idx}. {business}")

    choice = input(Fore.CYAN + Style.BRIGHT + "\nChoose a business to open (1-3): ")
    if choice == '1':
        current_business = "Jewelry Store"
    elif choice == '2':
        current_business = "Shop"
    elif choice == '3':
        current_business = "Gas Station"
    else:
        print(Fore.RED + "Invalid choice. Returning to menu.")
        return

    if player_money >= businesses[current_business]['cost']:
        player_money -= businesses[current_business]['cost']
        print(Fore.GREEN + Style.BRIGHT + f"You successfully opened '{current_business}'!")
    else:
        print(Fore.RED + Style.BRIGHT + "You don't have enough money to open this business.")
        current_business = None
        return

    current_business_level = 1
    print(Fore.WHITE + Style.BRIGHT + f"Business Level: {current_business_level}")

def buy_house():
    global player_money, current_house, current_house_level
    print(Fore.CYAN + Style.BRIGHT + "\nYou decided to buy a house in the city...")
    print(Fore.WHITE + Style.BRIGHT + "Available districts for buying a house:")
    for idx, house in enumerate(houses.keys(), start=1):
        print(f"{idx}. {house} (${houses[house]['cost']})")

    choice = input(Fore.CYAN + Style.BRIGHT + "\nChoose a district to buy a house (1-3): ")
    if choice == '1':
        current_house = "Poor District"
    elif choice == '2':
        current_house = "Middle-class District"
    elif choice == '3':
        current_house = "Rich District"
    else:
        print(Fore.RED + "Invalid choice. Returning to menu.")
        return

    if player_money >= houses[current_house]['cost']:
        player_money -= houses[current_house]['cost']
        print(Fore.GREEN + Style.BRIGHT + f"You successfully bought a house in '{current_house}'!")
    else:
        print(Fore.RED + Style.BRIGHT + "You don't have enough money to buy this house.")
        current_house = None
        return

    current_house_level = 1
    print(Fore.WHITE + Style.BRIGHT + f"House Level: {current_house_level}")

def check_open_businesses():
    print(Fore.CYAN + Style.BRIGHT + "\nOpen businesses in the city:")
    for business, details in businesses.items():
        print(f"{business}: Level {current_business_level} (Income: ${details['min_income']}-${details['max_income']})")

def save_and_exit():
    print(Fore.YELLOW + Style.BRIGHT + "\nGame saved. See you next time!")
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
        choice = input(Fore.CYAN + Style.BRIGHT + "\nChoose an action (1-6): ")
        
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
            save_and_exit()
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

        input(Fore.YELLOW + "\nPress Enter to continue...")

if __name__ == "__main__":
    main()
