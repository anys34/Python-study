def f(List):
    if List == []:
        return 0
    return List.pop() + f(List)

List = list(map(int, input().split()))
print(f(List))
