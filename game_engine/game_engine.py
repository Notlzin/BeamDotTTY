# game_engine.py
import time

tips_array = ["did you know: this is a terminal only game.", "tip: always control yourself in keybinds.", "stupidly coded in python",
              "notes: you'd have to run everything on your own, just fork, pull to your folder, then play. voila :D"]

class GameEngine:
    def __init__(self):
        self.game_engine_initialized = False
        self.game_engine_state = False
        self.game_initialized = False

    def initializeGameEngine(self):
        print("initializing game engine...")
        print("might take a while...")
        for tips in tips_array:
            print(tips)
            time.sleep(1.5)
        time.sleep(25)
        print("finished initialization.")
        self.game_engine_initialized = True

    def change_game_state(self):
        print("changing game state in the code...")
        time.sleep(2.88)
        print("self.game_engine_state = True")
        self.game_engine_state = True

    def initializeGame(self):
        print("initializing game...")
        self.game_initialized = True
        time.sleep(10)


# game test
if __name__ == "__main__":
    GameEngine().initializeGameEngine()
    GameEngine().change_game_state()
    GameEngine().initializeGame()
