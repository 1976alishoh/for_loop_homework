def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s = ""
    for i in range(n):
        s =  s + str(i) +","
    return(s)
print(main(3))