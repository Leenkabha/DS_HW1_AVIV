#!/bin/bash

# Step 1: Compile
echo "🔧 Compiling..."
g++ -std=c++14 -DNDEBUG -Wall -o main.out *.cpp
if [ $? -ne 0 ]; then
  echo "❌ Compilation failed"
  exit 1
fi
echo "✅ Compilation succeeded."

# Step 2: Prepare output directory
mkdir -p student_outputs

# Step 3: Run tests
for infile in dspotify_generated/*.in; do
  base=$(basename "$infile" .in)
  ./main.out < "$infile" > "student_outputs/$base.out"
done
echo "✅ Finished running tests."

# Step 4: Compare outputs
echo "🔍 Comparing outputs..."
pass=0
fail=0
for outfile in dspotify_generated_out/*.out; do
  base=$(basename "$outfile")
  diff -q "student_outputs/$base" "$outfile" > /dev/null
  if [ $? -eq 0 ]; then
    echo "$base ✅"
    ((pass++))
  else
    echo "$base ❌"
    ((fail++))
  fi
done

echo ""
echo "✅ Passed: $pass"
echo "❌ Failed: $fail"
