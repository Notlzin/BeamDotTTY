# crash.py
import random

def decide_crash_py(is_crashed: bool):
    if is_crashed == True:
        print(f"you crashed at: {random.randint(0, 500)} meters away from something!")
        print("great job at drunk driving")
    else:
        print("great driving! im proud of you, user.")
