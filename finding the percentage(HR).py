n = int(input())

c = 1
students = {}
while c <= n :
    line = input()
    inList = line.split()
    students[inList[0]] = inList[1:4]
    c += 1
    
student = input()

sum = 0
for gs in students[student]:
    sum = sum + float(gs)

print('{0:.2f}'.format(sum / 3))
