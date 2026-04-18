import os
import re

html_files = [
    "index.html",
    "home/index.html",
    "who_we_are/index.html",
    "gallery/index.html",
    "contact_us/index.html"
]

def add_assets(content):
    if '<link rel="stylesheet" href="/style.css">' not in content:
        content = content.replace("</head>", '    <link rel="stylesheet" href="/style.css">\n</head>')
    if '<script src="/main.js"></script>' not in content:
        content = content.replace("</body>", '    <script src="/main.js"></script>\n</body>')
    return content

def update_logo(content):
    content = content.replace('class="h-12 w-auto object-contain"', 'class="h-16 md:h-20 w-auto object-contain"')
    return content

def fix_routes(content):
    content = content.replace('href="#"', 'href="/contact_us/"') # usually fallback
    # Specifically replacing text buttons, we can just replace their exact strings if we can find them,
    # or just use regex for the href nearest to the text.
    # It's easier to just do text replacements for known broken links.
    # But wait, some buttons are <button> instead of <a>.
    
    # "Join the Movement" -> /contact_us/
    # If it's a <button>, change it to <a href="/contact_us/" class="...">Join the Movement</a>
    # Let's search for buttons first
    content = re.sub(r'<button([^>]*)>(\s*Join the Movement\s*)</button>', r'<a href="/contact_us/"\1>\2</a>', content)
    content = re.sub(r'<button([^>]*)>(\s*Become a Catalyst\s*)</button>', r'<a href="/contact_us/"\1>\2</a>', content)
    content = re.sub(r'<button([^>]*)>(\s*Become a Partner\s*)</button>', r'<a href="/contact_us/"\1>\2</a>', content)
    content = re.sub(r'<button([^>]*)>(\s*Our Story\s*)</button>', r'<a href="/who_we_are/"\1>\2</a>', content)
    
    # Same for <a>
    content = re.sub(r'<a href="[^"]*"([^>]*)>(\s*Join the Movement\s*)</a>', r'<a href="/contact_us/"\1>\2</a>', content)
    content = re.sub(r'<a href="[^"]*"([^>]*)>(\s*Become a Catalyst\s*)</a>', r'<a href="/contact_us/"\1>\2</a>', content)
    content = re.sub(r'<a href="[^"]*"([^>]*)>(\s*Become a Partner\s*)</a>', r'<a href="/contact_us/"\1>\2</a>', content)
    content = re.sub(r'<a href="[^"]*"([^>]*)>(\s*Our Story\s*)</a>', r'<a href="/who_we_are/"\1>\2</a>', content)

    # Support us button in navbar
    content = re.sub(r'<button([^>]*)>(\s*Support Us\s*)</button>', r'<a href="/contact_us/"\1>\2</a>', content)
    
    return content

def add_scroll_reveal(content):
    # Add reveal-on-scroll to <section> elements that don't have it, but wait, some sections are containers.
    # We can just add it to the first child of <section> or to the <section> itself.
    # Using regex to find all <section class="...">
    def replace_section(m):
        cls = m.group(1)
        if "reveal-on-scroll" not in cls:
            return f'<section class="{cls} reveal-on-scroll"' + m.group(2) + '>'
        return m.group(0)
    
    # Wait, some sections have `reveal-on-scroll` added manually below. Let's just add to all sections safely.
    content = re.sub(r'<section class="([^"]*)"([^>]*)>', replace_section, content)
    return content

for path in html_files:
    if not os.path.exists(path):
        continue
    with open(path, "r") as f:
        content = f.read()
    
    content = add_assets(content)
    content = update_logo(content)
    content = fix_routes(content)
    content = add_scroll_reveal(content)
    
    # Specifics for home/index.html and index.html
    if path in ["home/index.html", "index.html"]:
        # Update stats
        # The numbers are wrapped in <span class="block text-4xl ...">
        # Let's replace the exact text content of these spans with stat-counter
        # We need to manually target them or use a smart regex.
        
        # 1. 4+ -> data-target="4" data-suffix="+"
        content = content.replace('<span class="block text-4xl md:text-5xl font-extrabold text-primary mb-2">4+</span>',
                                  '<span class="block text-4xl md:text-5xl font-extrabold text-primary mb-2 stat-counter" data-target="4" data-suffix="+">0</span>')
        # 2. 1000+ -> data-target="1000" data-suffix="+"
        content = content.replace('<span class="block text-4xl md:text-5xl font-extrabold text-secondary mb-2">1000+</span>',
                                  '<span class="block text-4xl md:text-5xl font-extrabold text-secondary mb-2 stat-counter" data-target="1000" data-suffix="+">0</span>')
        # 3. 50+ -> data-target="50" data-suffix="+"
        content = content.replace('<span class="block text-4xl md:text-5xl font-extrabold text-tertiary mb-2">50+</span>',
                                  '<span class="block text-4xl md:text-5xl font-extrabold text-tertiary mb-2 stat-counter" data-target="50" data-suffix="+">0</span>')
                                  
        # Second stats strip
        content = content.replace('<span class="block text-4xl font-extrabold text-primary mb-2">12+</span>',
                                  '<span class="block text-4xl font-extrabold text-primary mb-2 stat-counter" data-target="12" data-suffix="+">0</span>')
        content = content.replace('<span class="block text-4xl font-extrabold text-secondary mb-2">$2.4M</span>',
                                  '<span class="block text-4xl font-extrabold text-secondary mb-2 stat-counter" data-target="2.4" data-prefix="$" data-suffix="M">0</span>')
        content = content.replace('<span class="block text-4xl font-extrabold text-tertiary mb-2">85%</span>',
                                  '<span class="block text-4xl font-extrabold text-tertiary mb-2 stat-counter" data-target="85" data-suffix="%">0</span>')
        content = content.replace('<span class="block text-4xl font-extrabold text-primary mb-2">100+</span>',
                                  '<span class="block text-4xl font-extrabold text-primary mb-2 stat-counter" data-target="100" data-suffix="+">0</span>')

        # Staggered delays on "What We Do" cards
        # We find `<div class="bg-surface-container-low rounded-3xl p-8 hover:bg-surface-container-high transition-colors">`
        # and replace with stagger
        cards = content.split('<div class="bg-surface-container-low rounded-3xl p-8 hover:bg-surface-container-high transition-colors">')
        if len(cards) > 1:
            new_content = cards[0]
            for i in range(1, len(cards)):
                delay = i * 100
                new_content += f'<div class="bg-surface-container-low rounded-3xl p-8 hover:bg-surface-container-high transition-colors reveal-on-scroll" style="transition-delay: {delay}ms;">' + cards[i]
            content = new_content
            
    # Specifics for who_we_are/index.html
    if path == "who_we_are/index.html":
        # Add animate-float to hero image
        content = content.replace('<img class="w-full h-full object-cover"', '<img class="w-full h-full object-cover animate-float"')
        
        # Numbers in who we are
        content = content.replace('<span class="block text-2xl font-bold text-primary">120+</span>',
                                  '<span class="block text-2xl font-bold text-primary stat-counter" data-target="120" data-suffix="+">0</span>')
        content = content.replace('<span class="block text-2xl font-bold text-secondary">1.2M</span>',
                                  '<span class="block text-2xl font-bold text-secondary stat-counter" data-target="1.2" data-suffix="M">0</span>')
        
        # Mission & Vision cards
        # Replace the Mission card classes
        content = content.replace('<!-- Mission Card -->\n<div class="bg-surface-container-low p-12 rounded-3xl relative overflow-hidden group hover:bg-surface-container-high transition-colors duration-500">',
                                  '<!-- Mission Card -->\n<div class="mission-card card-hover-transition p-12 rounded-3xl relative overflow-hidden group duration-500">')
        # Replace the Mission icon container
        content = content.replace('<div class="w-12 h-12 flex items-center justify-center rounded-xl bg-primary text-white mb-8">',
                                  '<div class="icon-container w-12 h-12 flex items-center justify-center rounded-xl mb-8">')
        
        # Replace the Vision card classes
        content = content.replace('<!-- Vision Card -->\n<div class="bg-surface-container-low p-12 rounded-3xl relative overflow-hidden group hover:bg-surface-container-high transition-colors duration-500">',
                                  '<!-- Vision Card -->\n<div class="vision-card card-hover-transition p-12 rounded-3xl relative overflow-hidden group duration-500">')
        # Replace the Vision icon container (only the second one after mission, which we already replaced)
        # We need to make sure we replace the `bg-tertiary text-white`
        content = content.replace('<div class="w-12 h-12 flex items-center justify-center rounded-xl bg-tertiary text-white mb-8">',
                                  '<div class="icon-container w-12 h-12 flex items-center justify-center rounded-xl mb-8">')


    with open(path, "w") as f:
        f.write(content)

print("Applied enhancements to HTML files")
