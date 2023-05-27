import easygui as eg
monster_cards = {"Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
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

while True:
    name = eg.enterbox("What is the name of your new MONSTER", "MONSTER name")
    monster_cards[name] = {}
    strength = eg.enterbox("What is the Strength of your new MONSTER", "MONSTER name")
    speed = eg.enterbox("What is the Speed of your new MONSTER", "MONSTER name")
    stealth = eg.enterbox("What is the  Stealth of your new MONSTER", "MONSTER name")
    cunning = eg.enterbox("What is the Cunning of your new MONSTER", "MONSTER name")
    monster_cards[name]["Strength"] = strength
    monster_cards[name]["Speed"] = speed
    monster_cards[name]["Stealth"] = stealth
    monster_cards[name]["Cunning"] = cunning
    redo = ""
    while redo != "Exit":
        for stat, value in monster_cards.items():
            print(f"{stat}, {value}")
        redo = eg.buttonbox("Which stat would you like to change", "Stat change", choices=stats)
        if redo == "Strength":
            strength = eg.enterbox("What is the Strength of your new MONSTER", "MONSTER name")
            monster_cards[name]["Strength"] = strength
        elif redo == "Speed":
            speed = eg.enterbox("What is the Speed of your new MONSTER", "MONSTER name")
            monster_cards[name]["Speed"] = speed
        elif redo == "Stealth":
            stealth = eg.enterbox("What is the Stealth of your new MONSTER", "MONSTER name")
            monster_cards[name]["Stealth"] = stealth
        elif redo == "Cunning":
            cunning = eg.enterbox("What is the Cunning of your new MONSTER", "MONSTER name")
            monster_cards[name]["Cunning"] = cunning
