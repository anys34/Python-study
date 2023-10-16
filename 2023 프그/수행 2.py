def f(List):
    if List == []:
        return
    print(List.pop(), end=' ')
    f(List)

List = list(input().split())
f(List)
