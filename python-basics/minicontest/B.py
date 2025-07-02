"""
Вы начали использовать код из предыдущей задачи, но наткнулись на определенные проблемы.
Первая из проблем - оказалось, что не все строчки используют символы A, C, G, T - и иногда появляются какие-то другие символы. Такие строчки не надо использовать при поиске нужной подстроки.
Вторая из проблем - оказывается, что нельзя, чтобы код из вашей вакцины встречался в геноме человека, иначе произойдёт что-то плохое. Таким образом, теперь после всех строчек с геномами штаммов вирусов будет подаваться строка с геномом человека, и ответная строка должна не быть подстрокой генома человека.
Если будет подходить несколько подстрок с одинаковой частотой встречаемости в штаммах, то нужно вывести ту, которая идёт первой в алфавитном порядке.

Формат ввода:
N M
N строк геномов штаммов
S - строка генома человека

Формат вывода:
Самая часто встречающаяся подстрока для штаммов
"""

n, m = map(int, input().split())
substrs = {}
for i in range(n):
    word = input()
    if not all(c in 'ACGT' for c in word):
        continue
    for i in range(len(word) - m + 1):
        substr = word[i:i + m]
        if substr in substrs:
            substrs[substr] += 1
        else:
            substrs[substr] = 1
human_genome = input()
valid_substrs = {sub: freq for sub, freq in substrs.items() if sub not in human_genome}
max_frequency = max(valid_substrs.values())
most_common_substrs = [sub for sub, freq in valid_substrs.items() if freq == max_frequency]

print(min(most_common_substrs))

