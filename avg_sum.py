queries = [[0,4],[1,1],[2,4],[1,4],[1,3]]
li = [2,3,-1,4,7]

for i in q:
    start = i[0] #starting index
    end = i[1]  # ending index
    
    sum = 0
    for j in range(start:(end+1)):
        sum += li[j]
        
print(sum/((end-start)+1))
