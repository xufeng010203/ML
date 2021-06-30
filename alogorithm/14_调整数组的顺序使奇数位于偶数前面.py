''''''



def Reorder(li):
    p1 = 0
    p2 = len(li) - 1

    while p1 < p2:
        if li[p1] % 2 != 0:
            p1 += 1
        elif li[p2] % 2 == 0:
            p2 -=1
        li[p1], li[p2] = li[p2], li[p1]


if __name__ == '__main__':

    li = [1,2,3,4,6,5, 0, -1]
    Reorder(li)
    print(li)