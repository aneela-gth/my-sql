str="aneela"
vowels="aeiou"
v_count=0
c_count=0
for i in str:
    if i in vowels:
        v_count+=1
    else:
        c_count+=1
print(v_count)
print(c_count)

lst = [1, 2, 1, 3, 1, 3]
dupl = []

for i in lst:
    if lst.count(i) > 1 and i not in dupl:
        dupl.append(i)

print(dupl)

lst1 = [[1, 2], [3, 4], [5, 6]]
flat=[]
for sub in lst1:
    for item in sub:
        flat.append(item)
print(flat)

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = []

for i in a:
    if i in b and i not in common:
        common.append(i)

print(common)


lst = [1, 2, 3, 4, 5, 6]
groups = []

for i in range(0, len(lst), 2):
    groups.append(lst[i:i+2])

print(groups)