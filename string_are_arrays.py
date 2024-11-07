import sys
count = 0

string = sys.argv
string.pop(0)
for i in string:
    for j in i:
        if (j == 'z'):
            print('z')
            count+=1

if (count == 0):
    print('none')
