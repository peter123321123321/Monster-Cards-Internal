import easygui as eg

cards = {"Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
         "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
         "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
         "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
         "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
         "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
         "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
         "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
         "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
         "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}}
stats = ["Strength", "Speed", "Stealth", "Cunning"]
monsters = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem", "Websnake", "Moldvine", "Vortexwing", "Rotthing",
            "Froststep", "Wispghoul"]


def welcome():
    while True:
        function = {"Add_Remove": add_monster,
                    "Remove MONSTER": remove_monster,
                    "Find_Show": find_show,
                    "Exit": exit}
        guide = eg.buttonbox("Welcome to The Takeaway Shop\n"
                             "What would you like to do today", "The Takeaway Shop",
                             choices=list(function.keys()))
        if guide == "Exit":
            break
        chosen_function = function.get(guide)
        chosen_function()


def add_monster():
    monster_name = eg.enterbox("What is the name of your new MONSTER", "MONSTER name")
    if monster_name is None:
        exit()
    monsters.append(monster_name)
    cards[monster_name] = {}
    for i in stats:
        monster_stat = eg.integerbox(f"What is the level of your MONSTERS {i}", f"MONSTER {i}",
                                     lowerbound=1, upperbound=25)
        if monster_stat is None:  # Check if the user pressed Cancel
            exit()
        cards[monster_name][i] = monster_stat
    while True:
        check = eg.buttonbox(f"Are the details of this MONSTER card correct\n{monster_name}, {cards[monster_name]}",
                             "Check details", choices=["Yes", "No"])
        if check == "Yes":
            break
        change = eg.buttonbox("Which stat would you like to change", "Stat change",
                              choices=["Strength", "Speed", "Stealth", "Cunning"])
        if change is None:  # Check if the user pressed Cancel
            exit()
        edit_stat = eg.integerbox(f"The original stat was {cards[monster_name][change]} "
                                  f"what would you like the new stat to be", "Stat change", lowerbound=1, upperbound=25)
        if edit_stat is None:
            exit()
        cards[monster_name][change] = edit_stat


def remove_monster():
    monster_index = 0
    while True:
        if len(monsters) == 0:
            eg.msgbox("No MONSTERS found in the catalog.")
            return

        monster_name = monsters[monster_index]
        monster_stats = cards[monster_name]
        mns = f"{monster_name}\n"

        for stat in stats:
            mns += f"[{stat}: {monster_stats[stat]}] "
        total_stats = sum(monster_stats.values())
        mns += f"\n[Total Stats: {total_stats}]"

        choice = eg.buttonbox(mns, "MONSTER Catalogue", choices=["Previous", "Next", "Delete", "Exit"])
        if choice is None:
            exit()

        if choice == "Previous":
            monster_index -= 1
        elif choice == "Next":
            monster_index += 1
            if monster_index >= len(monsters):
                monster_index = 0
        elif choice == "Delete":
            del cards[monster_name]
            monsters.remove(monster_name)
            if monster_index >= len(monsters):
                monster_index = 0
        else:
            break


def find_show():
    choice = eg.buttonbox("Would you like to find a MONSTER or show all MONSTER", "Find or Show MONSTERS",
                          choices=["Find MONSTER", "Show MONSTERS"])
    if choice == "Show MONSTERS":
        monster_index = 0
        while True:
            monster_name = monsters[monster_index]
            monster_stats = cards[monster_name]
            mns = f"{monster_name}\n"

            for stat in stats:
                mns += f"[{stat}: {monster_stats[stat]}] "
            total_stats = sum(monster_stats.values())
            mns += f"\n[Total Stats: {total_stats}]"

            choice = eg.buttonbox(mns, "MONSTER Catalogue", choices=["Previous", "Next", "Exit"])
            if choice is None:
                exit()

            if choice == "Previous":
                monster_index -= 1
            elif choice == "Next":
                monster_index += 1
                if monster_index >= len(monsters):
                    monster_index = 0
            else:
                break
    elif choice == "Find MONSTER":
        find = ""
        while find != "Return":
            find = eg.buttonbox("Which MONSTER would you like to find", "MONSTER find", choices=monsters,)
            monster_find = cards.get(find)
            if monster_find is not None:
                monster_details = f"{find}\n"
                for stat in stats:
                    monster_details += f"[{stat}: {monster_find[stat]}] "
                stat_total = sum(monster_find.values())
                monster_details += f"\n[Total Stats: {stat_total}]"
                eg.msgbox(monster_details)


# Main Routine
welcome()
eg.msgbox("Thanks for playing with the MONSTER Cards, Goodbye, and have fun", "Goodbye")


