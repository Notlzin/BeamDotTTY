# window_check.py
# manually do shit for you window on the car
# window checker python
from parts.windows import window_type, window_health_check

if __name__ == "__main__":
    print("window_type()")
    print("window_health_check()")
    print("choose which one.")
    userFunc = str(input("choose function: "))
    if userFunc.startswith("window_type()") or userFunc.startswith("window_type"):
        choice1 = str(input("tinted, tempered, or normal glass: "))
        if choice1.startswith("tinted"):
            window_type("tinted")
        elif choice1.startswith("tempered"):
            window_type("tempered")
        elif choice1.startswith("normal"):
            window_type("")
        else:
            print("LUA_ERROR: window type not found")

    elif userFunc.startswith("window_check_health()") or userFunc.startswith("window_check_health"):
        choice2 = str(input("damaged, or broken, or undamaged? choose one: "))
        if choice2.startswith("damaged"):
            window_health_check(True, False)
        elif choice2.startswith("broken"):
            window_health_check(True, True)
        elif choice2.startswith("undamaged"):
            window_health_check(False, False)
        else:
            print("idk, error, fuck off..")

    else:
        print("choice unfound. maybe try reading existing shit?")
