# choose_car.py

def choose_car(car):
    while True:
        try:
            if car.startswith("sedan"):
                print("spawned sedan!")
                exit()
                break
            elif car.startswith("truck"):
                print("spawned truck!")
                exit()
                break
            elif car.startswith("exit"):
                print("goodbye!!")
                break
            else:
                print("vehicle does not exist... yet.")
        except KeyboardInterrupt as KeyInt:
            print(f"keyboard interrupt: {KeyInt}, unallowed to INT.")

choose_car("sedan")
