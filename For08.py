def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    s = 1
    for i in range(1,N):
        s = s +1/i
    return(s)
print(main(4))
