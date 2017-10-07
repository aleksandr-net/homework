#!/usr/bin/python3.5

n = int(input())
p = int(input())

f_input = open('data.txt')

f_output1 = open('out-1.txt', 'w')
f_output1.write('')
f_output1.close()

f_output2 = open('out-2.txt', 'w')
f_output2.write('')
f_output2.close()

lst_input = list(f_input.read().replace('\n','').split(' '))
lst_output = []

i = 0

while i < len(lst_input):
    if int(lst_input[i]) % n == 0:
        f_output1 = open('out-1.txt', 'a')
        f_output1.write(str(lst_input[i]) + ' ')
        f_output1.close()
    else:
        pass
    i += 1

f_output1 = open('out-1.txt')
temp = f_output1.read()
f_output1.close()
f_output1 = open('out-1.txt', 'w')
f_output1.write(temp.strip())
f_output1.close()

i = 0

while i < len(lst_input):
    lst_output.append(int(lst_input[i]) ** p)
    f_output2 = open('out-2.txt', 'a')
    f_output2.write(str(lst_output[i]) + ' ')
    f_output2.close()
    i += 1

f_output2 = open('out-2.txt')
temp = f_output2.read()
f_output2.close()
f_output2 = open('out-2.txt', 'w')
f_output2.write(temp.strip())
f_output2.close()

f_input.close()
