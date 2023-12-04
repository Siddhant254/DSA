queries = [[0,4],[1,1],[2,4],[1,4],[1,3]]
li = [2,3,-1,4,7]
pre = []
pre_sum = 0
pre.append(pre_sum)
for i in li:
    pre_sum += i
    pre.append(pre_sum)
print(pre)
print(li)

for i in queries:
    start = i[0] #starting index
    end = i[1]  # ending index
    print("[{},{}]".format(start,end))
    print((pre[end+1] - pre[start])/((end-start)+1))
    print()
