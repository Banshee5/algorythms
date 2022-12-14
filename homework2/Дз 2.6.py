def robCircle(nums: List[int]) -> int:
    if len(nums) == 1: # если дом всего один, сразу возвращаем его значение
            return nums[0]
    if len(nums) == 2: # если дома два, возвращаем значение максимального дома
            return max(nums[0], nums[1])

    return max(my_darling(nums[1:]), my_darling(nums[:-1]))


def my_darling(nums: List[int]) -> int:  #каждая ячейка - это максимальная сумма, которую мы можем украсть со всех домов до текущего, включая его
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) # проверяем что больше, значение предыдущей ячейки или текущей + пред-предыдущей

    return dp[-1]


#решаем динамическим программированием
#если у нас первый дом взят, то последний мы взять не можем и если у нас последний взят, то первый мы взять не можем
#сложность O(n)