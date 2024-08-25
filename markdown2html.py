#!/usr/bin/env python3
import sys
import os
import markdown

# Check if the number of arguments is less than 2
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Assign arguments to variables
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Read the Markdown file
with open(markdown_file, 'r') as file:
    md_content = file.read()

# Convert Markdown content to HTML
html_content = markdown.markdown(md_content)

# Write the HTML content to the output file
with open(output_file, 'w') as file:
    file.write(html_content)

# Exit with status 0 (success)
sys.exit(0)
