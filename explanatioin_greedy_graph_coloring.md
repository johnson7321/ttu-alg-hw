#greedy graph coloring的解釋
### **1. 程式碼目標**
這段程式碼使用貪婪演算法為一個無向圖的每個頂點分配顏色，確保相鄰頂點不會有相同的顏色。該演算法能快速解決圖著色問題，但不保證使用最少的顏色。

---

### **2. 關鍵函數與邏輯**

#### **(1) `addEdge` 函數**
```python
def addEdge(adj, v, w):
    adj[v].append(w)
    adj[w].append(v)  # 無向圖，雙向邊
    return adj
```
- **功能**：
  - 建立無向圖，將頂點 \( v \) 和 \( w \) 連接。
- **參數**：
  - `adj`：鄰接列表，儲存圖的結構。
  - `v`、`w`：要連接的兩個頂點。
- **邏輯**：
  - 在鄰接列表中，為 \( v \) 添加鄰接點 \( w \)，同時為 \( w \) 添加鄰接點 \( v \)。
- **例子**：
  - 如果 \( v = 0, w = 1 \)，則結果是：
    ```
    adj = [[1], [0], [], []]  # 頂點 0 與 1 相連
    ```

---

#### **(2) `greedyColoring` 函數**
```python
def greedyColoring(adj, V):
    result = [-1] * V  # 初始化，每個頂點的顏色為 -1
    result[0] = 0  # 第一個頂點分配第一種顏色
    available = [False] * V  # 儲存顏色是否已被相鄰頂點使用

    for u in range(1, V):  # 遍歷剩餘的頂點
        # 標記相鄰頂點的顏色為不可用
        for i in adj[u]:
            if result[i] != -1:  # 如果相鄰頂點已著色
                available[result[i]] = True

        # 找出第一個可用顏色
        cr = 0
        while cr < V:
            if not available[cr]:
                break
            cr += 1

        result[u] = cr  # 為當前頂點分配顏色

        # 重置顏色的可用狀態
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = False

    # 輸出結果
    for u in range(V):
        print("Vertex", u, " --->  Color", result[u])
```

- **功能**：
  - 將顏色分配給所有頂點，保證相鄰頂點顏色不同。
- **邏輯**：
  1. 初始化：
     - 使用 `result` 陣列儲存每個頂點的顏色（初始值為 -1，表示未著色）。
     - 第一個頂點分配第一種顏色 \( 0 \)。
     - 使用 `available` 陣列紀錄顏色是否可用。
  2. 為每個頂點分配顏色：
     - 標記當前頂點的所有相鄰頂點所使用的顏色為「不可用」。
     - 找到第一個可用顏色，並將其分配給當前頂點。
     - 重置顏色的可用狀態，為下一個頂點準備。
  3. 輸出每個頂點的顏色。

---

#### **(3) 主程式**
```python
if __name__ == '__main__':
    g1 = [[] for i in range(5)]
    g1 = addEdge(g1, 0, 1)
    g1 = addEdge(g1, 0, 2)
    g1 = addEdge(g1, 1, 2)
    g1 = addEdge(g1, 1, 3)
    g1 = addEdge(g1, 2, 3)
    g1 = addEdge(g1, 3, 4)
    print("Coloring of graph 1 ")
    greedyColoring(g1, 5)

    g2 = [[] for i in range(5)]
    g2 = addEdge(g2, 0, 1)
    g2 = addEdge(g2, 0, 2)
    g2 = addEdge(g2, 1, 2)
    g2 = addEdge(g2, 1, 4)
    g2 = addEdge(g2, 2, 4)
    g2 = addEdge(g2, 4, 3)
    print("\nColoring of graph 2")
    greedyColoring(g2, 5)
```

- **功能**：
  - 建立兩個測試用的圖，並使用 `greedyColoring` 函數進行著色。
- **邏輯**：
  1. 使用鄰接列表儲存圖的結構。
  2. 呼叫 `addEdge` 函數，建立每個圖的邊。
  3. 呼叫 `greedyColoring` 函數，執行貪婪著色並輸出結果。

---

### **3. 輸出結果解釋**
#### **圖 1 的結構**
```
頂點 0: 與頂點 1, 2 相連
頂點 1: 與頂點 0, 2, 3 相連
頂點 2: 與頂點 0, 1, 3 相連
頂點 3: 與頂點 1, 2, 4 相連
頂點 4: 與頂點 3 相連
```
**結果**：
```
Vertex 0 --->  Color 0
Vertex 1 --->  Color 1
Vertex 2 --->  Color 2
Vertex 3 --->  Color 0
Vertex 4 --->  Color 1
```

#### **圖 2 的結構**
```
頂點 0: 與頂點 1, 2 相連
頂點 1: 與頂點 0, 2, 4 相連
頂點 2: 與頂點 0, 1, 4 相連
頂點 3: 與頂點 4 相連
頂點 4: 與頂點 1, 2, 3 相連
```
**結果**：
```
Vertex 0 --->  Color 0
Vertex 1 --->  Color 1
Vertex 2 --->  Color 2
Vertex 3 --->  Color 0
Vertex 4 --->  Color 3
```

---

### **4. 程式的優缺點**

#### **優點**
1. 演算法簡單，容易實現。
2. 保證相鄰頂點顏色不同。
3. 適合處理大規模圖的快速近似解。

#### **缺點**
1. 不保證使用最少的顏色數量。
2. 演算法結果依賴頂點處理順序，不同順序可能導致不同的著色數量。

---
