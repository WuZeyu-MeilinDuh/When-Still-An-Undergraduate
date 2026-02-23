print('Please enter the month in integer as...')
reply1 = int(input())
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
month = months[reply1 - 1]
print('Please enter the day in integer as ...')
reply2 = int(input())
bankA = ['st','nd','rd','th'] #调用不同的后缀。
if reply2 % 10 == 3 and reply2 != 13:
    day = str( reply2 ) + bankA[2]
elif reply2 % 10 == 2 and reply2 != 12:
    day = str( reply2 ) + bankA[1]
elif reply2 % 10 == 1 and reply2 != 11:
    day = str( reply2 ) + bankA[0]
else:
    day = str( reply2 ) + bankA[3]
print('The date is: ' + str(month) + '. ' + day)