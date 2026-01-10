# test.py
from w_key import move_forwards
from a_key import move_totheleft
from s_key import move_backwards
from d_key import move_totheright

def check_key_type(key: str):
    w = "w"
    a = "a"
    s = "s"
    d = "d"
    if key == "w":
        print(move_forwards(w))
    elif key == "a":
        print(move_totheleft(a))
    elif key == "s":
        print(move_backwards(s))
    elif key == "d":
        print(move_totheright(d))
    else:
        print("key undefined.")

# test
if __name__ == "__main__":
    game_engine_init = True
    while game_engine_init:
        try:
            key = str(input("WASD: "))
            check_key_type(key=key)
        except Exception as e:
            print(f"EXCEPTION: {e}")
