# beams.py
import sys

def beams(beams_amount: int):
    for i in range(beams_amount):
        sys.stdout.write(f"Beams #{i} registered.\n")

beams(50)
