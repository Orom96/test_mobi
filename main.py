# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
import json

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# #1
# print("I***like***Python")

# #2
# a=input()
# b=input()
# c=input()
# d=input()
# print(b,c,d,sep=a)
#

# 3
# a=int(input())
# print(a+1,a+2)

# 4
# a=int(input())
# b=int(input())
# c=int(input())
#
# print(a+b+c)

# #5
# a=int(input())
# print("Объем =",a**3)
# print("Площадь =",6*(a**2))

# #6
# a=int(input())
# b=int(input())
# c=3*(a+b)**3+275*b**2-127*a-41
# print(c)


# #7
# a=int(input())
# print(a,a*2,a*3,a*4,a*5, sep="---")

# #8
# a=int(input())
# b=a//100
# print(b)

# #9
# a=int(input())
# b=a//60
# c=a%60
# print(a,"мин-", "это",b,"час",c,"минут")


# 10
# a=int(input())
# b=a//100
# c=a//10%10
# d=a%10
# print(f"Сумма цифр: {b+c+d}")
# print(f"Произведение цифр: {b*c*d}")

# #11
# a=int(input())
# if a%2==0:
#     print("Чётное")
# else:print("Нечётное")
#
# #12
# a,b,c=int(input()),int(input()),int(input())
# if b==a+1 and c==a+2:
#     print('YES')
# else:print('NO')

# #13
# a=int(input())
# b=int(input())
# if a<b:
#     print(a)
# else:print(b)

# #14
# a=int(input())
#
# if a<=13:
#     print("детство")
# elif 14<=a<=24:
#     print("молодость")
# elif 25<=a<=59:
#     print("зрелость")
# elif a>=60:
#     print("старость")


# a=int(input())
# if (1<(a/1000)<10)//7 or (1<(a/1000)<10)//17:
#     print("YES")
# else: print("NO")


# a=int(input())
# if -1<a<=17:
#     print("Принадлежит")
# else:print("Не принадлежит")


# # найти промежуток
# a=int(input())
# if -3>=a<7:
#     print("Принадлежит")
# else:print("Не принадлежит")

# среднее число
# a,b,c=int(input()),int(input()),int(input())
# if a<b<c: or c<b<a
#     print(b)
# elif b<a<c or c<a<b:
#     print(b)
# else
#     print(c)

# количество дней
# a=int(input())
# if 1<a<8:
#     if a%2!=0:
#     print("31")
#     elif a==2:
#     print("28")
#     else:print("30")

# a=float(input())
# b=float(input())
# c=float(input())
# d=float()
# e=float()
# b!=0
# c!=0
# d=b+c
# e=a/d
# print(e)

# фио
# a,b,c=input(),input(),input()
# print(a[0],b[0],c[0])


# хороший оттенок
# a=input()
# if "хорошо" in a.lower():
#     print("yes")
# else: print("no")


# # положительное число
# a=float(input())
# print(a%1)
# a=input()
# if "синий" in a.lower():
#     print("yes")
# else: print("no")

# s = input()
# if '@'  in s and '.' in s:
#     print("YES")
# else:
#     print('NO')

# a="abc"
# print (a[-1:3])
# print (a[-2:2])
# print (a[-3:1])

# полинддром
# a=input()
# b=a[::-1]
# if a==b:
#     print("yes")
# else:print("no")
#
# # срезы
# a=input()
# print("количество букв в строке:",len(a))

# print("строка повторенная 3 раза:",a*3)
# b=a[:1]
# print("первый символ строки :",b)
# c=a[:3]
# print("первые три символа строки:",c)
# d=a[-3:]
# print("последние три символа строки:",d)
# e=a[::-1]
# print("строку в обратном порядке:",e)
# f=a[1:-1]
# print("строку с удалением первого и последнего символа:",f)
# import math
#
# a=input()
# b = math.ceil(len(a)/2)
# c=a[:b]
# d=a[b:]
# # print(b,c)
# print(d+c)

# a=input()
# if a.isspace()=="true":
#     if a[0]==a.capi():
#         print('YES')
#     else:print("NO")

# b=input()
# a=b.lower()
# print("аденин:",a.count("а"))
# print("Гуанин:",a.count("г"))
# print("цитозин",a.count('Ц'))
# print("тимин",a.count("т"))
#
# a=input()
# if  a.endswith('.com')  or  a.endswith('.ru'):
#     print('YES')
# else:print('NO')
# # ---------
#
# a=input()
# if '.com' in a  or '.ru' in a:
#     print('YES')
# else:print('NO')

# a=input()
# for i in range(10):
#     print(i,a)

# a=int(input())
# b=int(input())
# if a<=b:
#      for i in range(a,b+1):
#          print(i)

# перчик
# m,n=int(input()),int(input())
# for i in range(m,n-1, -1):
#     if i%2!=0:
#         print(i)


# количество цифр в строке
# a=input()
# for a in range():
#     print(count(a))
#

# повторяй за мной
# a=input()
# for i in range(10):
#     print(i,a)

# квадрат числа
# a=int(input())
# for i in range(a):
#     print("Квадрат числа",i,"равен",i*i)


# # популяция
# a, b, c = int(input()), int(input()), int(input())
# for i in range(1, c + 1):
#     print(a)
#     a = a + (a * b) / 100


# a=int(input())
# for i in range(a):
#     num = input()
#
#     print(num.count("11"))


# a, c = int(input()), input()
# for i in range(c):
#     print(a)
# m,n=int(input()),int(input())
# for i in range(m,n-1, -1):
#     if i%2!=0:
#         print(i)

# a=input()
# if a.isalnum():
#     b="1",
#
#     if b in a:
#         print(a.count(b))


# a = input()
# for i in range(a.lower()):
#         print (a.count())

# a=int(input())
# for i in range(i+1,11):
#     print (a*i)

# input=float(("введите сумму=",a))
# b,c,d,e,f=float(input()),float(input()),float(input()),int(input()),float(),int()
#
# print("процентная ставка",b)
# print("на сколько лет",d)
# e=a+(b/100*10)*d
# f=e-a
# print("Общая сумма за 5 лет =",e)
# print("чистая прибыль равна = ",f)

summa=int(input())
period=float(input())
proc=10
for i in range(summa+proc*10/100,period+1):
    print(i)
