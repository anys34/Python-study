def f(list_test):
    if (len(list_test) == 0):
        return 0
    return int(list_test.pop()) + f(list_test)

list_test = list(input().split())

print(f(list_test))