import deque from collections

n = int(input())
map = [[0 for _ in range(n+2)] for _ in range(n+2)]

#make_bomb
for i in range(n+2):
  map[0][i] = -1
  map[n+1][i] = -1
  map[i][0] = -1
  map[i][n+1] = -1

#make_apple
apples = int(input())
for apple in range(apples):
  n, m = map(int, input().split())
  map[n][m] = 1

#game_setting
time = 0
head_position = [1, 1]
whole_body = deque([])
whole_body.appendleft(head_position)
length_of_snake = 1
direction = 'right'
end_time = time

how_many_direction_changes = int(input())

time_to_change, rotation = map(input().split())

while time >= 0:

  # 시간 흐름
  time += 1

  # 방향 전환
  if time == int(time_to_change):
    if rotation == 'D':
      if direction == 'right':
        direction = 'down'
      elif direction == 'down':
        direction = 'left'
      elif direction == 'left':
        direction = 'up'
      else:
        direction = 'right'
      time_to_change, rotation = map(input().split())

    else:
      if direction == 'right':
        direction = 'up'
      elif direction == 'up':
        direction = 'left'
      elif direction == 'left':
        direction = 'down'
      else:
        direction = 'right'
      time_to_change, rotation = map(input().split())

  # 뱀 머리 움직임
  if direction == 'right':
    head_position[1] += 1
  elif direction == 'down':
    head_position[0] += 1
  elif direction == 'left':
    head_position[1] -= 1
  else:
    head_position[0] -= 1

  if map[head_position[0], head_position[1]] == 0:
    whole_body.append(head_position)
    map[head_position[0], head_position[1]] = -1
    gone_body = whole_body.popleft()
    map[gone_body[0], gone_body[1]] = 0
  elif map[head_position[0], head_position[1]] == 1:
    whole_body.append(head_position)
    map[head_position[0], head_position[1]] = -1
  else:
    end_time = time
    break
  
print(res)
