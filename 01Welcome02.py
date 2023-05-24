import easygui as eg


def welcome():
    while True:
        function = {"Add_Remove": add_remove,
                    "Find_Show": find_show,
                    "Exit": exit}
        guide = eg.buttonbox("Welcome to The Takeaway Shop\n"
                             "What would you like to do today", "The Takeaway Shop",
                             choices=list(function.keys()))
        if guide == "Exit":
            break
        chosen_function = function.get(guide)
        chosen_function()


def add_remove():
    print("workin")


def find_show():
    print("workin")


# Main Routine
welcome()
eg.msgbox("Thanks for playing with the Monster Cards," "Goodbye, and have fun")
