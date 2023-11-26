#importy
from random import randint, choice

#kolory
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'

#separator
def print_separator():
    separator = f"{Colors.YELLOW}{'-' * 40}{Colors.END}"
    print(separator)

#przywitanie
print_separator()
print(f"{Colors.YELLOW}Witaj w grze Chomik w Parkourze{Colors.END}")

#podanie imienia chomika
name = input(f"{Colors.MAGENTA}Podaj imię swojego chomika: {Colors.END}")
life, strength, karma = 200, 150, 20
print(f"{Colors.MAGENTA}Witaj, {Colors.CYAN}{name}{Colors.END}")

#ataki
def drapanie():
    global strength
    attack = randint(2, 8)
    strength -= 3
    return attack

def ugryzienie():
    global strength
    if strength < 5:
        print(f"{Colors.RED}Nie masz wystarczająco siły!{Colors.END}")
        return 0
    attack = randint(3, 15)
    strength -= 5
    return attack

def kopnij():
    global strength
    if strength < 5:
        print(f"{Colors.RED}Nie masz wystarczająco siły!{Colors.END}")
        return 0
    attack = randint(4, 12)
    strength -= 5
    return attack

def przeskocz():
    print(f"{Colors.GREEN}Udało Ci się przejść przeszkodę, przeskakując ją z gracją!{Colors.END}")
    return 0

def zniszcz():
    global strength
    if strength < 15:
        print(f"{Colors.RED}Nie masz wystarczająco siły!{Colors.END}")
        return 0
    strength -= 15
    print_separator()
    print(f"{Colors.GREEN}Zniszczyłeś przeszkodę, ale straciłeś trochę siły!{Colors.END}")
    return randint(8, 20)

def choose_attack_przeszkody():
    while True:
        print_separator()
        print(f"{Colors.BLUE}1 - Przeskocz{Colors.END}")
        print(f"{Colors.BLUE}2 - Zniszcz{Colors.END}")
        choice = input(f"{Colors.CYAN}Wybierz atak (1-2): {Colors.END}")
        if choice == '1':
            return przeskocz()
        elif choice == '2':
            return zniszcz()
        else:
            print(f"{Colors.RED}Nieprawidłowy wybór. Spróbuj jeszcze raz.{Colors.END}")

def choose_attack_przeciwnicy():
    while True:
        print_separator()
        print(f'{Colors.BLUE}1 - Drapanie{Colors.END}')
        print(f'{Colors.BLUE}2 - Ugryzienie{Colors.END}')
        print(f'{Colors.BLUE}3 - Kopnięcie{Colors.END}')
        choice = input(f"{Colors.CYAN}Wybierz atak (1-3): {Colors.END}")
        if choice == '1':
            return drapanie()
        elif choice == '2':
            return ugryzienie()
        elif choice == '3':
            return kopnij()
        else:
            print(f"{Colors.RED}Nieprawidłowy wybór. Atakujesz pazurami. Spróbuj jeszcze raz.{Colors.END}")

def levele():
    przeszkody = [
        ["Drzewo", 15, 5],
        ["Wiszący Most", 25, 10],
        ["Skała z Mchami", 18, 6]
    ]
    return choice(przeszkody)

opponents = [
    {"name": "Szczur", "life": 20, "attack": 10},
    {"name": "Kot", "life": 30, "attack": 15},
    {"name": "Lew", "life": 50, "attack": 20, "boss": True},
    {"name": "Panna Chomik", "interest": 50}
]

#użyte przeszkody
used_przeszkody = []
used_opponents = []

#lizcznik przeszkód
przeszkody_count = 0
opponents_count = 0

#przeszkody
panna_chomik_encountered = False
while life > 0 and strength > 0:
    if len(used_przeszkody) < len(levele()):
        obstacle = levele()

        while obstacle in used_przeszkody:
            obstacle = levele()

        used_przeszkody.append(obstacle)

        print_separator()
        print(f"{Colors.GREEN}{name} pokonuje przeszkodę: {obstacle[0]}{Colors.END}")
        print(f"{Colors.GREEN}Przeszkoda ma {obstacle[1]} punktów trudności i zadaje Ci {obstacle[2]} obrażeń{Colors.END}")

        life -= obstacle[2]
        if life <= 0:
            break

        print(f"{Colors.GREEN}Masz {life} punktów życia i {strength} punktów siły{Colors.END}")

        attack = choose_attack_przeszkody()

        if attack > 0:
            obstacle[1] -= attack
            print(f"{Colors.GREEN}Udało Ci się przejść przeszkodę, zadając {attack} obrażeń{Colors.END}")

        if obstacle[1] <= 0:
            print_separator()
            print(f'{name} pokonał przeszkodę!!!')
            przeszkody_count += 1

            if obstacle[0] == "Drzewo":
                life += karma
                print(f"{Colors.GREEN}Twój chomik zyskuje {karma} punktów zdrowia dzięki znalezieniu nowej ścieżki!{Colors.END}")


#przeciwnicy
    elif len(used_opponents) < len(opponents):
        chosen_opponent = choice(opponents)

        while chosen_opponent in used_opponents:
            chosen_opponent = choice(opponents)

        used_opponents.append(chosen_opponent)

        #panna chomik
        if chosen_opponent['name'] == "Panna Chomik" and not panna_chomik_encountered:
            panna_chomik_encountered = True
            print_separator()
            print(f"{Colors.GREEN}{name} spotyka {chosen_opponent['name']}!{Colors.END}")

            print(f"{Colors.GREEN}Panna Chomik wydaje się zainteresowana tobą!{Colors.END}")

            print_separator()
            print(f"{Colors.BLUE}1 - Zaproś na randkę{Colors.END}")
            print(f"{Colors.BLUE}2 - Olać i iść dalej{Colors.END}")

            reaction_choice = input(f"{Colors.CYAN}Wybierz numer (1-2): {Colors.END}")

            if reaction_choice == '1':
                print(f"{Colors.GREEN}Chomik zaprosił Pannę Chomik na randkę!{Colors.END}")
            elif reaction_choice == '2':
                print(f"{Colors.GREEN}Chomik olewa Pannę Chomik i idzie dalej.{Colors.END}")
            else:
                print(f"{Colors.RED}Nieprawidłowy wybór. Chomik jest niezdecydowany!{Colors.END}")

        else:
            opponent = chosen_opponent
            print_separator()
            print(f"{Colors.GREEN}{name} spotyka przeciwnika: {opponent['name']}{Colors.END}")
            print(f"{Colors.GREEN}Przeciwnik ma {opponent['life']} punktów życia i zadaje Ci {opponent['attack']} obrażeń{Colors.END}")

            while life > 0 and opponent['life'] > 0:
                attack = choose_attack_przeciwnicy()
                opponent['life'] -= attack

                if attack > 0:
                    print(f"{Colors.GREEN}Zadałeś przeciwnikowi {attack} obrażeń! Pozostało mu {opponent['life']} życia.{Colors.END}")

                if opponent['life'] <= 0:
                    print_separator()
                    print(f'{name} pokonał przeciwnika: {opponent["name"]}!!!')
                    opponents_count += 1
                    break

                print(f"{Colors.GREEN}Masz {life} punktów życia i {strength} punktów siły{Colors.END}")

            if opponents_count == len(opponents) - 1:
                print(f"{Colors.GREEN}Wszyscy przeciwnicy zostali pokonani!{Colors.END}")
                break

#zakończenie parokouru
print_separator()
print(f"{Colors.GREEN}KONIEC DŻUNGLOWEGO PARKOURU!{Colors.END}")

#dom
print_separator()
dom = input(f"{Colors.CYAN}Czy chcesz wejść do domu? (tak/nie): {Colors.END}")

if dom.lower() == 'tak':
    print(f"{Colors.GREEN}Chomik wraca do domu!{Colors.END}")

    print_separator()
    print(f"{Colors.GREEN}W domu czeka na ciebie szczotka, jedzenie i wygodne legowisko.{Colors.END}")

#jedzienie
    print_separator()
    print(f"{Colors.BLUE}Co chcesz dać do jedzenia chomikowi?{Colors.END}")
    print(f"{Colors.BLUE}1 - Karma{Colors.END}")
    print(f"{Colors.BLUE}2 - Warzywa{Colors.END}")
    print(f"{Colors.BLUE}3 - Sałata{Colors.END}")
    print(f"{Colors.BLUE}4 - Trutka na szczury{Colors.END}")

    food_choice = input(f"{Colors.CYAN}Wybierz numer (1-3): {Colors.END}")

    if food_choice == '1':
        print(f"{Colors.GREEN}Chomik dostaje karma i odzyskuje trochę życia!{Colors.END}")
        life += 10
    elif food_choice == '2':
        print(f"{Colors.GREEN}Chomik dostaje warzywa i czuje się lepiej!{Colors.END}")
        life += 5
    elif food_choice == '3':
        print(f"{Colors.GREEN}Chomik dostaje sałatę i odzyskuje trochę życia!{Colors.END}")
        life += 8
    elif food_choice == '4':
        print(f"{Colors.RED}UWAGA: Chomik zmarł po zażyciu Trutki. Gra kończy się tragicznie.{Colors.END}")
        print(f"{Colors.GREEN}KONIEC GRY!{Colors.END}")
        quit()
    else:
        print(f"{Colors.RED}Nieprawidłowy wybór. Chomik jest głodny!{Colors.END}")

#kąpiel
print_separator()
print(f"{Colors.BLUE}Czym chcesz umyć chomika?{Colors.END}")
print(f"{Colors.BLUE}1 - Szampon{Colors.END}")
print(f"{Colors.BLUE}2 - Mydło{Colors.END}")
print(f"{Colors.BLUE}3 - Domestos{Colors.END}")

wash_choice = input(f"{Colors.CYAN}Wybierz numer (1-3): {Colors.END}")

if wash_choice == '1':
    print(f"{Colors.GREEN}Chomik jest teraz czysty i pachnący szamponem!{Colors.END}")
elif wash_choice == '2':
    print(f"{Colors.GREEN}Chomik jest teraz czysty i pachnący mydłem!{Colors.END}")
elif wash_choice == '3':
    print(f"{Colors.RED}UWAGA: Chomik zmarł po użyciu Domestosu. Gra kończy się tragicznie.{Colors.END}")
    print(f"{Colors.GREEN}KONIEC GRY!{Colors.END}")
    quit()
else:
    print(f"{Colors.RED}Nieprawidłowy wybór. Chomik czeka na kąpiel!{Colors.END}")

#sen
print_separator()
sleep_choice = input(f"{Colors.CYAN}Czy chcesz ułożyć chomika do snu? (tak/nie): {Colors.END}")

if sleep_choice.lower() == 'tak':
    print(f"{Colors.GREEN}Chomik kładzie się do snu. Dobranoc!{Colors.END}")
else:
    print(f"{Colors.GREEN}Chomik zostaje aktywny. Dziękujemy za grę!{Colors.END}")