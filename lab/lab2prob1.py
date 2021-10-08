def ff(n):
    dct = {}
    for i in range(n):
        k = 0
        j = i + 1
        x = 0
        e = 0
        for e in range(i):
            if(s[i] == s[e]):
                x = x + 1
        if x == 0:
            for j in range(n):
                if s[i] == s[j]:
                    k = k + 1
            dct[s[i]] = k
    return dct

s = input("Введіть рядок:")
n = len(s)
print(ff(n))