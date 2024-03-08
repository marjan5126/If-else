a = int(input())
b = int(input())
c = int(input())
if a<b and c<b:
    print(b)
elif b<a and c<a:
    print(c)
else:    
    print(a)

# array_length = int(input())
# array_input = input(array_length)
# user_array = list(map(int, array_input.split()))
# print(user_array[-2])
array_length = int(input())
array_input = input()
user_array = list(map(int, array_input.split()))
user_array.sort()
print(user_array[-2])
