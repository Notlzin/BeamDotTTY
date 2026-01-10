# doors.py

# configuration
un_damaged_door_health_char = "#"
damaged_door_health_char = ";"
broken_door_health_char = "?"

def open_car_door():
    print("opened car door.")
    print("|    |")

def close_car_door():
    print("closed car door.")
    print("|[___]|")

def check_if_damaged(door_health: int, is_damaged: bool):
    if door_health == 100 and not is_damaged:
        print("door safe to go.")
        print(f"door health: {un_damaged_door_health_char}")
    elif door_health < 100 and door_health > 0 and is_damaged:
        print("door is damaged. stay cautious.")
        print(f"door health: {damaged_door_health_char}")
    elif door_health == 0 and is_damaged:
        print("car door is broken, your car is shit")
        print(f"door health: {broken_door_health_char}")
    else:
        print("unhandled exception (i guess?)")

# test if __name__ == "__main__"
if __name__ == "__main__":
    open_car_door()
    close_car_door()
    check_if_damaged(100, False)
