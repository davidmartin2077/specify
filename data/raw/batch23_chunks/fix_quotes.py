#!/usr/bin/env python3
"""Find and fix broken quote patterns in Python file."""
filepath = "data/raw/batch23_chunks/generate_review_chunk000.py"
with open(filepath, "r") as f:
    lines = f.readlines()

# Known problematic pattern: ASCII " used around Chinese terms inside Python string literals
# We need to find lines where " appears both as string delimiter and inside the string
# Strategy: for lines with pattern:  "....."..."....."
# Replace the inner " with '

import re

fixes = 0
new_lines = []
for i, line in enumerate(lines):
    stripped = line.rstrip()
    # Count " characters
    dq_count = stripped.count('"')
    if dq_count > 2:
        # Check if this line is a string value containing embedded Chinese-style quotes
        # Look for pattern: starts with spaces, then ", then Chinese text, then ", etc.
        # We want to replace the problematic inner quotes

        # Simple heuristic: replace "XXX" (where XXX is Chinese) inside string values
        # with 'XXX'

        # Match: Chinese_char"Chinese_text"Chinese_char
        # This is " around Chinese terms inside a Python string
        original = stripped
        # Replace sequences where " surrounds non-empty content and is not at the start/end
        # Look for pattern: 汉字"汉字"汉字
        line = re.sub(r'(?<=[一-鿿\w])"([^"]*?)"(?=[一-鿿\w，。；：、\)])', r"'\1'", line)
        if line != original:
            fixes += 1
    new_lines.append(line)

if fixes:
    with open(filepath, "w") as f:
        f.writelines(new_lines)
    print(f"Fixed {fixes} lines.")
else:
    print("No fixes applied with pattern matching.")

# Verify
try:
    compile("".join(new_lines), "verify.py", "exec")
    print("Syntax OK!")
except SyntaxError as e:
    print(f"ERROR at line {e.lineno}: {e.msg}")
    # Show context
    context = new_lines[max(0, e.lineno-3):e.lineno+1]
    for j, cl in enumerate(context):
        print(f"  {e.lineno-3+j+1}: {cl.rstrip()}")
