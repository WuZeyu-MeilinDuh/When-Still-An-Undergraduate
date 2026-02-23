'''
A = 【 1，2，0】
    【 3，-1，4】

A‘ = 【1，3】
     【2，-1】
     【0，4】
'''


def produce(a):
    form = []
    for i in range(1, a + 1):
        form.append([])
    return form



print('Let me make you a matrix, and I will transpose it automatically.')
print('Give me an integer x, for the number of rows intended.')
rows = int(input())
print('Now give me an integer y, for the number of columns intended.')
columns = int(input())
matrix = produce(rows)
for a in range(1, rows + 1):
    print('For row ' + str(a) + ' you would type in?(please press Enter each time after you give the number)')
    for b in range(1, columns):
        t = int(input())
        matrix[a - 1].append(t)
        print('Next?')
    k = int(input())
    matrix[a - 1].append(k)
print('Good. Your intended matrix is as follows.')
for i in range(0, rows):
    print(matrix[i])



print('Would you like your matrix transposed? Please reply yes or no.')
reply = input()
if reply == 'yes':
    print('Your transposed matrix is as follows.')
    matrix_t = produce(columns)
    for m in range(0, rows):
        for n in range(0, columns):
            matrix_t[n].append(matrix[m][n])
    for r in range(0, columns):
        print(matrix_t[r])
    print('Programme completed.')
if reply == 'no':
    print('Programme completed.')