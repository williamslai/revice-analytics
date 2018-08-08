data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) # 把line加到data裡面
		count += 1 #count一直加1
		if count % 1000 == 0:  # %是用來求餘數。
		    print(len(data))
print(len(data))

#print(data) 全印出來。
print(data[0]) #只印出第一筆。
print('----------------')
print(data[1]) #只印出第二筆。