The golden rule of choosing between `while` and `for` isn't about speed—it's about **clarity** and **how you control the iteration**. 

A `for` loop is essentially a specialized `while` loop designed for a specific job: **iterating over a known sequence or range**. 

Here is the exact decision-making framework, directly applied to algorithm problems (and our two-pointer/three-pointer examples).

---

### 1. Use a `for` loop when:
**You know exactly how many times to iterate, or you are processing every element in a fixed collection.**

- The index moves in a **fixed, predictable step** (usually `+1` or `-1`).
- You just need to look at each element once.
- You want to avoid manual incrementing bugs (off-by-one errors).

**Example in Two/Three-Pointer:** 
The **outer loop** that fixes the first element in Three-Sum. We know we must start at index `0` and stop at `len(arr) - 3`. We don't skip around unpredictably.

```python
# Perfect for 'for' - fixed range, predictable step
for i in range(len(nums) - 2):
    # do something with nums[i]
```

**Other classic problems:** 
- Finding the maximum element in an array.
- Counting vowels in a string.
- Iterating over a matrix.

---

### 2. Use a `while` loop when:
**You do NOT know how many iterations remain, OR the step size changes dynamically.**

- The loop must run **until a certain condition is met**, not a specific count.
- The pointer can **jump** (e.g., `left += 5` or `right -= 3`), or might not move at all in some cases.
- You need **multiple independent variables** moving toward each other at different speeds.

**Example in Two/Three-Pointer:** 
The **inner two-pointer scan**. `left` and `right` move based on the sum (`total < target`). Sometimes you skip duplicates (`while left < right and nums[left] == nums[left+1]: left += 1`). The step size is *conditional*, not fixed.

```python
# Perfect for 'while' - condition-based, variable step size
while left < right:
    if nums[left] + nums[right] == target:
        left += 1  # Could jump 1, or jump 5 if skipping duplicates
    elif total < target:
        left += 1
    else:
        right -= 1
```

**Other classic problems:** 
- Binary Search (you cut the range in half each time).
- Merging two sorted lists (pointers move independently).
- Sliding window with a dynamic window size (you shrink or expand based on a condition).

---

### 3. Direct Application to the Code I Gave You

| Loop Type | Where I used it | Why |
| :--- | :--- | :--- |
| **`for` loop** | Outer loop in `three_sum_while` | We explicitly know `i` goes from `0` to `n-2`. It's clean, safe, and we don't accidentally skip incrementing `i`. |
| **`while` loop** | Inner pair search in `three_sum_while` | `left` and `right` move unpredictably. If a sum is too small, `left++`; if too big, `right--`; if we find a match, we move *both*. A `for` loop cannot handle this easily. |
| **`for` loop with inner `while`** | `two_sum_for` function | The outer pointer (`left`) uses `for` because it must visit every index. The inner adjustment (`right`) uses `while` because it needs to "rewind" multiple steps based on the sum. |

---

### 4. The "Mental Shortcut" Checklist

When you read a problem, ask yourself:

1. **"Does my loop variable always increase by exactly 1, every single time?"**
   - **Yes** → Use `for`.
   - **No** (sometimes it jumps, sometimes it stays) → Use `while`.

2. **"Am I iterating over a list/range just to look at the values?"**
   - **Yes** → Use `for` (it's more readable).
   - **No** (I am waiting for a specific state, like `left >= right`) → Use `while`.

3. **"Can this loop run forever if I make a mistake?"**
   - `while` loops are more prone to infinite loops (if you forget `left += 1`). 
   - **Rule of thumb**: Use `for` whenever you possibly can. Only switch to `while` when the iteration logic is too complex for a fixed-step `for` loop.

---

### Summary Table

| Criterion | Choose `for` | Choose `while` |
| :--- | :--- | :--- |
| **Number of iterations** | Known / Fixed (e.g., `n` times) | Unknown / Conditional (e.g., until target found) |
| **Iterator movement** | Fixed step (e.g., `i += 1`) | Variable / Conditional jumps (e.g., skip duplicates) |
| **Number of control variables** | Usually 1 (the index) | Multiple (e.g., `left` AND `right` moving independently) |
| **Risk of infinite loops** | Low | Higher (must manually increment/decrement carefully) |
| **Best used for** | Outer loops, traversing arrays, DP tables | Two-pointers, Binary Search, Sliding Windows, Tree/Graph BFS/DFS |

**Final Pro-Tip:** In competitive programming, prefer `for` for outer structures (clarity) and `while` for inner moving pointers. If you write a `while` loop and find yourself writing `i += 1` at the very bottom of it, ask yourself: *"Could I just use a `for` loop here instead?"* 9 times out of 10, the answer is yes.