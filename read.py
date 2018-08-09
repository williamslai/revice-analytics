data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) # 把line加到data裡面
		count += 1 #count一直加1
		if count % 1000 == 0:  # %是用來求餘數。
		    print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #總長

print('平均長度等於', sum_len/len(data)) #全部長度➗幾筆data


#篩選，留言長度少於100個字的
#data，是全部的留言，裝著一百萬筆的清單。)
#每一個d是一個留言。

new = []
for d in data:  #把清單中的東西一個個拿出來。 
    if len(d) < 100: #if 你的長度小於100
    	new.append(d) #我就把你(d:留言)裝進新清單(new)裡面。
print('一共有', len(new), '筆清單')
