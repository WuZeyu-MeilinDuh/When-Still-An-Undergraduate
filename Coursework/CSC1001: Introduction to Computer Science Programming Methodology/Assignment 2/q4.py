# Question 4: Anagrams
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary


def isAnagram(s1, s2):
    ''' 
    Return True if two words are anagrams; otherwise, return False
    parameter s1: string
    parameter s1: string
    return: bools (True/False), the validity
    '''
    # TODO part
    # ------- Your code start here -------

    lst1 = []
    lst2 = []
    for i in range(0, len(s1)):
        lst1.append(s1[i])
    lst1.sort()
    for i in range(0, len(s2)):
        lst2.append(s2[i])
    lst2.sort()
    if lst1 == lst2:
        return True
    else:
        return False

    # ------- End of your code -----------


if __name__ == '__main__':
    # Sample test cases
    # isAnagram("listen", "silent") # anagram
    # isAnagram("listen", "silenc") # not anagram

    # Prompts the user to enter two strings
    # Displays "is an anagram" if they are anagrams; otherwise, displays "is not an anagram"
    str1 = input("Please input your first string: ")
    str2 = input("Please input your second string: ")
    if isAnagram(str1, str2):
        print("is an anagram")
    else:
        print("is not an anagram")