# truck.py
import sys, os
from game_engine.keybinds.w_key import move_forwards
from game_engine.keybinds.a_key import move_totheleft
from game_engine.keybinds.s_key import move_backwards
from game_engine.keybinds.d_key import move_totheright

# force path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(r"D:\\beamng\\game_engine\\keybinds")

class Truck:
    def __init__(self):
        self.x_axis = 0
        self.z_axis = 0

    def move_forward(self):
        print(move_forwards("w"))
        self.x_axis += 0.5
        print(f"in reality, you moved: {self.x_axis}, lmao")

    def move_backward(self):
        print(move_backwards("s"))
        self.x_axis -= 0.5
        print(f"in reality, you moved: {self.x_axis}, lmao!!! (i said it louder)")

    def move_left(self):
        print(move_totheleft("a"))
        self.z_axis -= 0.5
        print(f"in reality, you moved: {self.z_axis}... okay")

    def move_right(self):
        print(move_totheright("d"))
        self.z_axis += 0.5
        print(f"in reality, you moved: {self.z_axis}, qwertyuiop")

    def honk(self):
        print("HONK")
        print("go away")

def start_truck_engine():
    # for fun
    truck = Truck()
    while True:
        print("WASD\nor....\nHONK.\nchoose which one.")
        yourChoice = str(input("choice: "))
        if yourChoice in ['w', "W"]:
            truck.move_forward()
        elif yourChoice in ['s', "S"]:
            truck.move_backward()
        elif yourChoice in ['a', 'A']:
            truck.move_left()
        elif yourChoice in ["d", 'D']:
            truck.move_right()
        elif yourChoice in ["honk", "HONK"]:
            truck.honk()
        else:
            print("choice does not exist!")

if __name__ == "__main__":
    start_truck_engine()
