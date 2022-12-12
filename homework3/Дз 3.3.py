#в дереве нужно найти среднее арифмитическое на каждой глубине и вывести их списки
#Сложность O(N)
class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: #если "дают" не корень
            return []

        stack = [root]
        res = [] #пустой список, куда мы будем записывать
        while len(stack) > 0: #пока длина больше нуля, выполняется условие
            values = []
            res1 = []
            for score in stack:
                if score:
                    values.append(score.val) #стандартные условия дерева
                if score.left:
                    res1.append(score.left)
                if score.right:
                    res1.append(score.right)

            if len(values) > 0:
                res.append(sum(values) * 1.0 / len(values)) #среднее арифмитическое детей
            res = res1

        return res