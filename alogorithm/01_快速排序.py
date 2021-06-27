'''
快速排序：
    选择一个值：
        把比这个值大的放在右侧
        把比这个值小的放在左侧
        递归调用
'''

def quick_sort(arr, start, end):
    """
    一定要有递归终止条件
    :param arr:
    :param start:
    :param end:
    :return:
    """

    if start >= end:
        return
    privot = arr[start]
    low = start
    high = end

    while low < high:
        while low < high and arr[high] >= privot:
            high -= 1
        arr[low] = arr[high]

        while low < high and arr[low] < privot:
            low += 1
        arr[high] = arr[low]
    arr[low] = privot

    quick_sort(arr, start, low - 1)
    quick_sort(arr, low + 1, end)


if __name__ == '__main__':
    l = [6, 5, 4, 3, 2,1]
    quick_sort(l, 0, 5)
    print(l)