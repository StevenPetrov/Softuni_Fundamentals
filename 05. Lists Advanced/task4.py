l = input().split(' ')
palindrome = input()

pali_list = [x for x in l if x == x[::-1]]

print(pali_list)
print(f"Found palindrome {l.count(palindrome)} times")

