# First task
'''from sympy import isprime

num = int(input())

print(isprime(num))'''


# Second task
'''a = set(input('Enter something '))
b = set(input('Enter something '))
print(a - b)'''

# Third task
'''example = input('Enter an example: ').split(' ')
if example[1] == '+':
    print(int(example[0]) + int(example[2]))
elif example[1] == '-':
    print(int(example[0]) - int(example[2]))
elif example[1] == '*':
    print(int(example[0]) * int(example[2]))
elif example[1] == '/':
    print(int(example[0]) / int(example[2]))
else:
    print('Error')'''

# Fourth task
'''n = (input('Enter a number: '))
num_lst = list(n)
int_num_lst = []
for i in num_lst:
    int_num_lst.append(int(i))
result = 0
for i in int_num_lst:
    result += i
print(result)
while result >= 10:
    int_lst_result = []
    list(str(result))
    for a in list(str(result)):
        int_lst_result.append(int(a))
    dop_result = 0
    for a in int_lst_result:
        dop_result += a
    print(dop_result)
    result = dop_result'''

# Fourth task
n = input('Enter a number: ')
result = 0
num_lst = list(n)
int_num_lst = []
for i in num_lst:
    int_num_lst.append(int(i))
while int(n) > 9:
    for i in int_num_lst:
        result += i
    n = result
print(n)

'''n = int(input('Input a number: '))
while n > 9:
    n = sum(map(int, str(n)))
print(n)'''






















