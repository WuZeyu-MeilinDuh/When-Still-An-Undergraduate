
def printAnyList( anyList ) :
    result = ''
    for n in range( len(anyList) - 1 ):
        result += anyList[n] + ', '
    return result + 'and' + anyList[-1]

testList = ['China', 'USA', 'Japan']
print( printAnyList( testList ) )