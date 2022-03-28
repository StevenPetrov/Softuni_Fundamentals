# teamA = ['A-1','A-2','A-3','A-4','A-5','A-6','A-7','A-8','A-9','A-10','A-11']
# teamB = ['B-1','B-2','B-3','B-4','B-5','B-6','B-7','B-8','B-9','B-10','B-11']
#
# info = input().split(' ')
# for x in info:
#     if x in teamA:
#         teamA.remove(x)
#     elif x in teamB:
#         teamB.remove(x)
#
# print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")
# if len(teamA) < 7 or len(teamB) < 7:
#     print("Game was terminated")

info = input().split(' ')
players_kicked = []
playersA = 11
playersB = 11
condition = False
for x in info:
    if x not in players_kicked:
        players_kicked.append(x)
        if 'A' in x :
            playersA -= 1
        else:
            playersB -= 1
        if playersA < 7 or playersB < 7:
            condition = True
            break

print(f"Team A - {playersA}; Team B - {playersB}")
if condition:
    print("Game was terminated")