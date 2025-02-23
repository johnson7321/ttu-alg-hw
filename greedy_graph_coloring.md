## **Graph Coloring Using Greedy Algorithm**

### **1. 概述**
- **目標**：為圖的頂點分配顏色，確保相鄰頂點的顏色不同。
- **問題性質**：
  - 著色問題是一個 **NP-complete問題**，因此無法使用高效演算法保證找到最小顏色數量的解。
  - 貪婪演算法提供近似解，**不保證最少顏色**，但顏色數量不會超過 \( d+1 \)，其中 \( d \) 是圖中頂點的最大度數。

---

### **2. 演算法邏輯**
1. **初始步驟**：
   - 為第一個頂點分配第一種顏色。
2. **後續頂點著色**：
   - 遍歷剩餘的頂點：
     1. 檢查當前頂點的所有相鄰頂點，標記它們已使用的顏色。
     2. 為當前頂點分配一個最小的可用顏色。
     3. 如果所有相鄰頂點的顏色都已使用，則為當前頂點分配一種新的顏色。

---

### **3. 關鍵特性**
- **保證的顏色上限**：最多使用 \( d+1 \) 種顏色。
  - 因為一個頂點的相鄰頂點最多有 \( d \) 種顏色，當前頂點可以使用第 \( d+1 \) 種顏色。
- **不保證最少顏色**：
  - 演算法結果依賴於頂點處理順序，不同的順序可能導致不同的顏色數量。
- **時間複雜度**：\( O(V^2 + E) \)
  - \( V \) 是頂點數量，\( E \) 是邊數。

---

### **4. 演算法分析**
- **優點**：
  - 實現簡單，計算速度快。
  - 適合處理大規模圖的近似解。
- **缺點**：
  - 不保證使用最少顏色。
  - 順序依賴性強，頂點順序不同可能產生不同的結果。

---

### **5. 與其他方法的比較**
1. **Welsh–Powell Algorithm**：
   - 改進貪婪演算法的一種方式。
   - 將頂點按度數遞減排序，先處理度數最高的頂點。
   - 通常能有效減少所需顏色數量。
2. **其他演算法**：
   - 動態規劃、啟發式方法等，也能用於圖著色問題，但計算成本較高。

---

### **6. 實例與結果**
- **圖 1**：
  - 著色結果：使用 3 種顏色。
  - 頂點與顏色對應：
    ```
    頂點 0 -> 顏色 0
    頂點 1 -> 顏色 1
    頂點 2 -> 顏色 2
    頂點 3 -> 顏色 0
    頂點 4 -> 顏色 1
    ```
- **圖 2**：
  - 著色結果：使用 4 種顏色。
  - 頂點與顏色對應：
    ```
    頂點 0 -> 顏色 0
    頂點 1 -> 顏色 1
    頂點 2 -> 顏色 2
    頂點 3 -> 顏色 0
    頂點 4 -> 顏色 3
    ```

---

### **7. 演算法的關鍵限制**
1. **頂點順序的影響**：
   - 頂點處理順序可能導致顏色數量的增加或減少。
   - 例如，將圖中的頂點重新排序後，可能需要更多顏色來完成著色。
2. **改善方法**：
   - 使用 Welsh–Powell 或其他排序策略，優化著色結果。

---

### **8. 理論支持**
- 保證顏色上限的數學證明：
  - 若某頂點的相鄰頂點最多有 \( d \) 個，則至多需要 \( d+1 \) 種顏色，因為總有一種顏色未被使用。
  - 可以使用數學歸納法證明這一結論。

---

### **9. 常見應用**
1. **時間表設計**：
   - 為課程或會議安排時間，確保無衝突。
2. **地圖著色**：
   - 為地圖中的地區著色，保證相鄰地區顏色不同。
3. **編譯器寄存器分配**：
   - 為變量分配寄存器，避免同時使用的變量佔用相同寄存器。

---
