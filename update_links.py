import os
import re

directories = [".", "home", "who_we_are", "gallery", "contact_us"]
for d in directories:
    filepath = os.path.join(d, "index.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r") as f:
        content = f.read()
    
    # Use regex to find and replace href="#" for the nav links
    # <a ... href="#" ...>Home</a> -> <a ... href="/" ...>Home</a>
    content = re.sub(r'href="#"([^>]*>Home</a>)', r'href="/"\1', content)
    content = re.sub(r'href="#"([^>]*>Who We Are</a>)', r'href="/who_we_are/"\1', content)
    content = re.sub(r'href="#"([^>]*>Gallery</a>)', r'href="/gallery/"\1', content)
    content = re.sub(r'href="#"([^>]*>Contact Us</a>)', r'href="/contact_us/"\1', content)
    
    with open(filepath, "w") as f:
        f.write(content)
print("Updated all nav links")
