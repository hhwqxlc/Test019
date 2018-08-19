# ids = [1,4,3,3,4,2,3,4,5,6,1]
# ids = list(set(ids))
# print(ids)
# ids = [1,4,3,3,4,2,3,4,5,6,1]
# data = []
# for i in ids:
#     if i not in data:
#         data.append(i)
# print(data)
ids = [1,4,3,3,4,2,3,4,5,6,1]
data=[i for i in ids if ids.count(i)!=1]
print(data)





