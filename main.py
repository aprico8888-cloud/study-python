scores = [80, 90, 70]

avg = sum(scores)/len(scores)

print("平均:", avg)
print("最大:", max(scores))

for s in scores:
    if s >= avg:
        print("平均以上:", s)