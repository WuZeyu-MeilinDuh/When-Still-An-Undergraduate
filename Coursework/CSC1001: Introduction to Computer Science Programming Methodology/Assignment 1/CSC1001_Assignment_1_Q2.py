def hexa(var):
    var_s = var #创建一个备用值，当原始值出于计算需要而被改动时，可以使用备用值。
    if var_s > 16:
        global ex #ex是最高幂。
        for i in range(0, 20):
            if var_s > 16**i and var_s <= 16**(i + 1):
                ex = i #求得ex。
                break
        bank = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        digit = [] #digit是十六进制下，该数字每一位使用十进制表示的序列。
        for b in range(ex, -1, -1): #对给定的16的幂。
            for a in range(1, 16): #a是digit列表中的元素；通过依次分离各次幂的系数来确定十六进制的数。
                if var - a * 16**b >= 0 and var - (a + 1) * 16**b < 0:
                    var = var - a * 16**b #此处会修改原始var，故开头设置var_s。
                    digit.append(a)
                    break
        if var_s % 16 != 0:
            for c in range(0, len(digit)):
                d = digit[c]
                print(bank[d], end = '')
        if var_s % 16 == 0: #修正当var取特殊值16的倍数的情况。
            for c in range(0, len(digit)):
                d = digit[c]
                print(bank[d], end = '')
            print(bank[0])
    if var_s < 16 and var_s >= 0: #修正当var取特殊值小于16的情况。
        print(var_s)
    if var_s == 16: #修正当var取特殊值16的情况。
        print(10)

print('Please enter an integer, so that I will transfer it as a hexadecimal number. The integer of choice can be set to be smaller than 0.')
num = int(input())
if num >= 0:
    hexa(num)
if num < 0: #处理负数的情况。
    num_s = -num
    print('-', end = '')
    hexa(num_s)