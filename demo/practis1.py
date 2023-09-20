

# def pair(arr,k):

#     number_seen={}
#     for i in arr:
#         diff=k-i
#         print(diff)

#         if diff in number_seen:
#             return [i,diff]
#         number_seen[i]=True    



    
# print(pair([4,7,8,1,4,3],12))

# import math
def findMin(arr):
    
    left=0
    right=-1

    while left<right:
        mid =math.floor((left+right))
        # print(mid)

        if arr[mid]>arr[right]:
            left=mid+1

        else :
            right=mid

    print(arr[left])

findMin([13,17,18,19,3,6,8,12])                



