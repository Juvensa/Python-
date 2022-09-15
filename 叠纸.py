# 一张纸的厚度为0.08mm，对折多少次能达到珠峰的高度（8848.13m）
h1 = 0.08 / 1000
h2 = 8848.13

count = 0
for i in range(1,999999):
    a = 2 * h1
    h1 = a
    count += 1
    if a > h2:
        break
print(count)

# while True:
#     h1 *= 2
#     count += 1
#     if h1 > h2:
#         break
# print(count)