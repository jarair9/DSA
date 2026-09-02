## Prefix Sum Algorithm – Variants, Python Examples, and Practice Questions

The **prefix sum** (also called cumulative sum) is one of the most fundamental techniques in competitive programming. It allows you to answer range‑sum queries in **O(1)** after an **O(n)** preprocessing.

But the idea can be extended in many ways. Here I list the **most common variants** you’ll encounter, with Python implementations and a practice problem for each.

---

### Variant 1 – Standard 1D Prefix Sum Array
**Idea**: Given an array `arr`, build `pref` where `pref[i] = sum(arr[0..i])`.  
Then sum of subarray `arr[l..r]` = `pref[r] - pref[l-1]` (with `pref[-1]=0`).

```python
def build_prefix(arr):
    pref = [0] * len(arr)
    pref[0] = arr[0]
    for i in range(1, len(arr)):
        pref[i] = pref[i-1] + arr[i]
    return pref

def range_sum(pref, l, r):
    if l == 0:
        return pref[r]
    return pref[r] - pref[l-1]
```

**Practice Question**:  
Given an array of integers, answer multiple queries asking for the sum of elements between indices `l` and `r` (inclusive).  
*Example*: `arr = [1,2,3,4,5]`, query `(1,3)` → `2+3+4=9`.

---

### Variant 2 – 1D Difference Array (for Range Updates)
**Idea**: Instead of prefix sums from the array, we build a **difference array** `diff` such that  
`arr[i] = prefix_sum(diff)[i]`.  
This allows range **add** updates in O(1) and point queries after prefix‑summing `diff`.

```python
def range_add(diff, l, r, val):
    diff[l] += val
    if r+1 < len(diff):
        diff[r+1] -= val

# After all updates, build prefix sum of diff to get final array
def apply_updates(diff):
    arr = [0] * len(diff)
    cur = 0
    for i in range(len(diff)):
        cur += diff[i]
        arr[i] = cur
    return arr
```

**Practice Question**:  
You have an array of zeros of size `n`. Apply `m` operations: add `val` to all elements from index `l` to `r`. After all operations, print the final array.  
*Example*: `n=5`, ops: `(1,3,2)`, `(2,4,3)` → final `[0,2,5,5,3]`.

---

### Variant 3 – 2D Prefix Sum (Submatrix Sum)
**Idea**: For a 2D matrix, build `pref[i][j] = sum of submatrix from (0,0) to (i,j)`.  
Then sum of any submatrix `(r1,c1)` to `(r2,c2)` can be computed in O(1).

```python
def build_2d_prefix(mat):
    rows, cols = len(mat), len(mat[0])
    pref = [[0]*(cols+1) for _ in range(rows+1)]  # 1-indexed for convenience
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            pref[i][j] = (mat[i-1][j-1] 
                          + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1])
    return pref

def submatrix_sum(pref, r1, c1, r2, c2):
    # Convert to 1-indexed inclusive
    return (pref[r2+1][c2+1] - pref[r1][c2+1] 
            - pref[r2+1][c1] + pref[r1][c1])
```

**Practice Question**:  
Given a 2D matrix of integers, answer multiple queries: sum of elements in the rectangle defined by top‑left `(r1,c1)` and bottom‑right `(r2,c2)`.  
*Example*: matrix `[[1,2],[3,4]]`, query `(0,0,1,1)` → `10`.

---

### Variant 4 – Prefix Sum with HashMap (Subarray Sum Equals K)
**Idea**: Maintain the prefix sum while iterating. Use a hash map to store frequencies of prefix sums seen so far. This solves problems like "count subarrays with sum equal to K" in O(n).

```python
def subarray_sum_equals_k(arr, k):
    count = 0
    prefix_sum = 0
    freq = {0: 1}   # empty prefix sum
    for num in arr:
        prefix_sum += num
        # check if (prefix_sum - k) exists
        count += freq.get(prefix_sum - k, 0)
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count
```

**Practice Question**:  
Given an array of integers, count the number of subarrays whose sum equals a given target `k`.  
*Example*: `arr = [1,1,1]`, `k=2` → answer `2` (subarrays `[1,1]` at indices 0‑1 and 1‑2).

---

### Variant 5 – Prefix XOR (or any Associative Operation)
**Idea**: Prefix sums aren’t limited to addition. For any associative operation that has an inverse (like XOR, where `x^x=0`), we can build prefix arrays and answer range queries quickly.

```python
def build_prefix_xor(arr):
    pref = [0] * len(arr)
    pref[0] = arr[0]
    for i in range(1, len(arr)):
        pref[i] = pref[i-1] ^ arr[i]
    return pref

def range_xor(pref, l, r):
    if l == 0:
        return pref[r]
    return pref[r] ^ pref[l-1]
```

**Practice Question**:  
Given an array of integers, answer queries for the XOR of all elements from `l` to `r`.  
*Example*: `arr = [1,2,3,4]`, query `(1,3)` → `2 ^ 3 ^ 4 = 5`.

---

### Variant 6 – Prefix Sum with Modulo (Counting Subarrays Divisible by K)
**Idea**: Use prefix sums modulo `K`. Two prefix sums with the same remainder give a subarray whose sum is divisible by `K`. Count frequency of remainders.

```python
def subarrays_divisible_by_k(arr, k):
    count = 0
    prefix_mod = 0
    freq = {0: 1}
    for num in arr:
        prefix_mod = (prefix_mod + num) % k
        count += freq.get(prefix_mod, 0)
        freq[prefix_mod] = freq.get(prefix_mod, 0) + 1
    return count
```

**Practice Question**:  
Given an array of integers, count the number of contiguous subarrays whose sum is divisible by `K`.  
*Example*: `arr = [4,5,0,-2,-3,1]`, `k=5` → answer `7`.

---

### Variant 7 – Prefix Sum on Trees (Path Sum Queries)
**Idea**: For a rooted tree, define `pref[node] = sum of values on path from root to node`.  
Then sum of values on path from `u` to `v` = `pref[u] + pref[v] - 2*pref[lca] + value[lca]`.  
(Requires LCA preprocessing, but the prefix array is built via DFS.)

```python
# Build prefix sums during DFS
def dfs(node, parent, current_sum):
    pref[node] = current_sum + value[node]
    for child in tree[node]:
        if child != parent:
            dfs(child, node, pref[node])
```

**Practice Question**:  
Given a tree where each node has a weight, answer queries: sum of weights on the path from node `u` to `v`.  
*Example*: weights `[1,2,3]`, edges `(1-2, 1-3)`, query `(2,3)` → `2+1+3=6`.

---

### Variant 8 – Dynamic Prefix Sum (Fenwick Tree / BIT)
**Idea**: When the array is updated frequently (point updates), a Fenwick Tree (Binary Indexed Tree) provides prefix sums and point updates in O(log n). It’s essentially a dynamic version of prefix sum.

```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def update(self, idx, delta):   # 1-indexed
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx
    def query(self, idx):           # prefix sum [1..idx]
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s
```

**Practice Question**:  
Implement a data structure that supports:
- `update(i, val)` – add `val` to element at index `i`
- `query(l, r)` – return sum of elements from `l` to `r`
Both in O(log n).

---

### Variant 9 – Prefix Sum with Coordinate Compression
When the array indices are large but sparse (e.g., only a few updates or queries), compress the coordinates and use a difference map or prefix sums on compressed coordinates. This is often used in sweep‑line algorithms.

**Practice Question**:  
Given a set of intervals `[l, r]` with values, find the maximum overlapping count at any point. (Use difference map with compression.)

---

## Summary Table

| Variant                     | Core Use Case                                         | Time Complexity         |
|-----------------------------|-------------------------------------------------------|-------------------------|
| 1D Prefix Sum               | Static range sum queries                              | O(1) per query          |
| Difference Array            | Range updates, point queries                          | O(1) per update         |
| 2D Prefix Sum               | Static submatrix sum queries                          | O(1) per query          |
| Prefix + HashMap            | Count subarrays with sum = K / divisible by K         | O(n)                    |
| Prefix XOR                  | Range XOR (or other invertible ops)                   | O(1) per query          |
| Prefix on Trees             | Path sum queries on static tree                       | O(log n) with LCA       |
| Fenwick Tree (BIT)          | Dynamic point updates + prefix sums                   | O(log n) per operation  |
| Prefix + Compression        | Sparse intervals / events                             | Depends on compression  |

---

## Final Note

There is **no fixed number** of variants – you can adapt prefix sums to any operation that is associative and invertible, and combine them with other data structures or techniques. The ones listed above cover 90% of competitive programming problems.

For practice, I recommend starting with:
- **LeetCode 560** (Subarray Sum Equals K)
- **LeetCode 303** (Range Sum Query - Immutable)
- **LeetCode 304** (Range Sum Query 2D - Immutable)
- **LeetCode 370** (Range Addition)
- **LeetCode 1248** (Count Number of Nice Subarrays – uses prefix parity)
- **CSES** problems on prefix sums and difference arrays.

Good luck with your learning!