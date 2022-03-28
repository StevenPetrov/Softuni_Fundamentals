# list1 = [3]
# # print(list.count(3))
#
# test = (i for i, value in enumerate(list1) if value == '3')
# print(list(test))


# nums = input().split(' ')
#
# new_list = []
#
# for x in nums:
#     if int(x) > 0:
#         new_list.append(-int(x))
#     else:
#         new_list.append(abs(int(x)))
#
# print(new_list)

nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(' ')))]