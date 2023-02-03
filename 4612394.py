def fun(n):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [dict[r] for r in n]
    return sum(value if value >= next_value else -value for value, next_value in zip(values[:-1], values[1:])) + values[-1]
for i in range(5):
    n = input()
    print(fun(n))