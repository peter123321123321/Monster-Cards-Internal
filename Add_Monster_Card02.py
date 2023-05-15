# changed while check != Yes to wile true so that it stop when the user says Yes
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

monster_name = eg.enterbox("What is the name of your new MONSTER", "MONSTER name")
cards[monster_name] = {}
for i in stats:
    monster_stat = eg.integerbox(f"What is the level of your MONSTERS {i}", f"MONSTER {i}", lowerbound=1, upperbound=25)
    cards[monster_name][i] = monster_stat
while True:
    check = eg.buttonbox(f"Are the details of this MONSTER card correct\n{monster_name}, {cards[monster_name]}",
                         "Check details", choices=["Yes", "No"])
    if check == "Yes":
        break
    change = eg.buttonbox("Which stat would you like to change", "Stat change",
                          choices=["Strength", "Speed", "Stealth", "Cunning"])
    change_stat = eg.integerbox(f"The original stat was {cards[monster_name][change]} "
                                f"what would you like the new stat to be", "Stat change", lowerbound=1, upperbound=25)
    cards[monster_name][change] = change_stat
