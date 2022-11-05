def raise_to_degrees(number):
    i = 0
    while True:
        result = number**i
        yield result
        if result > 1000**20:
            break
        i += 1


res = raise_to_degrees(123454)
print(res)
for _ in res:
    print(_)
    print("----------")

