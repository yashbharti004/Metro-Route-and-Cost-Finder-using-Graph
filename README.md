# 🚇 Nagpur Metro Route Finder (Graph + Dijkstra Algorithm)

A Python-based implementation of the Nagpur Metro route system using **Graph Data Structure** and **Dijkstra's Shortest Path Algorithm**.

This project calculates:
- Shortest route between two stations
- Number of stations travelled
- Estimated fare based on distance slabs

---

## 📌 Project Objective

To simulate a real-world metro navigation system using:
- Graph representation (Adjacency List)
- Priority Queue (Min Heap)
- Dijkstra’s Algorithm for shortest path calculation

This project is useful for:
- DSA practice
- Graph implementation understanding
- Interview preparation
- Academic mini-project submission

---

## 🧠 Concepts Used

- Graph Data Structure
- Weighted Undirected Graph
- Dijkstra Algorithm
- Min Heap (heapq)
- Dictionary & Defaultdict
- Path Reconstruction
- Fare Calculation Logic

---

## 🗺️ Metro Route Covered

Stations included:

1. Prajapati Nagar  
2. Vaishnodevi Square  
3. Ambedkar Square  
4. Telephone Exchange  
5. Chitar Oli Chowk  
6. Agrasen Square  
7. Dosar Vaishya Square  
8. Nagpur Railway Station  
9. Cotton Market  
10. Sitabuldi  
11. Jhansi Rani Square  
12. Institution of Engineers  
13. Shankar Nagar Square  
14. LAD Square  
15. Dharampeth College  
16. Subhash Nagar  
17. Rachana Ring Road Junction  
18. Vasudev Nagar  
19. Bansi Nagar  
20. Lokmanya Nagar  

---

## 💰 Cost Calculation Logic

| Stations Travelled | Cost |
|--------------------|------|
| 1 – 3              | ₹10  |
| 4 – 9              | ₹20  |
| 10 – 14            | ₹30  |
| 15+                | ₹35  |

---

## ⚙️ How It Works

1. Graph is created using adjacency list.
2. Each station is connected sequentially.
3. Dijkstra’s algorithm finds the shortest path.
4. Number of stations is calculated.
5. Fare is determined using slab logic.
6. Route and fare are displayed.

---

## ▶️ How to Run

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/nagpur-metro-graph.git
