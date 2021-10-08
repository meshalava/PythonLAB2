s = open('lab2.txt', 'r')
text=s.readlines()
a = input("Введіть шуканий символ або символи:") + '\n'
n = len(text)
for i in range(n):
    if text[i].endswith(a) == True:
        l = text[i]
        print(l[::-1])
s.close()

