# added check if user presses cancel and redirect to welcome
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


def add_monster():
    monster_name = eg.enterbox("What is the name of your new MONSTER", "MONSTER name")
    if monster_name is None:
        exit()
    monsters.append(monster_name)
    cards[monster_name] = {}
    for i in stats:
        monster_stat = eg.integerbox(f"What is the level of your MONSTERS {i}", f"MONSTER {i}", lowerbound=1, upperbound=25)
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
