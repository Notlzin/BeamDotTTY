# axles.py

def turning(direction):
    if direction == "left":
        print(f"{"\\---\\"}")
    elif direction == "right":
        print("/---/")
    else:
        print("direction does not exist, go to hyperspace instead")

def turn_left(directions, degrees=90):
    print(f"turning by: {degrees} degrees.")
    if directions == "left":
        turning("left")
    else:
        turning(directions)
        print("note: this is left.")

def turn_right(directions, degrees=90):
    print(f"turning by: {degrees} degrees.")
    if directions == "right":
        turning("right")
    else:
        turning(directions)
        print("note: this is right.")
