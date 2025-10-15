
# Two Adjacent Strictly Increasing Subarrays (Max k)

- 前計算: inc[i] = i から始まる厳密増加の長さ
- 判定 ok(k): ある a (0..n-2k) で inc[a] >= k かつ inc[a+k] >= k
- 二分探索で最大 k
- 計算量: O(n log n), 追加メモリ O(n)
