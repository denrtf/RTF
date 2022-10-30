try:
    try:
        print("start")
        print(Hello)
        print("End. No erorr")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)
