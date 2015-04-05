#!/usr/bin/env bash
set -e
set -u

for i in {1..3}; do

  output_file="/tmp/output${i}.txt"

  # Generate output from your program
  python set.py < "testcases/input${i}.txt" > "$output_file"

  # Diff that output with the expected output; this should be empty
  echo "Test case ${i}:"
  diff "$output_file" "testcases/output${i}.txt"
  echo

done
