scores = [80, 90, 70]

# 平均
print(sum(scores)/len(scores))

# 最大値
print(max(scores))

# 60以上だけ表示
for s in scores:
    if s >= 60:
        print(s)