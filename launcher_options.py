# launcher_options.py
import random, time

def options(option):
    if option == "1":
        print("running the game...")
        print("BEAMNG.TTY. THE BEST TERMINAL GAME.")
        print("return 0;")
    elif option == "2":
        print("running the game (still)")
        print("BEAMNG.TTY. THE BEST TERMINAL GAME. (still)")
        print('return 1; (??!)')
    elif option == "3":
        print(f"cleared cache: {random.randint(0, 1000)} bytes.")
    elif option == "4":
        print("verifying shit.exe...")
        time.sleep(10)
        print("done!")
    else:
        print("choice does not exists. consider reading the source code?")

if __name__ == "__main__":
    while True:
        print("before starting: here are some things: ")
        print("1. start the game normally")
        print("2. automatic mode (no mods. yet. for now.)")
        print("3. clear cache. (somehow)")
        print("4. verify integrity (check files.)")
        choice = input("choose which ones: ")
        options(choice)
