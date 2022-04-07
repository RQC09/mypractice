# 变量解包
# 普通解包
username = ["xiaolei", "wanghua"]
author, reader = username
print(author)
print(reader)

# 动态解包
data = ["xl", "apple", "banana", "orange", "wh"]
username, *fruits, reader = data
print(username)
print(fruits)
print(reader)


# 冒泡排序函数（默认偶数比奇数大）
def magic_bubble_sort(numbers):
    """有魔力的冒泡排序算法，默认所有的偶数都比奇数大

    :param numbers:需要排序的列表，函数会直接修改原始列表
    """
    stop_position=len(numbers)-1
    while stop_position>0:
        for i in range(stop_position):
            current,next_=numbers[i], numbers[i+1]
            current_is_even,next_is_even=current%2==0,next_%2==0
            should_swap=False
            #交换位置的两个条件
            # - 前面是偶数，后面是奇数
            # - 前面和后面同为奇数或偶数，但是前面比后面大
            if current_is_even and not next_is_even:
                should_swap=True
            elif current_is_even==next_is_even and current > next_:
                should_swap=True
            if should_swap:
                numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
        stop_position-=1
    return numbers

print(magic_bubble_sort([1,4,7,9]))