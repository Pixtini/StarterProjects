nums = [2,2,1,1,1,3]
k = 2

nums_str = []
for i in range(len(nums)):
    nums_str.append(str(nums[i]))

def occurance(e):
    global nums
    count = 0
    for i in range(len(nums)):
        if nums[i] == int(e):
            count += 1
    return count


nums_str.sort(reverse=True,key=occurance)

print_list = []
j = 0

while len(print_list) != k:
    if int(nums_str[j]) not in print_list:
        print_list.append(int(nums_str[j]))
    j += 1
print(print_list)
    

        
        
        
        
        
