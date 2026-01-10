# open_doors.py
from parts.doors import open_car_door, close_car_door

def choiceMaker(choice):
    if choice.startswith("open"):
        open_car_door()
    elif choice.startswith("close"):
        close_car_door()
    else:
        print("door went to 5D realm")

should_open_doors = str(input("open_or_close: "))

if __name__ == "__main__":
    choiceMaker(should_open_doors)
