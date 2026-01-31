list1 = [2,4,7,8,11]
2	target = int(input("Enter target:"))
3	for i in range(0,len(list1),1):
4	    for j in range(0,len(list1),1):
5	        if(list1[i]+list1[j]) == target:
6	            print(i,j)
