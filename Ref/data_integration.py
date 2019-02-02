
"""
# STAGE 1: sorted

test = []
test2 = []
test3 = []
with open('result.txt','r', encoding="UTF-8") as f2:# 把爬好的raw数据打开
    for each in f2:
        # test.append(each.strip().split(' ')[0].strip('.'))
        # test2.append(' '.join(each.strip().split(' ')[1:]))
        test3.append([int(each.strip().split(' ')[0].strip('.')),' '.join(each.strip().split(' ')[1:])])
        # 因为作者基本会打空格来分开单词，所以用空格来split。
        # 因为数字他都会加个.，所以把点去掉，但是接下来sort后发现有些不是数字开头的，手动取出来放到sorted_0.txt

# print(test3[655])

# for i in test:

test3.sort()

for i in test3:
    with open('sorted_1.txt', 'a', encoding="UTF-8") as f:# 写
        f.write(str(i[0]) + '\t' + i[1] + '\n')

"""

"""
# STAGE 2: set

original = []
cur = []
cur2 = []

with open ('original.txt','r', encoding="UTF-8") as f:# 这是作者之前自己整理出来的
	for each in f:
		original.append(each.strip().split(' ')[1].strip('.'))# 我放到git上前面有| ，所以索引是1

with open ('sorted_1.txt','r', encoding="UTF-8") as f2:# 第一步排好序后的数据
	for each in f2:
		cur.append(each.strip().split('\t')[0])
		cur2.append(' '.join(each.strip().split('\t')[1:]))

new_one = [(x, cur2[cur.index(x)]) for x in cur if x not in original]# 找cur不在original里的

with open('new_one.txt', 'a', encoding="UTF-8") as f3:# 存
	for i in new_one:
		f3.write(i[0] + '\t' + i[1] + '\n')

"""

"""
# STAGE 2: putintogether

# 首先经过一系列简单处理把没出现的和已出现的以md表格形式放一起，数字后去掉点放了个制表符。

cur = []

with open ('new.txt','r', encoding="UTF-8") as f4:# 数字拆出
	for each in f4:
		cur.append((int(each.strip().split('\t')[0].lstrip('| ')), each.strip().split('\t')[1]))

cur.sort()

with open('new_2.txt', 'a', encoding="UTF-8") as f5:# 排序好再拼
	for i in cur:
		f5.write('| ' + str(i[0]) + '. ' + i[1] + '\n')

"""
