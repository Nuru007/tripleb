import os
import re

directories = [".", "home"]
for d in directories:
    filepath = os.path.join(d, "index.html")
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r") as f:
        content = f.read()

    # 1. Inject tailwind animations into the config
    config_injection = """
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-15px)' },
                        },
                        zoom: {
                            '0%, 100%': { transform: 'scale(1)' },
                            '50%': { transform: 'scale(1.05)' },
                        }
                    },
                    animation: {
                        float: 'float 4s ease-in-out infinite',
                        zoom: 'zoom 15s ease-in-out infinite',
                    },
"""
    # Insert config_injection right after "extend: {"
    if "keyframes: {" not in content:
        content = content.replace('"extend": {', '"extend": {' + config_injection)
        content = content.replace('extend: {', 'extend: {' + config_injection)

    # 2. Add animate-zoom to the image
    content = content.replace(
        '<img class="w-full h-full object-cover"',
        '<img class="w-full h-full object-cover animate-zoom"'
    )

    # 3. Add animate-float to the other two cards and add delays so they don't animate synchronously
    # The first card has animate-float, the other two don't.
    # The second card starts with '<div class="absolute -right-4 bottom-12 bg-surface-container-lowest'
    # The third card starts with '<div class="absolute left-12 -bottom-6 bg-surface-container-lowest'
    
    # Let's just find the divs and replace them
    content = content.replace(
        '<div class="absolute -left-8 top-1/4 bg-surface-container-lowest p-6 rounded-2xl shadow-[0_12px_40px_0_rgba(21,25,53,0.06)] flex items-center gap-4 animate-float border border-outline-variant/10">',
        '<div class="absolute -left-8 top-1/4 bg-surface-container-lowest p-6 rounded-2xl shadow-[0_12px_40px_0_rgba(21,25,53,0.06)] flex items-center gap-4 animate-float border border-outline-variant/10">'
    )
    
    content = content.replace(
        '<div class="absolute -right-4 bottom-12 bg-surface-container-lowest p-6 rounded-2xl shadow-[0_12px_40px_0_rgba(21,25,53,0.06)] flex items-center gap-4 border border-outline-variant/10">',
        '<div class="absolute -right-4 bottom-12 bg-surface-container-lowest p-6 rounded-2xl shadow-[0_12px_40px_0_rgba(21,25,53,0.06)] flex items-center gap-4 animate-float [animation-delay:1s] border border-outline-variant/10">'
    )
    
    content = content.replace(
        '<div class="absolute left-12 -bottom-6 bg-surface-container-lowest p-6 rounded-2xl shadow-[0_12px_40px_0_rgba(21,25,53,0.06)] flex items-center gap-4 border border-outline-variant/10">',
        '<div class="absolute left-12 -bottom-6 bg-surface-container-lowest p-6 rounded-2xl shadow-[0_12px_40px_0_rgba(21,25,53,0.06)] flex items-center gap-4 animate-float [animation-delay:2s] border border-outline-variant/10">'
    )

    with open(filepath, "w") as f:
        f.write(content)

print("Added animations")
