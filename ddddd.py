f = open("tutoring.txt", "r")
A=[]
for l in f:
    a = list(l.strip())
    a.remove('/')
    a.remove('/')
    line = ''.join(a)
    list_dv = line.split()
    d = list_dv[0]
    v = list_dv[1]
    A.append((int(d), int(v)))
print(A)
f.close()