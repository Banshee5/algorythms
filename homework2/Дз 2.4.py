class Solution(object):
    def maxProfit(self, prices):

        cur_max = 0       # вводим переменную максимального профита
        for i in range(1, len(prices)):    # проходимся циклом по ценам за акцию с 1 идекса тк нулевой нам не с чем сравнивать
            if prices[i] > prices[i-1]:    # сравниваем цену с предыдущей
                cur_max += prices[i] - prices[i-1]     # увеличиваем переменную максимального профита вычитая стоимость прошлого дня
        return cur_max        # возвращаем переменную

#решаем задачу динамическим программированием
#выполняем итерацию по цене, определяем, больше ли следующий элемент предыдущего
#если больше, то мы можем покупать и продавать акции, если нет, то идем дальше
#когда удовлетворяется условие, мы продолжаем добавлять их разницу в итоговое значение
#сложность О(n)