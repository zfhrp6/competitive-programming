H, W = map(int, input().split())
field = []
for row in range(H):
  line = list(map(int, input().split()))
  field.append(line)

def nearest_odd(point, depth):
  #print('nearest', point, depth)
  for i in range(depth):
    if point[1] + i < H and point[0] + depth - i < W:
      if field[point[1] + i][point[0] + depth - i]%2:
        #print('found', point[1] + i, point[0] + depth - i)
        return (point[1] + i, point[0] + depth - i)
  else:
    return (-1,-1)

def make_swap_ops(p1, p2):
  #print('make', p1, p2)
  ops = []
  height_dist = abs(p1[1]-p2[1])
  width_dist = abs(p1[0]-p2[0])
  for xmove in range(1, width_dist+1):
    #print('xmove',xmove)
    ops.append((p1[0]+xmove-1,p1[1],p1[0]+xmove,p1[1]))
  for ymove in range(1, height_dist+1):
    #print('ymove',ymove)
    ops.append((p1[0]+width_dist,p1[1]+ymove-1,p1[0]+width_dist,p1[1]+ymove))
  return ops



pairs = []
for y in range(H):
  for x in range(W):
    #print('current pos', x,y)
    if field[y][x]%2:
      tmp = (-1,-1)
      for pl in range(1, max(H,W)):
        tmp = nearest_odd((x,y), pl)
        if tmp[0] > -1:
          #print('tmp is tuple', tmp)
          pairs.append(((y,x),tmp))
          field[y][x] += 1
          field[tmp[0]][tmp[1]] += 1
          break
    #print('fie', field)
    #print('pairs', pairs)

ops = []
for pair in pairs:
  ops += make_swap_ops(*pair)
print(len(ops))
for op in ops:
  #print(op)
  print(op[1],op[0],op[3],op[2])
