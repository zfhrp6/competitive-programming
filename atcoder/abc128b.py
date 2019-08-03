n = int(input())
city_score = {}
for i in range(n):
    city, score = input().split()
    city_score[city] = city_score.get(city, []) + [(int(score), i)]

for city in sorted(city_score.keys()):
  for score in sorted(city_score[city], reverse=True):
    print(score[1]+1)
