line = input().split(chr(92))

line2 = line[-1].split('.')

print(f'File name: {line2[0]}')
print(f'File extension: {line2[1]}')