from typing import List

def max_adjacent_increasing(nums: List[int]) -> int:
    n = len(nums)
    # k >= 2 を前提にする
    if n < 4:
        return 0

    inc = [1] * n  # inc[i] = i から始まる厳密増加の長さ
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            inc[i] = inc[i + 1] + 1

    def ok(k: int) -> bool:
        limit = n - 2 * k
        if limit < 0:
            return False
        for a in range(limit + 1):
            if inc[a] >= k and inc[a + k] >= k:
                return True
        return False

    # ★ 下限を 2 に変更
    lo, hi, ans = 2, n // 2, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

if __name__ == "__main__":
    print(max_adjacent_increasing([2,5,7,8,9,2,3,4,3,1]))  # 3
