import os
import re

directories = [".", "home", "who_we_are", "gallery", "contact_us"]
for d in directories:
    filepath = os.path.join(d, "index.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r") as f:
        content = f.read()
    
    # Replace the header logo with the image
    # We can search for the first occurrence of "The Empathic Curatorial" after "<header"
    header_idx = content.find("<header")
    if header_idx != -1:
        end_header_idx = content.find("</header>", header_idx)
        if end_header_idx != -1:
            header_content = content[header_idx:end_header_idx]
            # Replace the text with the image tag
            new_header_content = re.sub(
                r"The Empathic Curatorial", 
                r'<img src="/tripleb.png" alt="Tripleb Logo" class="h-12 w-auto object-contain">', 
                header_content, 
                count=1, 
                flags=re.IGNORECASE
            )
            content = content[:header_idx] + new_header_content + content[end_header_idx:]

    # Replace all other occurrences with "Tripleb"
    content = re.sub(r"The Empathic Curatorial", "Tripleb", content, flags=re.IGNORECASE)
    
    with open(filepath, "w") as f:
        f.write(content)

print("Updated logo and text references")
