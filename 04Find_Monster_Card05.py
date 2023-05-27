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
stat_edit = stats + ["Name"]
choices = monsters + ["Exit"]


find = ""
while find != "Exit":
    find = eg.buttonbox("Which MONSTER would you like to find", "MONSTER find", choices=choices,)
    monster_find = cards.get(find)
    while True:
        # Asks user if the details are correct + prints MONSTER details
        check = eg.buttonbox(f"Are the details of this MONSTER card correct\n{find}, {cards[find]}",
                             "Check details", choices=["Yes", "No"])
        # Checks if the user is happy with the MONSTER
        if check == "Yes":
            break
            # Asks user what stat they would like to change
        change = eg.buttonbox("Which stat would you like to change", "Stat change",
                              choices=stat_edit)
        # If they want to change the name ask them for the new name then replace the old one with new one
        if change == "Name":
            new_name = eg.enterbox("What would you like the new MONSTERS name to be", "Change MONSTER Name")
            # Check if user presses cancel
            if new_name is None:
                break
            cards[new_name] = cards.pop(find)
            # Replace name in list
            monsters[monsters.index(find)] = new_name
            find = new_name
        else:
            # Asks user what they want to change the stat to + print original stat
            edit_stat = eg.integerbox(f"The original stat was {cards[find][change]} "
                                      f"what would you like the new stat to be", "Stat change",
                                      lowerbound=1, upperbound=25)
            # Check if user pressed cancel
            if edit_stat is None:
                break
            # Add new stat to dictionary
            cards[find][change] = edit_stat
