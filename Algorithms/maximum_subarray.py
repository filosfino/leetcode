# -- coding: utf-8 --


def get_max_slice(array):
    """
    假定已知前面的最大序列值, 每引入一个新元素只需要比较新元素对已有最大序列值的影响即可
    """
    assert len(array)

    max_ending_here = max_so_far = array[0]

    for i in array[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def times_3_bitcount(array):

    """
    3(0b11) 的 位移操作必定会得到两个 '1' bit
    因为 array 已经顺序排好, 后一个必定大于前一个,
    如果后一个位移数 = 前一个 + 1, 则会得到 0b11 + 0b110 = 0b1001, 结果仍然为 2 个 '1' bit
    如果后一个位移数 > 前一个 + 1, 则会得到 0b11 + 0b110..0 = 0b11..11, 结果为 4 个 '1' bit
    """
    previous = array[0]
    result = 2

    for current in array[1:]:
        if current == previous + 1:
            pass
        else:
            result += 2
    return result

