import MainMenu, level1, level2, level3, level4, objects, tools, enemy, settings


level = "mainmenu"

isrunning = True
while isrunning:
    if level == "mainmenu":
        level = MainMenu.mainMenuloop()
    if level == "settings":
        level = settings.settings_loop()
    if level == "level1":
        level = level1.leve1loop()
    if level == "level2":
        level = level2.level2loop()
    if level == "level3":
        level = level3.level3loop()
    if level == "level4":
        level = level4.level4loop()

