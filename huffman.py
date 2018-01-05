import heapq

def frequency(file1):
	dicti={}
	for line in file1:

		for i in range(len(line)):
			if not(line[i] in dicti):
				dicti[line[i]]=1
			else:
				dicti[line[i]]+=1
	return (dicti)		

def encode(text):
	exchange=[]
	for sym,freq in text.items():
		exchange.append([freq,[sym,'']])
	heapq.heapify(exchange)	
	while len(exchange)>1:
		left=heapq.heappop(exchange)
		right=heapq.heappop(exchange)
		for element in left[1:]:
			element[1]='0'+element[1]
		for element in right[1:]:
			element[1]='1'+element[1]
		heapq.heappush(exchange,[left[0]+right[0]]+left[1:]+right[1:])	
	exchange=heapq.heappop(exchange)
	return exchange



if __name__ == "__main__":

	filename="hello.txt"
	file=open(filename,'r')


	freq=frequency(file)
	#sorted_dicti=sorted(dicti.items(),key=operator.itemgetter(1))
	print(freq)
	print("...........................")
	encoded=encode(freq)
	
	print(encoded)
	print("...........................")
	print("Symbol \t Frequency \t\t Code")
	for i in encoded[1:]:
		count=freq[i[0]]
		print(repr(i[0])+"\t\t"+str(count)+"\t\t  "+ i[1])

	# fh=open("Compressed.txt","a")

	
	# itemDict = {item[0]: item[1] for item in encoded[1:]}
	# print(itemDict)
		

  

