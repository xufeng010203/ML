'''

旋转数组
前半部分时递增  后面部分是递增
{3， 4， 5， 1， 2} 是{1， 2，3， 4， 5}的一个旋转数组
输出 数组中最小数字  1
利用 递增特性

'''

def min1(li):
    p1 = 0
    p2 = len(li) - 1


    while p1 < p2:
        mid = (p1 + p2) // 2
        if p2 - p1 == 1:
            return li[p2]
        else:
            if li[mid] >= li[p1]:
                #当中间值大于左边的值时，说明中间值在左边
                p1 = mid
            elif li[mid] < li[p2]:
                ##当中间值小于左边的值时，说明中间值在右边
                p2 = mid
    return li[p2]
print(min1([8,9,1,2,3,4,5]))

