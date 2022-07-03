import sys
input = sys.stdin.readline

n = int(input())
power_matrix = [list(map(int, input().split())) for _ in range(n)]
team1 = [False for _ in range(n)]
min_diff = 10 ** 10

def team_maker(person, head_count):
  global min_diff
  TO = n / 2
  if head_count == TO:
    team1_power, team2_power = 0, 0
    for i in range(n):
      for j in range(n):
        if team1[i] and team1[j]:
          team1_power += power_matrix[i][j]
        elif not team1[i] and not team1[j]:
          team2_power += power_matrix[i][j]
    diff = abs(team1_power - team2_power)
    min_diff = min(min_diff, diff)
    return
  
  for i in range(person, n):
    if team1[i] == False:
      team1[i] = True
      team_maker(person+1, head_count+1)
      team1[i] = False

team_maker(0, 0)
print(min_diff)
