arr=['mon','Tue','Wed','Thu','Fri','sat','sun']
arr1=[0,1,2,3,4,5,6,1,2,3,4,5,6,]
Ans=[]


for i in range(0,len(arr)):
    # print(i)
    for j in arr1:    
        # print(j,end=',')    
         Ans.append(arr[j])
    break


print(Ans)    


    

    
   
