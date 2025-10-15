
#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: $0 <platform> <slug>"
  echo "Example: $0 leetcode adjacent-increasing-two-blocks"
  exit 1
fi

PLATFORM=$1
SLUG=$2
DIR="problems/${PLATFORM}/${SLUG}"

if [ -d "${DIR}" ]; then
  echo "Directory already exists: ${DIR}"
  exit 1
fi

mkdir -p "${DIR}"

cat > "${DIR}/README.md" <<'MD'
# <TITLE>

## 方針
- （ここに解法の要点）

## 計算量
- 時間：
- 空間：

## 落とし穴
- 
MD

cat > "${DIR}/solution.py" <<'PY'
from typing import List

def solve():
    # TODO: 実装
    pass

if __name__ == "__main__":
    # TODO: 簡易動作確認 or 入力処理
    pass
PY

cat > "${DIR}/test_solution.py" <<'PY'
def test_dummy():
    assert 1 + 1 == 2
PY

echo "Created: ${DIR}"
