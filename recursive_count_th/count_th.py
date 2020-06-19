'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # set start = to word.find('th')
    start = word.find('th')
    # if the value is not -1 aka it's FOUND the index of 'th'
    if start != -1:
        # return 1 + recurse the function passing in word and go from the index of where "start" aka "th" is and move over 2 letters and check to the end of the word
        return 1 + count_th(word[start+2:])
    else:
        return 0
