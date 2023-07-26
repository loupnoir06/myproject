
#1-misol

# s=input('s=')
# arr=[]
# for i in s:
#     n=0
#     for k in s:
#         if k==i:
#             n+=1
#     arr.append(f'{i}:{n},')

# print(f'd={arr}')

#2-misol

# f=open('imthon.txt','r')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('file2.txt','a')
# for i in arr:
#     if i%2==1:
#         f.write(f'{i} 00 ')

#3-misol

# f=open('imthon.txt','r')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('file2.txt','a')
# for i in arr:
#     if i%2==1:
#         f.write(f' {i}{i} ')
#     else:
#         f.write(f'{i}')

#4-misol

# f=open('imthon.txt','r')
# arr=list(map(str,f.read().split()))
# f.close()
# f=open('file2.txt','a')
# for i in arr:
#     f.write(f'{i} ')

#5-misol

# s=input('satr kiriting:')
# s1=input('s1=')
# s2=input('s2=')

# print(s.replace(s1,s2,1 ))

#6-misol

# def soz_son(n):
#     n100=n%1000/100
#     n10=n%100/10
#     n=n%10
#     n1=int(n10)
#     n2=int(n100)
#     s='yuz'
#     dict={
#         0:'',
#         1:'bir',
#         2:'ikki',
#         3:'uch',
#         4:'tort',
#         5:'besh',
#         6:'olti',
#         7:'yetti',
#         8:'sakkiz',
#         9:'toqqiz',
#     }
#     dict1={
#         0:'',
#         1:'o\'n',
#         2:'yigirma',
#         3:'ottiz',
#         4:'qiriq',
#         5:'ellik',
#         6:'otmush',
#         7:'yetmush',
#         8:'sakson',
#         9:'toqson',
#     }
#     if n2==0:
#         s=''
#     print(dict[n2],s,dict1[n1],dict[n])

# n=int(input('n='))
# soz_son(n)