import Opisy
import sys

from Funkcje import netto_brutto, brutto_netto


def petla(password):                                # password checksum counter
    total_counter = ""
    lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
    upper = lower.upper()
    digits = "01234567890"
    specials = "!@$%^&*"
    for i in password:
        if i in lower:
            total_counter += "l"
        elif i in upper:
            total_counter += "u"
        elif i in digits:
            total_counter += "d"
        elif i in specials:
            total_counter += "s"
    return total_counter


def set_password(password, total_counter):          # checksum password control
    if password == "e":
        print(Opisy.exit_text)
        sys.exit(0)
    while "l" not in total_counter or "u" not in total_counter or "d" not in total_counter \
            or "s" not in total_counter or len(password) > 12 or len(password) < 6:
        print(Opisy.bad_type_password)
        password = input(Opisy.ask_password_again_text)
        petla(password)
        total_counter = petla(password)
    print(Opisy.correct_password_text)


def logon(logon_ask):                               # Ask about entrance
    while logon_ask != "t" or logon_ask != "n":
        logon_ask = input(Opisy.confirm_logon_text)
        if logon_ask == "t" or logon_ask == "n":
            if logon_ask == "n":
                print(Opisy.exit_text)
                sys.exit(0)
            elif logon_ask == "t":
                break


def confirm_password(password):                     # Confirm your password
    while True:
        ownerpassword = input(Opisy.confirm_password)
        if ownerpassword == "e":
            print(Opisy.exit_text)
            sys.exit()
        elif ownerpassword != password:
            print(Opisy.bad_password)
        else:
            print(Opisy.welcome_text)
            break


def menu(menu_input):
    while menu_input != "e" or menu_input != "o" or menu_input != "r" or menu_input != "s" \
            or menu_input != "d" or menu_input != "a":
        menu_input = input(Opisy.menu_input_text)
        if menu_input == "a":                       # add on menu
            add_on_input = ''
            add_on(add_on_input)
        elif menu_input == "e":                     # exit
            print(Opisy.exit_text)
            sys.exit(0)


def add_on(add_on_input):
    while add_on_input != "b" or add_on_input != "k" or add_on_input != "e" or add_on_input != "r":
        add_on_input = input(Opisy.add_on_text)
        if add_on_input == "b":                       # brutto netto calculator
            ask_brutto_netto = ''
            brutto_netto_calc(ask_brutto_netto)
        elif add_on_input == "e":                     # return to menu
            print(Opisy.exit_text)
            sys.exit(0)
        elif add_on_input == "r":
            break
        elif add_on_input == "k":                     # exit
            rate_interest_start = 0
            interest_rate(rate_interest_start)


def brutto_netto_calc(ask_brutto_netto):
    while ask_brutto_netto != "b" or ask_brutto_netto != "n" or ask_brutto_netto != "e" or ask_brutto_netto != "r":
        ask_brutto_netto = input(Opisy.brutto_netto_calc_text)
        if ask_brutto_netto == "r":
            break
        kwota = float(input(Opisy.salary_text))
        if ask_brutto_netto == "b":
            netto_brutto(kwota)
        elif ask_brutto_netto == "n":
            brutto_netto(kwota)
        elif ask_brutto_netto == "e":
            print(Opisy.exit_text)
            sys.exit(0)


def interest_rate(rate_interest_start):         # rate interest inputs
    print("KALKULATOR OPROCENTOWANIA")
    stan_p = float(input("podaj stan poczatkowy konta\n"))
    procent = float(input("podaj oprocentowanie\n"))
    okres = float(input("ile lat będziez trzymał środki\n"))
    pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
    pytanie = pytanie.lower()
    while not pytanie in ["m", "d", "r"]:
        print("Wybierz zdefiniowaną odpowedź: d - dzień, m - miesiąc, r - rok")
        pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
    miesiąc = okres * 12
    procent_m = procent / 12

    dzień = okres * 365
    procent_d = procent / 365
    if pytanie == "m":
        wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

    elif pytanie == "r":
        wynik = stan_p * ((1 + (procent / 100)) ** okres)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

    elif pytanie == "d":
        wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

