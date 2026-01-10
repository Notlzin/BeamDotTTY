# windows.py

# config
window_health_normal = "<>"
window_health_damaged = "L:"
window_health_broken = "$%"

def window_type(win_type):
    if win_type == "tinted":
        print("its a tinted window!!")
    elif win_type == "bulletproof":
        print("bulletproof glass (!!!)")
    elif win_type == "tempered":
        print("its a tempered glass, ok")
    else:
        print("normal window glass")

def window_health_check(window_damaged: bool, window_broken):
    if window_damaged and window_broken is not True:
        print("window is just fine.")
        print(" _________")
        print("|_________|")
        print(f"win health: {window_health_normal}")
    elif window_damaged is True and window_broken is not True:
        print("window is damaged, glass cracked, waiting to be shattered.. (maybe? possibly. LOL)")
        print("|_  ___ _/")
        print(f"window health: {window_health_damaged}")
    elif window_damaged is True and window_broken is True:
        print("window broken, good luck =)")
        print("\\_  _   _/")
        print(f"window/win health: {window_health_broken}")
    else:
        print("what the fuck?")
