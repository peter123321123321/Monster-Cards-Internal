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
monsters = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem", "Websnake", "Moldvine", "Vortexwing", "Rotthing",
            "Froststep", "Wispghoul", "Return"]
stats = ["Strength", "Speed", "Stealth", "Cunning"]


find = ""
while find != "Return":
    edit = eg.buttonbox("Which MONSTER would you like to edit", "Edit MONSTER", choices=monsters)
    monster_edit = ""
    while monster_edit != "Return":
        monster_edit = eg.buttonbox("Would you like to change any of this MONSTERS stats", "Edit MONSTER",
                                    choices=["Strength", "Speed", "Stealth", "Cunning", "Return"])
        change_stat = eg.integerbox(f"The original stat was {cards[edit][monster_edit]} "
                                    f"what would you like the new stat to be", "Stat change", lowerbound=1,
                                    upperbound=25)
        cards[edit][monster_edit] = change_stat
