# sedan.py
from game_engine.keybinds.w_key import move_forwards
from game_engine.keybinds.a_key import move_totheleft
from game_engine.keybinds.s_key import move_backwards
from game_engine.keybinds.d_key import move_totheright
from game_engine.crash import decide_crash_py
from .parts.wheels import turn_wheel_left, turn_wheel_right
from .parts.hubcaps import is_hubcap_hit_boundaries, is_hubcaps_on_the_wheel
import sys
import os

# force path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# config
x_axis = 0

# test
class Sedan:
    @classmethod
    def move_left(cls):
        print(move_totheleft("a"))
        turn_wheel_left()

    def move_right(self):
        print(move_totheright("d"))
        turn_wheel_right()

    def move_forward(self):
        print(move_forwards("w"))

    def move_backward(self):
        print(move_backwards("s"))

def start_shit():
    global x_axis
    sedan = Sedan()
    while True:
        user_direction = str(input("WASD key: "))
        if user_direction.startswith("w") or user_direction.startswith("W"):
            x_axis += 1
            sedan.move_forward()
        elif user_direction.startswith("a"):
            sedan.move_left()
        elif user_direction.startswith("s"):
            x_axis -= 1
            sedan.move_backward()
        elif user_direction.startswith("d"):
            sedan.move_right()
        else:
            print("where are YOU going???")

# test
if __name__ == "__main__":
    if x_axis%2 == 0:
        decide_crash_py(True)
        is_hubcap_hit_boundaries(True)
        is_hubcaps_on_the_wheel(False)
    start_shit()
