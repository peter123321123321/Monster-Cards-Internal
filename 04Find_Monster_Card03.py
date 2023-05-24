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
            "Froststep", "Wispghoul", "Return"]


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


find = ""
while find != "Return":
    find = eg.buttonbox("Which MONSTER would you like to find", "MONSTER find", choices=monsters,)
    monster_find = cards.get(find)
    if monster_find is not None:
        monster_details = f"{find}\n"
        for stat in stats:
            monster_details += f"[{stat}: {monster_find[stat]}] "
        stat_total = sum(monster_find.values())
        monster_details += f"\n[Total Stats: {total_stats}]"
        eg.msgbox(monster_details)
