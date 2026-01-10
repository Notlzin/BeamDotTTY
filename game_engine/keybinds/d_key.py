# d_key.py

z_axis = 0

def move_totheright(key: str):
    global z_axis
    if key == "d":
        z_axis += 1
        return f"moved z_axis by: {z_axis}"
    else:
        return "key doesnt exist on this function."

# test
if __name__ == "__main__":
    print(move_totheright("d"))
    print(move_totheright("d"))
    print(move_totheright("d"))
