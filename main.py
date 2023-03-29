# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку,
# если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

# str2 = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
#
#
# def rle(str1):
#     if str1 == "":
#         return "You entered an empty string. Try again,please!"
#     temp = ""
#     temp1 = ""
#     result = ""
#     count = 1
#     for i in range(len(str1) - 1):
#         if str1[i] == str1[i + 1]:
#             count += 1
#             temp = str1[i] + str(count)
#             if i == ((len(str1)) - 2):
#                 result += temp
#         elif str1[i] != str1[i + 1]:
#             if temp == "":
#
#                 temp += str1[i]
#                 result += temp
#                 temp = ""
#             else:
#                 result += temp
#                 count = 1
#                 temp = ""
#         else:
#             temp = str1[i]
#             result += temp
#     if str1[-1] != str1[-2]:
#         temp1 += str1[-1]
#         result += temp1
#     return result
#
#
# print(rle(str2))


# Sample Input
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буква".

# words1 = ["eat", "tea", "tan", "ate", "nat", "bat", "ant"]


