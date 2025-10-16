# 二分探索（Binary Search）— 判定関数 / 境界探索 まとめ

二分探索は「**単調に変化する条件**の境界を探す」道具。  
最重要は **判定関数 `ok(x)` を作る** → **範囲 [L, R]** を決める → **更新方向の一貫性**。

---

## 1. いつ使う？
- 答えが **最大/最小の整数**で、`ok(k)` が単調（例：True → Falseに一方向へ壊れる）
- **実数の近似**（誤差 ε まで絞る）
- **配列の境界位置**（Lower/Upper Bound）

---

## 2. 整数版テンプレ（最大値探索）
```python
def binary_search_max(L, R, ok):
    lo, hi = L, R
    ans = L - 1  # 見つからなければ L-1 が返る
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):         # 成立 → 右へ寄せる（大きくできる）
            ans = mid
            lo = mid + 1
        else:               # 不成立 → 左へ寄せる（小さくする）
            hi = mid - 1
    return ans
```

## 3. 実数版テンプレ（誤差 ε で収束）
```python
def binary_search_real(L, R, ok, eps=1e-9):
    lo, hi = L, R
    for _ in range(100):  # 収束回数は問題のスケール次第
        mid = (lo + hi) / 2
        if ok(mid):       # 成立 → 右へ（最大化）
            lo = mid
        else:             # 不成立 → 左へ
            hi = mid
    return lo  # or hi
```

## 4. bisect（境界位置）での典型
```python
import bisect

# a の中で値 x の「挿入位置（左端）」 = Lower Bound
i = bisect.bisect_left(a, x)

# 右端 = Upper Bound
j = bisect.bisect_right(a, x)

# a に x が存在するか
exists = (i < len(a) and a[i] == x)
count  = j - i
```

## 5. 設計チェックリスト
- ok(x) は 単調か？（x を増やすと成立→不成立 or その逆の片側に揃う）
- **探索範囲 [L, R] が“あり得る全域”**か？（今回: L=2, R=n//2 など）
- 更新方向が一貫しているか？（最大化なら成立→右へ）
- 返す値は ans？ hi？ lo？（テンプレに合わせる）
- 端ケース（空配列、最小サイズ、オーバーフロー/浮動誤差）



## 6. ケーススタディ：隣接する増加部分列の最大 k
- LeetCode3350
【問題要約】
長さ k の 厳密増加な部分配列が 隣り合って 2 本（[a..a+k-1], [a+k..a+2k-1]）存在する最大 k を求める。
【キーアイデア】
右→左に前計算：
inc[i] = i から始まる厳密増加の長さ（nums[i] < nums[i+1] なら inc[i]=inc[i+1]+1）
【判定 ok(k)】
a ∈ [0, n-2k] に対し inc[a] ≥ k かつ inc[a+k] ≥ k を満たす a が存在するか
【探索範囲】
k ∈ [2, n//2]（2 本並べるには 2k ≤ n が必要。運用ルールとして k>=2）
【計算量】
前計算 O(n) ＋ 判定 O(n) × 二分探索 O(log n) ⇒ O(n log n)
【よくある落とし穴】
厳密増加なのに <= を使ってしまう（正しくは <）
a の上限は n - 2k（a + 2k - 1 < n の変形）
n < 4 だと k=2 を2本置けない → 0 を返す
k の下限運用（今回のリポでは 2 とした）