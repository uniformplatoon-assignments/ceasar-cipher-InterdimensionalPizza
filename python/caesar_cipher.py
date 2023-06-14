def caesar_cipher(string, shift_amount):
    abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newstr = ''
    for char in string:
        if char in abc:
            #newstr is appended with the second occurrence of the letter in abc that is matched, and then shifted.
            #This is done to make sure that once the letter is shifted, it still selects a letter of the same case.
            newstr += abc[abc.index(char, abc.index(char)+1) + shift_amount]
        else:
            newstr += char
    return newstr