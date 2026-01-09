# Weaver-Game-Solver
An efficient solving algorithm for a Weaver game
# Weaver-Game-Solver | Weaver 游戏自动求解器

An efficient algorithm to automatically solve the Weaver word game by finding the shortest transformation path between two valid four-letter words.

一个高效的算法程序，用于自动求解 Weaver 文字游戏，通过逐步替换单个字母，从起始单词转化为目标单词，找出最短路径。

---

## 📌 Features | 功能特点

- ✅ Fast BFS-based solution | 基于广度优先搜索（BFS）的高效路径查找
- ✅ Supports any valid 4-letter word in the dictionary | 支持任意在词库中的合法四字母单词
- ✅ Automatically avoids redundant paths | 自动规避重复路径
- ✅ Simple CLI interface for user input | 简洁的命令行交互界面
- ✅ Displays solution path and execution time | 输出求解路径与耗时

---

## 🧠 Algorithm Overview | 算法原理概览

This solver uses **Breadth-First Search (BFS)** to explore all possible one-letter transformations level by level.

本程序使用 **广度优先搜索（BFS）** 算法，逐层遍历所有可能的单字母变换路径，直到找到目标单词。

- Each word is treated as a node in a graph.  
  每个单词被视为图中的一个节点。
- An edge exists between two words if they differ by exactly one letter.  
  如果两个单词只有一个字母不同，则它们之间存在一条边。
- The shortest path from the start to end word is traced once the target is found.  
  找到目标单词后，程序会回溯出最短路径。

---

## 🛠 How to Use | 使用方法

### 1. Environment Setup | 环境配置

- Python 3.x required | 需要安装 Python 3.x
- Make sure `wordsLibrary.txt` is in the same folder
  确保 `wordsLibrary.txt` 与主程序在同一目录

### 2. Run the Solver | 运行程序

---

📈 Performance | 性能表现
Uses hash table (dictionary) for O(1) word existence check
使用字典实现 O(1) 单词查找效率

Avoids revisiting explored words to reduce complexity
避免重复访问已遍历的单词，提升效率

BFS ensures the shortest path is always found
BFS 可保证找到最短路径

---

📘 License | 授权许可
This project is licensed under the MIT License.
本项目采用 MIT 开源许可证。

✍️ Author | 作者
Leo Wang
GitHub: LeoWang0814

