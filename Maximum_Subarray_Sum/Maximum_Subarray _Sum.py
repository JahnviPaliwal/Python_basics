list1 = [23,78,90,11,67]
list2 = []
sum1=0
for i in range(0,len(list1),1):
    for j in range(0,len(list1),1):
        for k in range(i,j,1):
            sum1+=list1[k]
        list2.append(sum1)
        sum1=0    
        
        
print(max(list2))  
