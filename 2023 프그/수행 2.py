def f(list_test):
    a = list_test.pop(0)
    if(len(list_test) == 0):
        print(a, end=' ')
        return
    f(list_test)
    print(a, end=' ')

list_test = list(input().split())

f(list_test)
