from Stack import Stack

def match(text):
    lefty = '{[('
    righty = '}])'
    stac = Stack()
    for item in text:
        if item in lefty:
            stac.push(item)
        elif item in righty:
            if stac.is_empty():
                return False
            else:
                if righty.index(item) != lefty.index(stac.pop()):
                    return False
    return stac.is_empty()