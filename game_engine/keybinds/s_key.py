# s_key.py

x_axis = 0

def move_backwards(key: str):
    global x_axis
    if key == "s":
        x_axis -= 1
        return f"moved x_axis by: {x_axis}"
    else:
        return "key doesnt exist on this function."

# test
if __name__ == "__main__":
    print(move_backwards("s"))
