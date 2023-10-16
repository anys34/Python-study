def f(List):
    if len(List) == 1:
        return List[0]
    max = f(List[1:])
    return List[0] if List[0] > max else max

List = list(map(int, input().split()))
print(f(List))
