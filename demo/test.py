

# def modify_str():
#     str1='I Love Python'
#     str1.replace('Love','enjoy').split()
#     return str1
    

# print(modify_str())    



# print(-18//4)
# print(2*3**3*4)
# print(10-4*2)
# n1=int(input('Enter 1:'))
# n2=int(input('Enter 2:'))
# n3=int(input('Enter 3:'))


# total=n1+n2+n3

# print(total/3)



# def fibonacci():
#     a,b=0,1
#     while True:
#         yield a
#         print(a)
#         a,b=b,a+b
# f1=fibonacci()        
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))



# list1=[2,3,4,99,12,34,56,65]

# n=len(list1)
# # print(n)

# for i in range(n):
#     # print(i,end=' ')
#     for j in range(i+1,n):
#         # print(j,end=',')
#         if list1[i]>list1[j]:
        
#          list1[i],list1[j]=list1[j],list1[i]

# print(list1)      
#   

        
    

dict1={
    575:'Apple',
    876:'Banana',
    132:'Grapes',
    782:'Mango'
}    

d=sorted(dict1.keys())

dict2={}

for i in d:
    # print(i)
    
    dict2[i]=dict1[i]
print(dict2)
