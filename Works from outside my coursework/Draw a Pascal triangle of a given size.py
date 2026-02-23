# define function to initialise an array with dimension n*m
def init_array( row, col ):
    r = 0  
    arr = []  
    while r < row:
        c = 0  
        temp_line = []  
        while c < col:
            temp_line.append( 1 )  
            c = c + 1
        arr.append( temp_line )  
        r = r + 1
    # print( arr )
    return arr
# function initArray ends.

# print pascal triangle with format
def print_pas_triangle( arr ):
    for row in range( len( arr ) ):
        for col in range( len( arr ) - row ):
            print( ' ', end='' )
        for col in range( row + 1 ):
            print( str( int( arr[row][col] ) ) + ' ', end='' )
        print()
# function print_pas_triangle ends.

n = int( input( 'Enter the size of the triangle by layers: ') )

pascalArray = init_array( n, n )

# Computing
for i in range( 2,n ):
    for j in range( 1,i ):
        pascalArray[i][j] =  pascalArray[i-1][j-1] + pascalArray[i-1][j]

print_pas_triangle( pascalArray )



