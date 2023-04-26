val = int(input())
output = "Weird"
if val%2 == 1:
    pass
elif 2 <= val < 5:
    output = "Not Weird"
elif 6 <= val <= 20:
    pass
else:
    output = "Not Weird"

print(output)
