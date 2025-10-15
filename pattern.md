# プロコン パターン帳（共通メモ）

## 単調性 × 二分探索
- 判定関数 ok(k) が単調（True→False）なら境界を二分探索
- 例: 隣接する2本の増加部分配列の最大長（LeetCode）

## 2-pointer / 累積 / DP / ヒープ探索 …（ここに追記）
---

## 付記：隣接する2本の増加部分配列（最大 k）
- 前計算：`inc[i] = i から始まる厳密増加の長さ`（右→左）
- 判定 `ok(k)`：ある `a ∈ [0, n-2k]` で `inc[a] >= k` かつ `inc[a+k] >= k`
- 二分探索で最大 k（**今回の実装では k の下限を 2** とした）
- 参照：`problems/leetcode/adjacent-increasing-two-blocks/README.md`

**注意**  
- 厳密増加は `<` 比較。  
- 上限は `k ≤ n//2`。  
- off-by-one：`a` の上限は `n - 2k`。  
- `n < 4` のときは 2 本の長さ2が置けないので 0。
---

## 付記：隣接する2本の増加部分配列（最大 k）
- 前計算：`inc[i] = i から始まる厳密増加の長さ`（右→左）
- 判定 `ok(k)`：ある `a ∈ [0, n-2k]` で `inc[a] >= k` かつ `inc[a+k] >= k`
- 二分探索で最大 k（**今回の実装では k の下限を 2** とした）
- 参照：`problems/leetcode/adjacent-increasing-two-blocks/README.md`

**注意**  
- 厳密増加は `<` 比較。  
- 上限は `k ≤ n//2`。  
- off-by-one：`a` の上限は `n - 2k`。  
- `n < 4` のときは 2 本の長さ2が置けないので 0。
