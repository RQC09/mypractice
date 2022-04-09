#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# print(0.1 + 0.2)
#
# #统计列表中的偶数的两种方式
# #1
# numbers = [1, 2, 4, 5, 7]
# count = 0
# for i in numbers:
#     if i % 2 == 0:
#         count += 1
# print(count)
# #2
# print(sum(i % 2 != 0 for i in numbers))
#
# s= "Hello, world!"
# for c in s:
#     print(c)
# print(s[1:3])
# #反转字符串
# print(s[::-1])

#f-string格式
# username,score='aa',100
# print(f'Welcome {username},your score is {score:d}')
#
# words = ['Number(1-10):']
# for i in range(10):
#     words.append(f"Value:{i+1}")
# print(words)
# print('\n'.join(words))

#统计列表中单词数量，保存为字典并排序
l=['aa','ab','ac','bb','ab','ac','ac']
result_dict={}
for i in l:
    if i not in result_dict:
        result_dict[i]=1
    else:
        result_dict[i]+=1
#sorted排序函数：https://blog.csdn.net/gymaisyl/article/details/83039279
result_dict=sorted(result_dict.items(),key=lambda d:d[1],reverse=True)
print(result_dict)
