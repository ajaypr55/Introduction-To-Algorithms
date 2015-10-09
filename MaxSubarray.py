def Find_Max_Crossing_Subarray(A,lo,mid,hi):
    left_sum = -float("inf")
    sum = 0
    max_left = 0
    for i in range(mid,lo+1,-1):
        print i
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
            
    right_sum = -float("inf")
    sum = 0
    max_right = 0
    for j in range(mid+1,hi+1):
        sum = sum+A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left,max_right,left_sum+right_sum)
    
def Find_Max_Subarray(A,lo,hi):
    if lo == hi:
        return (lo,hi,A[lo])
    mid = lo+(hi-lo)/2
    left_tuple = Find_Max_Subarray(A,lo,mid)
    right_tuple = Find_Max_Subarray(A,mid+1,hi)
    cross_tuple = Find_Max_Crossing_Subarray(A,lo,mid,hi)
    if left_tuple[2] >= right_tuple[2] and left_tuple[2] >=cross_tuple[2]:
        return left_tuple
    if right_tuple[2] >= left_tuple[2] and right_tuple[2] >= cross_tuple[2]:
        return right_tuple
    else:
        return cross_tuple
        
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print Find_Max_Subarray(A,0,15)
        
        
    
    