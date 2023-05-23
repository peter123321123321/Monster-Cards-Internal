# combo that adds it to a database so that the monster cards used in previous versions are still there,
# Let it take float as a price

import easygui as eg


def welcome():
    while True:
        guide = eg.buttonbox("Welcome to The Takeaway Shop\n"
                             "What would you like to do today", "The Takeaway Shop",
                             choices=["Add or remove a combo", "Find or show combos", "Exit"])
        if guide == "Exit":
            break
        function = {"Add_Remove": add_remove,
                    "Find_Show": find_show}
        chosen_function = function.get(guide)
        chosen_function()


def add_remove():
    print("")


def find_show():
    print("")


# Main Routine
welcome()
eg.msgbox("Thanks for playing with the Monster Cards," "Goodbye, and have fun")


