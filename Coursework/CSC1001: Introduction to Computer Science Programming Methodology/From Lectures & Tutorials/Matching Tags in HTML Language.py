from Stack import Stack

def match(mssge):
    stac = Stack()
    j = mssge.find('<')

    while j != -1:
        k = mssge.find('>', j+1)
        if k == -1:
            return False
        piece = mssge[j+1: k]
        if not piece.startswith('/'):
            stac.push(piece)
        else:
            if piece[1: ] != stac.pop():
                return False
        j = mssge.find('<', k+1)

    return stac.is_empty()