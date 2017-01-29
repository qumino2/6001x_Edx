# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 1:
        return aStr
    elif len(aStr) == 2:
        return aStr[1:] + aStr[0:1] 
    else:
        return reverseString(aStr[1:]) + aStr[:1] 
#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if word.index(x[0:1]) > word.index(x[1:2]):
        return False
    if len(x) == 2 and word.index(x[0:1]) < word.index(x[1:2]):
        return True

    else:
        return x_ian(x[1:], word)

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) <= lineLength:
        return text
    else:
        if text[lineLength:lineLength+1] == ' ':
            return text[0:lineLength] + "\n" + insertNewlines(text[lineLength+1 :], lineLength)
        else:
            for i in range(100):
                if text[lineLength+i: lineLength+i+1] == ' ':
                    return text[0:lineLength + i] + "\n" + insertNewlines(text[lineLength+i+1:], lineLength)







