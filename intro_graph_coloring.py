V = 4  # 圖的頂點數量

def print_solution(color):
    # 打印顏色分配結果
    print("Solution Exists: Following are the assigned colors")
    print(" ".join(map(str, color)))

def is_safe(v, graph, color, c):
    # 檢查是否可以將顏色 'c' 分配給頂點 'v'
    for i in range(V):
        if graph[v][i] and c == color[i]:  # 如果頂點 v 與 i 相鄰，且顏色 c 已被使用
            return False
    return True  # 如果顏色 c 是安全的，返回 True

def graph_coloring_util(graph, m, color, v):
    # 基本情況：如果所有頂點都已分配顏色，返回 True
    if v == V:
        return True

    # 嘗試為當前頂點 'v' 分配不同的顏色
    for c in range(1, m + 1):
        # 檢查將顏色 'c' 分配給頂點 'v' 是否符合條件
        if is_safe(v, graph, color, c):
            color[v] = c  # 為頂點分配顏色

            # 遞迴分配顏色給剩餘的頂點
            if graph_coloring_util(graph, m, color, v + 1):
                return True

            # 如果顏色 'c' 的分配無法導致解決方案，回溯取消分配
            color[v] = 0

    # 如果無法為該頂點分配任何顏色，返回 False
    return False

def graph_coloring(graph, m):
    color = [0] * V  # 初始化顏色分配陣列，所有頂點的顏色設為 0（未分配）

    # 呼叫 graph_coloring_util()，從頂點 0 開始分配顏色
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")  # 如果無法找到解決方案，打印「無解」
        return False

    # 打印成功的顏色分配結果
    print_solution(color)
    return True

# 主程式
if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],  # 頂點 0 與頂點 1、2、3 相連
        [1, 0, 1, 0],  # 頂點 1 與頂點 0、2 相連
        [1, 1, 0, 1],  # 頂點 2 與頂點 0、1、3 相連
        [1, 0, 1, 0],  # 頂點 3 與頂點 0、2 相連
    ]

    m = 3  # 設定最多可使用的顏色數量為 3

    # 呼叫主函數進行圖著色
    graph_coloring(graph, m)
    
    # 此程式由 Raja Ramakrishna 提供
