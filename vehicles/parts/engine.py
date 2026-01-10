# engine.py

class CarEngine:
    @classmethod
    def check_if_engine_damaged(cls, engine_damaged: bool, engine_broken: bool, is_damaged: bool):
        if engine_damaged is False and engine_broken is False and is_damaged is False:
            print("engine isnt damaged nor broken, fresh as new")
            print("engine health: &")
            is_damaged = False
        elif engine_damaged is True and engine_broken is False and is_damaged is False:
            print("engine is damaged. stay cautious.")
            print("engine health: @")
            is_damaged = True
        elif engine_damaged is True and engine_broken is True and is_damaged is True:
            print("engine is fully broken. undrivable.")
            print("engine health: !")
            is_damaged = True
        else:
            print("what? unhandled exception? segfault 0xFC00AA1")

    def check_engine_power(self, base_engine_power):
        print(f"engine power is: {base_engine_power}")
        print(f"\t thats it. {base_engine_power} horsepower.")

def runClass():
    class_engine = CarEngine()

    # test
    class_engine.check_if_engine_damaged(False, False, False)
    class_engine.check_engine_power(100)

runClass()
