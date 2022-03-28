# l = list(map(int,input().split(' ')))
# k = int(input())
# terminated = []
# k_temp = k
#
# while True:
#     if k_temp <= len(l):
#         terminated.append(l[k_temp-1])
#         l.remove(l[k_temp-1])
#         k_temp += k
#     else:
#         k_temp += k
#         k_temp -= len(l)
#
