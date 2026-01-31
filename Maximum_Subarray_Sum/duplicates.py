a = [23,78,90,90,102,179,179,200]
list2=[]
n = 0 
for i in range(1,len(a),1):
    if a[i]!=a[i-1]:
        list2.append(a[i])
        
        
        
print(list2)        
