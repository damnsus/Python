"""
По миру началась пандемия нового вируса, а вы - вирусолог и нужно срочно разработать вакцину от этого вируса. Вы собрали N штаммов этого вируса (строки, содержащие буквы A, C, G, T). Вам нужно найти самую часто встречающуюся подстроку длины M, чтобы на основе этой последовательности разработать вакцину от вируса.
Если будет подходить несколько подстрок с одинаковой частотой встречаемости в штаммах, то нужно вывести ту, которая идёт первой в алфавитном порядке.

Формат ввода:
N M
и после этого N строк произвольной длины, разделенные newline.

Формат вывода:
Строка длины M.
"""

n, m = map(int, input().split())

substrs = {}
for i in range(n):
    word = input()
    for i in range(len(word) - m + 1):
        substr = word[i:i + m]
        if substr in substrs:
            substrs[substr] += 1
        else:
            substrs[substr] = 1
    max_frequency = max(substrs.values())
    most_common_substrs = [sub for sub, freq in substrs.items() if freq == max_frequency]

print(min(most_common_substrs))
