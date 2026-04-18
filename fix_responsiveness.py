import os
import re

html_files = [
    "index.html",
    "home/index.html",
    "who_we_are/index.html",
    "gallery/index.html",
    "contact_us/index.html"
]

def process_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r") as f:
        content = f.read()

    # 1. Padding Fixes
    # Only replace px-12 if it doesn't already have md:px-12, but we can just use regex to replace standalone px-12, or just replace px-12 entirely and clean up duplicates
    # Let's replace 'px-12 ' with 'px-6 md:px-12 '
    content = content.replace('px-12', 'px-6 md:px-12')
    # Clean up any potential 'md:px-6 md:px-12' or 'px-6 md:px-6 md:px-12' mess:
    content = content.replace('px-6 md:px-6 md:px-12', 'px-6 md:px-12')
    content = content.replace('md:px-6 md:px-12', 'px-6 md:px-12')
    # Let's clean up any double classes just in case
    content = content.replace('px-6 md:px-12 md:px-12', 'px-6 md:px-12')
    
    # Same for p-10 md:p-16
    content = content.replace('p-10 md:p-16', 'p-6 md:p-10 lg:p-16')
    content = content.replace('p-10', 'p-6 md:p-10') # for form container

    # 2. Typography Fixes
    # Contact Us specific (and any other 6xl md:8xl)
    content = content.replace('text-6xl md:text-8xl', 'text-5xl md:text-8xl break-words')
    # index.html
    content = content.replace('text-5xl md:text-7xl', 'text-4xl md:text-7xl break-words')
    # Other raw text-7xl or text-6xl without md:
    content = re.sub(r'\btext-7xl\b', 'text-5xl md:text-7xl break-words', content)
    content = re.sub(r'\btext-6xl\b', 'text-4xl md:text-6xl break-words', content)

    # Clean up double break-words
    content = content.replace('break-words break-words', 'break-words')

    # 3. Layout & Button Sizing Fixes
    # Contact Us submit button
    content = content.replace('px-10 py-5 rounded-full', 'w-full md:w-auto px-10 py-5 rounded-full')
    content = content.replace('px-8 py-3 rounded-full', 'w-full md:w-auto px-8 py-3 rounded-full')
    
    # Image grid in who_we_are
    content = content.replace('grid-cols-2 gap-4', 'grid-cols-1 sm:grid-cols-2 gap-4')

    with open(path, "w") as f:
        f.write(content)

for f in html_files:
    process_file(f)
print("Responsive fixes applied.")
