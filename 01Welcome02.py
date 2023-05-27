import easygui as eg


def welcome():
    while True:
        function = {"Add MONSTER": add_monster,
                    "Remove MONSTER": remove_monster,
                    "Find Show": find_show,
                    "Exit": exit}
        guide = eg.buttonbox("Welcome to The Takeaway Shop\n"
                             "What would you like to do today", "The Takeaway Shop",
                             choices=list(function.keys()))
        if guide == "Exit":
            break
        chosen_function = function.get(guide)
        chosen_function()


def add_monster():
    eg.msgbox("Add_Monster")


def remove_monster():
    eg.msgbox("Remove_Monster")


def find_show():
    eg.msgbox("Find_Show")


# Main Routine
welcome()
eg.msgbox("Thanks for playing with the Monster Cards," "Goodbye, and have fun")
