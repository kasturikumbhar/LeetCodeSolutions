

## 📚 **LeetCode Solutions**

---

### **1. DYNAMIC PROGRAMMING** (11 problems) 🔢
**Pattern Recognition:** Look for problems asking "find optimal choice", "max/min value", or "counting ways"

**Problems Covered:**
- `climbing_stairs` - **HINT:** Each step depends only on previous 2 steps → Use 2 variables (space optimized)
- `coin_change` - **HINT:** "Minimum coins" → DP with state = amount, transition = try all coins
- `house_robber` / `house_robber_II` - **HINT:** Adjacent elements can't both be selected → Alternate inclusion/exclusion
- `buy_n_sell_n_cooldown_stock` - **HINT:** State machine with 3 states (hold/sell/cooldown)
- `longest_common_subsequence` - **HINT:** 2D DP grid, characters match → diagonal; don't match → max of adjacent
- `longest_increasing_subsequence` - **HINT:** For each element, find best previous element that's smaller
- `target_sum` - **HINT:** Reframe as partition problem (sum-difference trick)
- `partition_equal_sum` - **HINT:** 0/1 knapsack variant - can we make target sum?
- `unique_paths` - **HINT:** Grid paths = combinations, fill DP row by row

---

### **2. SLIDING WINDOW** (5 problems) 🪟
**Pattern Recognition:** Look for "contiguous substring/subarray" with constraints (unique chars, condition met)

**Problems Covered:**
- `longest_substring_without_repeating_char` - **HINT:** Use set + 2 pointers; shrink window when duplicate found
- `longest_repeating_char_replacement` - **HINT:** Window valid if (max_freq + replacements ≤ window_size)
- `minimum_window_substring` - **HINT:** Expand to get all chars, shrink to minimize; track char frequencies
- `permutations_in_string` - **HINT:** Fixed window size; compare char frequency maps
- **⚠️ Empty folder:** merge-intervals, fast-slow-pointers, two-pointers need solutions

---

### **3. BINARY SEARCH** (5 problems) 🔍
**Pattern Recognition:** Look for "sorted array" + "find target" or "find boundary"

**Problems Covered:**
- `1st_last_position` / `1st_last_position_in_sortedlist` - **HINT:** Binary search twice - first to find leftmost, then rightmost occurrence
- `rotated_sorted_array` - **HINT:** One half is always sorted → Check if target is in sorted half, recurse on other
- `koko_eating_bananas` - **HINT:** Binary search on answer (eating speed) not the array!
- `median_two_sorted_array` - **HINT:** Binary search on partition point; ensure left_max ≤ right_min

---

### **4. TREES** (11 problems) 🌳
**Pattern Recognition:** Recursion + base case = null; think bottom-up vs top-down approach

**Problems Covered:**
- `same_tree` - **HINT:** Both null = True; one null = False; recurse on left & right
- `invert_tree` - **HINT:** Swap children recursively; process current before children (pre-order)
- `balanced_binary_tree` - **HINT:** Height difference ≤ 1 AND both subtrees balanced; return -1 if unbalanced
- `diameter_of_binary_tree` - **HINT:** Max path = left_height + right_height; track global max
- `depth_of_binary_tree` / `min_depth_btree` - **HINT:** Max/Min of (left, right) + 1
- `subtree_of_another_tree` - **HINT:** Serialize trees or compare recursively from each node
- `path_sum_in_bst` - **HINT:** Keep running sum; decrement target as you go down
- `level_order_traversal` - **HINT:** Use queue (BFS); process level by level
- `LCA_in_BST` - **HINT:** In BST, LCA is where path to p & q diverge (use BST property)

---

### **5. GRAPH** (4 problems) 🕸️
**Pattern Recognition:** "Islands", "paths", "cycles" → Use DFS/BFS/Union-Find

**Problems Covered:**
- `number_of_island` - **HINT:** DFS/BFS marking visited; count connected components
- `clone_graph` - **HINT:** HashMap to store node mapping; DFS/BFS to traverse
- `course_schedule` - **HINT:** Detect cycle using DFS (3 colors: white/gray/black)
- `pacific_atlantic` - **HINT:** Reverse: start from edges where water flows OUT; mark reachable cells

---

### **6. GREEDY** (6 problems) ✅
**Pattern Recognition:** "Maximize", "Minimize", "Valid" → Make locally optimal choice that leads to global optimum

**Problems Covered:**
- `jump_game` - **HINT:** Track farthest reachable position; if current index > farthest, return False
- `jump_game_II` - **HINT:** Track range of current jump level; increment jumps when i exceeds range
- `gas_station` - **HINT:** If cumsum < 0 at station i, next possible start is i+1
- `partition_labels` - **HINT:** Track last occurrence; expand window until last char of all included chars
- `merge_triplets` - **HINT:** Greedy selection: pick triplets that don't prevent target
- `valid_paranthesis` - **HINT:** Match closing with nearest opening; stack-based

---

### **7. HEAP** (3 problems) 📦
**Pattern Recognition:** "K-th largest", "median", "top K" → Use heap operations

**Problems Covered:**
- `top_k_frequency` - **HINT:** Count frequencies → Min-heap of size K (evict smallest freq)
- `merge_k_sorted_linked_list` - **HINT:** Min-heap of nodes; pop min, insert its next
- `median_from_data_stream` - **HINT:** Max-heap (left) + Min-heap (right); balance sizes; median from tops

---

### **8. MONOTONIC STACK** (2 problems) 📈
**Pattern Recognition:** "Next/Previous greater/smaller element" OR "Area under histogram"

**Problems Covered:**
- `daily_temperatures` - **HINT:** Stack stores indices; for each temp, pop smaller ones and record distances
- `largest_rectangle_area_in_histogram` - **HINT:** Stack maintains increasing heights; for each bar, extend width until taller bar blocks

---

### **9. BACKTRACKING** (1 problem) 🔄
**Pattern Recognition:** Generate all possibilities; prune invalid states

**Problems Covered:**
- `permutations` - **HINT:** DFS with swap; backtrack by swapping back

---

### **10-12. TODO FOLDERS** 🚀
- **Two-Pointers:** Classic (merge sorted arrays, container with most water)
- **Merge-Intervals:** Interval scheduling problems
- **Fast-Slow-Pointers:** Linked list cycle, finding middle

---

## **🎯 Quick Pattern Lookup Table**

| Pattern | Recognize By | Solution Strategy |
|---------|-------------|------------------|
| **DP** | Optimal substructure, overlapping subproblems | Define state, transition formula |
| **Sliding Window** | Contiguous subarray + condition | 2 pointers, expand/contract window |
| **Binary Search** | Sorted data + find target/boundary | Identify which half to search |
| **Trees** | Recursive structure, null as base case | DFS pre/in/post-order or BFS |
| **Graph** | Connected components, paths, cycles | DFS/BFS, 3-color DFS for cycle |
| **Greedy** | Local choice = global optimal | Prove why greedy works for problem |
| **Heap** | Top K, median, priority ordering | Min/Max heap with size management |
| **Monotonic Stack** | Next/Prev greater/smaller | Maintain order, pop and process |
| **Backtracking** | Generate all possibilities | DFS + undo changes |

---
