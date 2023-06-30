a = input()
semi = ''
final = []
length = len(a)
count = 0

# Split the input string and convert to a list of integers
for i in a:
    count += 1
    if count == length:
        semi += i
        if int(semi) not in final:
            final.append(int(semi))
    elif i == ',':
        final.append(int(semi))
        if int(semi) not in final:
            final.append(int(semi))
        semi = ''
    else:
        semi += i

count = 0
ends = []
min_num = max_num =final[0]

# Find the minimum and maximum numbers
for num in final:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

# Find the third smallest and third largest numbers
for i in range(min_num, max_num):
    if i in final:
        ends.append(i)

# Print the results
print("Third smallest:", ends[2])
print("Third largest:", ends[-3])
