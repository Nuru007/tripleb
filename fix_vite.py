import os

def fix_module_script():
    html_files = ["home/index.html", "index.html", "who_we_are/index.html", "gallery/index.html", "contact_us/index.html"]
    
    for path in html_files:
        if not os.path.exists(path): continue
        with open(path, "r") as f:
            content = f.read()
            
        # Add type="module" to main.js
        content = content.replace('<script src="/main.js"></script>', '<script type="module" src="/main.js"></script>')
        
        with open(path, "w") as f:
            f.write(content)
            
fix_module_script()
print("Fixed script tags.")
