class Solution(object):
    def getDescentPeriods(self, prices):
        smooth_descent = [1] * len(prices)  # создаем массив
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:  # сравниваем
                smooth_descent[i] += smooth_descent[i - 1]  # считаем количество мягких спадов
        return sum(smooth_descent)

#создаем массив, хранящий цену акции
#нулевой элемент мы не можем сравнить, поэтому начинаем с 1
#сложность О(n)