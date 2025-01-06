#intro graph coloring的解釋
### **1. 問題背景**
- **M-著色問題**：
  - 為圖中的每個頂點分配顏色，確保相鄰的頂點顏色不同。
  - 限制：最多使用 \( m \) 種顏色。
- **程式目標**：
  - 將顏色分配給圖中的所有頂點，滿足上述條件。
  - 如果有解，則輸出顏色分配結果；否則，顯示「無解」。

---

### **2. 程式的主要邏輯與功能**

#### **(1) `print_solution` 函數**
```python
def print_solution(color):
    print("Solution Exists: Following are the assigned colors")
    print(" ".join(map(str, color)))
```
- **功能**：
  - 輸出頂點的顏色分配結果。
- **參數**：
  - `color`：儲存每個頂點的顏色分配。
- **邏輯**：
  - 將 `color` 陣列轉換為字串形式，逐一打印。

---

#### **(2) `is_safe` 函數**
```python
def is_safe(v, graph, color, c):
    for i in range(V):
        if graph[v][i] and c == color[i]:
            return False
    return True
```
- **功能**：
  - 檢查是否可以為頂點 \( v \) 分配顏色 \( c \)。
- **參數**：
  - `v`：當前頂點。
  - `graph`：圖的鄰接矩陣。
  - `color`：當前的顏色分配。
  - `c`：要分配的顏色。
- **邏輯**：
  - 遍歷頂點 \( v \) 的所有鄰接頂點（從鄰接矩陣中找出）。
  - 如果鄰接頂點已分配顏色 \( c \)，則返回 `False`，否則返回 `True`。

---

#### **(3) `graph_coloring_util` 函數**
```python
def graph_coloring_util(graph, m, color, v):
    if v == V:  # 基本情況：所有頂點都已分配顏色
        return True

    for c in range(1, m + 1):  # 嘗試每一種顏色
        if is_safe(v, graph, color, c):  # 如果顏色 c 對頂點 v 是安全的
            color[v] = c  # 分配顏色

            if graph_coloring_util(graph, m, color, v + 1):  # 遞迴處理下一個頂點
                return True

            color[v] = 0  # 回溯：取消當前的顏色分配

    return False  # 如果無法分配顏色，返回 False
```
- **功能**：
  - 使用回溯法嘗試為所有頂點分配顏色。
- **參數**：
  - `graph`：圖的鄰接矩陣。
  - `m`：最多允許使用的顏色數量。
  - `color`：儲存當前的顏色分配。
  - `v`：當前處理的頂點索引。
- **邏輯**：
  1. **基本情況**：如果所有頂點都已分配顏色，返回 `True`。
  2. **嘗試顏色**：
     - 為當前頂點 \( v \) 嘗試每一種顏色 \( c \)。
     - 如果顏色安全（使用 `is_safe` 函數檢查），將其分配給頂點 \( v \) 並遞迴處理下一個頂點。
     - 如果後續步驟無解，則回溯（取消顏色分配）。
  3. 如果所有顏色都不適合，返回 `False`。

---

#### **(4) `graph_coloring` 函數**
```python
def graph_coloring(graph, m):
    color = [0] * V  # 初始化顏色分配陣列，所有頂點均未著色

    if not graph_coloring_util(graph, m, color, 0):  # 從頂點 0 開始著色
        print("Solution does not exist")
        return False

    print_solution(color)  # 打印成功的顏色分配
    return True
```
- **功能**：
  - 檢查是否存在一個合法的顏色分配，並輸出結果。
- **邏輯**：
  1. 初始化顏色分配陣列。
  2. 呼叫遞迴函數 `graph_coloring_util`，嘗試從頂點 0 開始分配顏色。
  3. 如果無解，打印「無解」；如果有解，打印顏色分配結果。

---

#### **(5) 主程式**
```python
if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]

    m = 3  # 顏色數量限制為 3

    graph_coloring(graph, m)  # 呼叫主函數
```
- **功能**：
  - 定義一個測試圖，並執行 M-著色問題的解法。
- **邏輯**：
  1. 定義圖的鄰接矩陣：
     ```
     0 -- 1
     | \  |
     2 -- 3
     ```
  2. 設定顏色數量限制為 3。
  3. 呼叫 `graph_coloring` 函數進行著色，並輸出結果。

---

### **3. 程式輸出**
對於輸入圖，程式輸出的結果是：
```
Solution Exists: Following are the assigned colors
1 2 3 2
```
- **解釋**：
  - 頂點 0 分配顏色 1。
  - 頂點 1 分配顏色 2。
  - 頂點 2 分配顏色 3。
  - 頂點 3 分配顏色 2。
- 這是一個合法的顏色分配，相鄰頂點顏色不同，且顏色數量不超過 3。

---

### **4. 總結**
- **關鍵邏輯**：
  - 使用回溯法遞迴嘗試顏色分配。
  - 檢查顏色分配是否安全。
  - 如果某一步無解，則回溯重新嘗試。
- **優點**：
  - 可以解決圖著色問題，保證找到合法解（如果存在）。
- **缺點**：
  - 回溯法的效率低，對於大圖可能需要很長時間。