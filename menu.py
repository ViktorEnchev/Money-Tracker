from money_tracker_menu import MTMenu
import os


def menu_choice():
    while True:
        choice = input('Your action: ')

        if(
            choice == '1' or choice == '2' or choice == '3' or
            choice == '4' or choice == '5' or choice == '6'
        ):
            break

    return int(choice)


def print_menu():
    os.system('clear')
    print("1 - show all data")
    print("2 - show data for specific date")
    print('3 - show expenses, ordered by categories')
    print('4 - add new income')
    print('5 - add new expense')
    print('6 - exit\n')


def interact_with_menu(choice, menu, interact):
    os.system('clear')

    if choice == 1:
        menu.show_all_data()
        input('Continue')

    if choice == 2:
        while True:
            os.system('clear')

            day = input('Day: ')
            month = input('Month: ')
            year = input('Year: ')

            try:
                menu.show_data_for_specific_date(day, month, year)
            except ValueError:
                continue
            else:
                input('Continue')
                break

    if choice == 3:
        menu.show_expenses_ordered_by_cat()
        input('Continue')

    if choice == 4:
        menu.add_inc()
        input('Continue')

    if choice == 5:
        menu.add_exp()
        input('Continue')


def main():
    os.system('clear')

    mt = MTMenu()

    name = input('Your name: ')
    os.system('clear')

    print('Hello {}.'.format(name))
    input('Continue')

    interact = True

    while interact:
        print_menu()
        choice = menu_choice()

        if choice == 6:
            os.system('clear')
            print("Goodbye, {}.\nHave a nice day!".format(name))
            input('Continue')
            interact = False

        else:
            interact_with_menu(choice, mt, interact)


if __name__ == '__main__':
    main()
