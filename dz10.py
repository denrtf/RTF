currency = {
    'UAN': 36.5,
    'USD': 1,
}


def covert(dollar, currency ="DOLLAR"):
    try:
        return dollar * course[currency]
    except KeyError:
        print("This currency does not exist")


def reload(arg):
    for key, val in arg.items():
        print(key, val)


while True:
    output = int(input())
    if output == 1:
        purchase_currency = input("Enter your currency : ")
        purchase_amount = int(input("Enter purchase amount: "))
        print(f"Bought", {covert(purchase_amount, purchase_currency)}, {purchase_currency})