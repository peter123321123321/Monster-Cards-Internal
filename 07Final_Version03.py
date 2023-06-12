"""This is the final version combining all the previous
components and modified to adhere to the feedback given."""
import easygui as eg


# Function directing user to chosen function
def welcome():
    while True:
        # Dictionary with options for each function
        function = {"Add MONSTER": add_monster,
                    "Remove MONSTER": remove_monster,
                    "Find/Show MONSTER": find_show,
                    "Exit": exit}
        # Button box that lets you choose a function to redirect to
        guide = eg.buttonbox("Welcome to The MONSTERS\n"
                             "What would you like to do", "The MONSTERS",
                             choices=list(function.keys()))
        if guide == "Exit":
            break
        # Direct to the chosen function
        chosen_function = function.get(guide)
        chosen_function()


# Function that lets user add + edit monster cards
def add_monster():
    # Enterbox for user to input MONSTER name
    monster_name = eg.enterbox("What is the name of your "
                               "new MONSTER", "MONSTER Name")
    # Check for if the user presses cancel
    if monster_name is None:
        return
    # Check for if the name user chose is already a MONSTER name
    elif monster_name in monsters:
        eg.msgbox(f"{monster_name} is already taken",
                  "MONSTER Name Taken")
        return
    temp_stats = {}
    # Loops and asks user the level of each of the MONSTERS stats
    for i in stats:
        monster_stat = eg.integerbox(f"What is the level of your "
                                     f"MONSTERS {i}", f"MONSTER {i}",
                                     lowerbound=1, upperbound=25)
        # Check for if the user presses cancel
        if monster_stat is None:
            temp_stats.clear()
            return
        # Adds stat to temp dictionary
        temp_stats[i] = monster_stat

    # Add monster name to dictionary
    monsters.append(monster_name)
    cards[monster_name] = {}
    cards[monster_name] = temp_stats
    while True:
        # Asks user if the details are correct + prints MONSTER details
        check = eg.buttonbox(f"Are the details of this MONSTER card correct"
                             f"\n{monster_name}, {cards[monster_name]}",
                             "Check details", choices=["Yes", "No"])
        # Checks if the user is happy with the MONSTER
        if check == "Yes":
            break
            # Asks user what stat they would like to change
        change = eg.buttonbox("Which stat would you like to change",
                              "Stat change", choices=stat_edit)
        # If they want to change the name ask them for the new name
        # then replace the old one with new one
        if change == "Name":
            new_name = eg.enterbox("What would you like the MONSTERS new"
                                   " name to be", "Change MONSTER Name")
            # Check if user presses cancel
            if new_name is None:
                break
            cards[new_name] = cards.pop(monster_name)
            # Replace name in list
            monsters[monsters.index(monster_name)] = new_name
            monster_name = new_name
        else:
            # Asks user what they want to change the stat to
            # + print original stat
            edit_stat = eg.integerbox(f"The original stat was "
                                      f"{cards[monster_name][change]}\n"
                                      f"what should the new stat be",
                                      "Stat change",
                                      lowerbound=1, upperbound=25)
            # Check if user pressed cancel
            if edit_stat is None:
                break
            # Add new stat to dictionary
            cards[monster_name][change] = edit_stat


# Function that lets user delete monster cards
def remove_monster():
    monster_index = 0
    while True:
        if len(monsters) == 0:
            eg.msgbox("No MONSTERS found in the catalogue.")
            return
        monster_name = monsters[monster_index]
        monster_stats = cards[monster_name]
        mns = f"{monster_name}\n"
        # Loops through each stat and adds it to mns
        for stat in stats:
            mns += f"[{stat}: {monster_stats[stat]}] "
        # Adds total stats to mns
        total_stats = sum(monster_stats.values())
        mns += f"\n[Total Stats: {total_stats}]"
        # Prints mns, Asks user if they want to go to the
        # Previous, Next, Delete the current MONSTER, or Exit
        choice = eg.buttonbox(mns, "MONSTER Catalogue",
                              choices=["Previous", "Next",
                                       "Delete", "Exit"])
        # Check for if the user presses cancel
        if choice is None:
            exit()
        # If choice is Previous -1 from monster_index
        if choice == "Previous":
            monster_index -= 1
        # If choice is Next +1 to monster_index
        elif choice == "Next":
            monster_index += 1
            # Check for if the monster_index goes past the last monster
            # it'll go back to the start
            if monster_index >= len(monsters):
                monster_index = 0
        # If choice is Delete remove MONSTER from list and dictionary
        elif choice == "Delete":
            del cards[monster_name]
            monsters.remove(monster_name)
            if monster_index >= len(monsters):
                monster_index = 0
        else:
            break


# Function that lets the user search for a specific monster
# or print to the python dictionary
def find_show():
    # Asks user whether they want to find or show MONSTERS
    choice = eg.buttonbox("Would you like to view a MONSTER or "
                          "show all MONSTERS", "Find or Show MONSTERS",
                          choices=["Find MONSTER", "Show MONSTERS"])
    if choice == "Show MONSTERS":
        print()
        # loops through dictionary printing MONSTER + stats
        for monster, stat in cards.items():
            print(f"{monster}, {stat}")
    elif choice == "Find MONSTER":
        find = ""
        while find != "Exit":
            find = eg.buttonbox("Which MONSTER would you like to find",
                                "MONSTER find",
                                choices=list(cards.keys()) + ["Exit"])
            if find == "Exit":
                break
            # Asks user if the details are correct + prints MONSTER details
            check = eg.buttonbox(f"Are the details of this MONSTER card "
                                 f"correct\n{find}, {cards[find]}",
                                 "Check details", choices=["Yes", "No"])
            # Checks if the user is happy with the MONSTER
            if check == "Yes":
                break
                # Asks user what stat they would like to change
            change = eg.buttonbox("Which stat would you like to change",
                                  "Stat change", choices=stat_edit)
            # If they want to change the name ask them for the new name
            # then replace the old one with new one
            if change == "Name":
                new_name = eg.enterbox("What would you like the MONSTERS new"
                                       " name to be", "Change MONSTER Name")
                # Check if user presses cancel
                if new_name is None:
                    break
                cards[new_name] = cards.pop(find)
                # Replace name in list
                monsters[monsters.index(find)] = new_name
                find = new_name
            else:
                # Asks user what they want to change the stat to
                # + print original stat
                edit_stat = eg.integerbox(f"The original stat was "
                                          f"{cards[find][change]} "
                                          f"what would you like the new "
                                          f"stat to be", "Stat change",
                                          lowerbound=1, upperbound=25)
                # Check if user pressed cancel
                if edit_stat is None:
                    break
                # Add new stat to dictionary
                cards[find][change] = edit_stat


# Main Routine
# Dictionary storing MONSTER cards
cards = {"Stoneling": {"Strength": 7, "Speed": 1,
                       "Stealth": 25, "Cunning": 15},
         "Vexscream": {"Strength": 1, "Speed": 6,
                       "Stealth": 21, "Cunning": 19},
         "Dawnmirage": {"Strength": 5, "Speed": 15,
                        "Stealth": 18, "Cunning": 22},
         "Blazegolem": {"Strength": 15, "Speed": 20,
                        "Stealth": 23, "Cunning": 6},
         "Websnake": {"Strength": 7, "Speed": 15,
                      "Stealth": 10, "Cunning": 5},
         "Moldvine": {"Strength": 21, "Speed": 18,
                      "Stealth": 14, "Cunning": 5},
         "Vortexwing": {"Strength": 19, "Speed": 13,
                        "Stealth": 19, "Cunning": 2},
         "Rotthing": {"Strength": 16, "Speed": 7,
                      "Stealth": 4, "Cunning": 12},
         "Froststep": {"Strength": 14, "Speed": 14,
                       "Stealth": 17, "Cunning": 4},
         "Wispghoul": {"Strength": 17, "Speed": 19,
                       "Stealth": 3, "Cunning": 2}}
# List of MONSTER stats
stats = ["Strength", "Speed", "Stealth", "Cunning"]
# List of MONSTERS
monsters = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem",
            "Websnake", "Moldvine", "Vortexwing", "Rotthing",
            "Froststep", "Wispghoul"]
# Stats + Name for editing
stat_edit = stats + ["Name"]
welcome()
# Prints goodbye message
eg.msgbox("Thanks for playing with the MONSTER Cards,\n"
          "Goodbye, and have fun!", "Goodbye")
