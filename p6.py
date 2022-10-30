try:
    print("start")
    print(10/0)
    print("End. No erorr")
except NameError:
    print("Houston, we have a problem")
except ZeroDivisionError:
    print("U cant do this")

print("End code")
