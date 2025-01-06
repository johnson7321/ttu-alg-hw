# Python3 程式，實現圖著色問題的貪婪演算法

def addEdge(adj, v, w):
	
	adj[v].append(w)
	
	# 注意：這是一個無向圖
	adj[w].append(v) 
	return adj

# 為所有頂點分配顏色（從 0 開始），並打印顏色分配結果
def greedyColoring(adj, V):
	
	result = [-1] * V  # 初始化，每個頂點的顏色設為 -1（未著色）

	# 為第一個頂點分配第一種顏色
	result[0] = 0;

	# 暫時陣列，用於儲存可用顏色。
	# 如果 available[cr] 的值為 True，表示顏色 cr 已被其相鄰頂點分配
	available = [False] * V

	# 為剩餘的 V-1 個頂點分配顏色
	for u in range(1, V):
		
		# 處理所有相鄰頂點，將它們使用的顏色標記為不可用
		for i in adj[u]:
			if (result[i] != -1):  # 如果相鄰頂點已被著色
				available[result[i]] = True

		# 找到第一個可用的顏色
		cr = 0
		while cr < V:
			if (available[cr] == False):  # 如果顏色可用
				break
			cr += 1
			
		# 將找到的顏色分配給當前頂點
		result[u] = cr 

		# 重置可用顏色的標記，為下一次迭代準備
		for i in adj[u]:
			if (result[i] != -1):  # 如果相鄰頂點已被著色
				available[result[i]] = False

	# 打印結果
	for u in range(V):
		print("頂點", u, " ---> 顏色", result[u])

# 主程式
if __name__ == '__main__':
	
	g1 = [[] for i in range(5)]  # 初始化圖 1 的鄰接列表
	g1 = addEdge(g1, 0, 1)
	g1 = addEdge(g1, 0, 2)
	g1 = addEdge(g1, 1, 2)
	g1 = addEdge(g1, 1, 3)
	g1 = addEdge(g1, 2, 3)
	g1 = addEdge(g1, 3, 4)
	print("圖 1 的著色結果")
	greedyColoring(g1, 5)

	g2 = [[] for i in range(5)]  # 初始化圖 2 的鄰接列表
	g2 = addEdge(g2, 0, 1)
	g2 = addEdge(g2, 0, 2)
	g2 = addEdge(g2, 1, 2)
	g2 = addEdge(g2, 1, 4)
	g2 = addEdge(g2, 2, 4)
	g2 = addEdge(g2, 4, 3)
	print("\n圖 2 的著色結果")
	greedyColoring(g2, 5)

# 此程式由 mohit kumar 29 提供
