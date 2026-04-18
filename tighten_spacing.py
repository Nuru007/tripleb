import os
import re

def tighten_spacing():
    html_files = ["home/index.html", "index.html", "who_we_are/index.html", "gallery/index.html", "contact_us/index.html"]
    
    for path in html_files:
        if not os.path.exists(path): continue
        with open(path, "r") as f:
            content = f.read()
            
        # Global Section Spacing
        content = content.replace('py-16 md:py-20', 'py-12 md:py-16')
        content = content.replace('py-16 md:px-12', 'py-12 md:px-12')
        content = content.replace('py-16', 'py-12')
        content = content.replace('pt-8 pb-16 md:pt-16 md:pb-24', 'pt-6 pb-10 md:pt-10 md:pb-16')
        
        # Margins & Gaps
        content = content.replace('mb-12', 'mb-8')
        content = content.replace('gap-12', 'gap-8')
        content = content.replace('gap-10', 'gap-8')
        content = content.replace('space-y-8', 'space-y-6')
        content = content.replace('space-y-10', 'space-y-8')
        
        # Card Paddings
        content = content.replace('p-10 rounded-3xl', 'p-8 rounded-[1.5rem]')
        content = content.replace('p-12', 'p-8')
        
        # Icon margins
        content = content.replace('mb-8', 'mb-6')
        
        with open(path, "w") as f:
            f.write(content)
            
tighten_spacing()
print("Spacing tightened globally.")
