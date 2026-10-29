#!/bin/bash
# Resumable paper downloader: loops over groups 01-20; a group is downloaded once its seed file has not
# changed for 10 minutes and `papers_en.py check` reports "problems 0". Re-running is safe (done items
# are skipped). Stop with: touch /root/.cache/aiug_lit/STOP_PAPERS
# Usage: bash scripts/run_papers_en.sh [rounds]   (default 40 rounds, 3 min apart)
cd "$(dirname "$0")/.." || exit 1
LOG=/root/.cache/aiug_lit/papers_run.log
rounds=${1:-40}
for ((r = 1; r <= rounds; r++)); do
  pending=0
  for g in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20; do
    [ -e /root/.cache/aiug_lit/STOP_PAPERS ] && { echo "STOP file present" >> "$LOG"; exit 0; }
    seed=$(ls scripts/seeds/papers/${g}_*_seed_cn.json 2>/dev/null | head -1)
    if [ -z "$seed" ]; then pending=1; continue; fi
    age=$(( $(date +%s) - $(stat -c %Y "$seed") ))
    if [ "$age" -lt 600 ]; then pending=1; continue; fi
    done_mark=/root/.cache/aiug_lit/papers_done_$g
    if [ -e "$done_mark" ] && [ "$done_mark" -nt "$seed" ]; then continue; fi
    if ! python3 -I scripts/papers_en.py check "$g" 2>&1 | tail -1 | grep -q "problems 0"; then
      echo "$(date -u +%H:%MZ) $g check has problems; skipped" >> "$LOG"; pending=1; continue
    fi
    echo "$(date -u +%H:%MZ) download $g" >> "$LOG"
    python3 -I -u scripts/papers_en.py download "$g" >> "$LOG" 2>&1 && touch "$done_mark"
  done
  [ "$pending" = 0 ] && { echo "$(date -u +%H:%MZ) all groups processed" >> "$LOG"; exit 0; }
  sleep 180
done
