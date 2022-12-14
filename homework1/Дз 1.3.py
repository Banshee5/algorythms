# Начинаем сиперебора. Смотрим, является ли камень с драгоценным
# Получается вложенный цикл
# Смотрим каждый камень, сравниваю его с каждым драгоценным. Если есть совпадение,то инкрементируем счетчик.
# Делаем возращение
# сложность O(N^M), (тк есть вложенный цикл)

def numJewelsInStones(jewels, stones):
    score = 0                 # счетчик равен 0
    for i in stones:            # смотрим в камни
        for j in jewels:        # рассматриваем камень, проходим по каждому драгоценному
            if i == j:          # если есть совпадение
                score += 1    # инкрементируем счетчик
    return score             # возвращаем счетчик
print(numJewelsInStones("aA", "aAAbbbb"))