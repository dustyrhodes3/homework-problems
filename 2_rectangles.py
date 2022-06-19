class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def doOverlap(l1, r1, l2, r2):

    if(l1.x > r2.x or l2.x > r1.x):
        return False

    if(r1.y > l2.y or r2.y > l1.y):
        return False

    return True


if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(0, 10)
    r2 = Point(10, 0)

    if(doOverlap(l1, r1, l2, r2)):
        print("Rectangles Fully Overlap")
    else:
        print("Rectangles Partially Overlap")
