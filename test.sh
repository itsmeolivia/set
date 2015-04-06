#!/usr/bin/env bash
set -e
set -u

for i in {1..1}; do

  output_file="/tmp/output${i}.txt"

  # Generate output from your program
  python game.py < "testcases/input${i}.txt" > "$output_file"

  # Diff that output with the expected output; this should be empty
  echo "Test case ${i}:"
  diff "$output_file" "testcases/output${i}.txt"
  echo

done
