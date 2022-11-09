def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    l = []
    for i in list1:
        l.append(i.capitalize())
    return l
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))