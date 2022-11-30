#Задание 3.10
print("Задание 3.10")

print("Введите число")
n = int(input())
 
s = ''
h = '0123456789ABCDEF'
 
while n > 0:
    s = h[n % 16] + s
    n = n // 16

print("Ваше число в шеснадцатиричной системе:")
print(s)





#Задание 3.11
print("Задание 3.11")
print("Введите свою строку")
s = input()

try:
    temp = float(s)
    if s.__contains__("."):
        print("число является дробным")
    else:
        print("Число не является двробным")
except:
    print("число не дробное")




#Задание 3.12
print("Задание 3.12")

print("Введите строку")
s = input()

count_s_rus = s.count("о")
count_s_eng = s.count("o")

if count_s_rus >= 2 or count_s_eng >= 2:
    if count_s_rus >= 2:
        first_index = s.find("о")
        last_index = s.rfind("о")
        print(s[first_index:last_index+1])
    elif count_s_eng >= 2:
        first_index = s.find("o")
        last_index = s.rfind("o")
        print(s[first_index:last_index+1])
else:
    print("о - одна или не встречается.")

