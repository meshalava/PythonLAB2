def f(n):
    if n in (1, 2):
        return 1
    return f(n - 1) + f(n - 2)
 
n = int(input("Введіть порядковий номер списку Фібоначчі:"))
print(f(n))
