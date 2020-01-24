'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    l = list(word)
    if len(l) <= 1:
        return count
    else:
        if l[0] == "t" and l[1] == "h":
            del(l[0:2])
            return 1+count_th(l)

        else:
            del(l[0])
            return count_th(l)
