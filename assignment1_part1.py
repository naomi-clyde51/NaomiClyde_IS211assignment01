def listDivide(numbers, divide=2):
    for x in listDivide:
        if x % divide == 0:
            return (listDivide)
        else:
            print(ListDivideException)

class ListDivideException(Exception):
    print ("Cannot be divided by 2.")

def testListDivide():
    """
    Test listDivide
    """
    assert listDivide([1, 2, 3, 4, 5]) == 2
    assert listDivide([2, 4, 6, 8, 10]) == 5
    assert listDivide([30, 54, 63, 98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1, 2, 3, 4, 5], 1) == 5


if __name__ == "__main__":
    testListDivide(listDivide)