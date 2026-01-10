# gas_tank.py

def check_gas_amount(gasoline_amount):
    print(f"there are: {gasoline_amount}L currently.")
    if gasoline_amount == 10:
        print("good amount of gas")
    elif gasoline_amount < 10 and gasoline_amount > 0:
        print("hmmm still good")
    elif gasoline_amount < 0:
        print("what the fuck did you do")
    else:
        print("error: gas > float('Infinity')")
