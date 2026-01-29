# List methods 

l = [5,2,3,6,4,7,8,9]
print(l)
l.append(10)
print(l)

m = [6,5,8,4,7,6]
m.sort()
print(m)

m.sort(reverse=True)
print(m)

m.reverse()
print(m)

k = l + m 
print(k)

l.copy()
m = l
m[0]= 0
print(m)

m.insert(5,80)
print(m)

l.extend(m)
print(l)
