'''

归并排序
：分治
       84571362
   8457        1362
   84 57       13 62
 8 4  5 7     1 3  6  2

48 57   13  62
4578   1236
12345678
'''

def merge(left, right):
    """
    合并两个有序数组
    :param left: arr
    :param right: arr
    :return:
    """

    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    #如果左边的值都比右边的小，执行循环后，result就是left,然后要把右边right 和result相加
    #同理右边的值都比左边的小，
    result += left[l:]
    result += right[r:]
    return result


def merge_sort(li):
    if len(li) <= 1:
        return li
    #二分分解
    num = len(li) // 2
    left = merge_sort(li[:num])
    right = merge_sort(li[num:])
    return merge(left, right)



alist = [54,26,93,17,77,31,44,55,20]
sorted_alist = merge_sort(alist)
print(sorted_alist)

