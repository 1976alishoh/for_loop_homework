def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    s = 0
    for i in range(0,N):
        if i % 2 ==1:
           s=s+i
    return s
print(main(12))