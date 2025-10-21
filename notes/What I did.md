# 学習ログ
# 2025-10-21
## 今日やったこと
- LeetCode3346: 与えられた区間 [L_i, R_i] のうち、同時にカバーされる最大本数を求める
## 解法
1. starts, ends を別配列に分けてソート
2. starts[i] <= ends[j] なら cur++、else cur--
3. max(cur) を取る



# 2025-10-19
## 今日やったこと
- LeetCode1625: 「状態空間探索（BFS/DFS）による文字列変換問題」かつ「辞書順最小化を目的とした探索問題」
- 文字列を操作しながら、BFS／DFSによる状態遷移探索を行う
## 気付き
- visited は set で十分。defaultdict(int) ではなく set が意味的にも高速にも適している。
- 最後に min するより、探索中に ans = min(ans, cur)をした方が良い。
- 加算は % 10 を使う。str(int(n) + a)[-1] でも動きますが計算・文字列化が重い。((int(n) + a) % 10) にしてから chr/str に戻すのが定石。


# 2025-10-18
## 今日やったこと
- LeetCode3397: 「区間ごとに1点を選んで最大数を取る」タイプの区間スケジューリング問題の亜種
- イマイチ直感的に腑に落ちない部分はあるが、実装は難しくない
## 気付き
- 「区間を左端でソート → 取れる最小値で貪欲に詰める」タイプの問題は割と多い

# 2025-10-17
## 今日やったこと
- LeetCode3003: 「k 種類制約付き区間」問題の定番パターン
- とても難しい
## 気付き
- at most k distinct
- one-modification optimization
- greedy + DP + prefix/suffix analysis
- 基準解＋差分最大化
- 以上の複合体らしい。。
- → 以下の問題を順に解くと良いらしい。
- LeetCode 340 – Longest Substring with At Most K Distinct Characters（ウィンドウ基礎）
- LeetCode 159 – At Most Two Distinct（2 種限定の直感磨き）
- LeetCode 1004 – Max Consecutive Ones III（“at most k flips” 型で差分思考練習）

# 2025-10-16
## 今日やったこと
- LeetCode2598: modごとの在庫管理でMEXを貪欲に構築する
## 気付き
- 「値に ±value を足せる」「k ずつずらせる」など、周期性（mod value） が問題の核心。
- 「何をしても剰余は変わらない」ため、各剰余ごとにいくつ要素があるか（count） に集約できる。
- 求めたい値（MEXなど）を順に増やしていき、必要な剰余の在庫があれば消費、なければ終了。

# 2025-10-15
## 今日やったこと
- LeetCode3350: 隣接する増加部分配列（inc + 二分探索）

## 気付き
- inc[i] は「i始点の増加長」にすると判定が楽
- k の下限は 2（自分ルール）
