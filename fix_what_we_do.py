import os

def fix_cards_and_nav():
    html_files = ["index.html", "home/index.html", "who_we_are/index.html", "gallery/index.html", "contact_us/index.html"]
    
    for path in html_files:
        if not os.path.exists(path):
            continue
            
        with open(path, "r") as f:
            content = f.read()

        # 1. Fix Mobile Navbar Button
        old_nav_btn = 'class="w-full md:w-auto bg-gradient-to-r from-primary to-primary-container text-white px-8 py-3 rounded-full font-bold text-sm tracking-tight hover:opacity-80 transition-opacity active:scale-95 duration-200 ease-in-out"'
        new_nav_btn = 'class="bg-gradient-to-r from-primary to-primary-container text-white px-8 py-3 rounded-full font-bold text-sm tracking-tight hover:opacity-80 transition-opacity active:scale-95 duration-200 ease-in-out"'
        content = content.replace(old_nav_btn, new_nav_btn)
        
        # 2. Fix "What We Do" Cards (only in index and home)
        if "home/" in path or path == "index.html":
            # Add stagger delays to the cards
            # We will find the grid and replace the card divs
            
            # Card 1 (Primary)
            content = content.replace(
                '<div class="group premium-card bg-surface-container-lowest p-8 rounded-[1.5rem] relative overflow-hidden">',
                '<div class="group premium-card bg-gradient-to-br from-primary to-primary/80 p-8 rounded-[1.5rem] relative overflow-hidden hover:scale-[1.02] hover:shadow-xl transition-all duration-300 ease-out" style="transition-delay: 100ms;">', 1
            )
            
            # Card 2 (Secondary)
            content = content.replace(
                '<div class="group premium-card bg-surface-container-lowest p-8 rounded-[1.5rem] relative overflow-hidden">',
                '<div class="group premium-card bg-gradient-to-br from-secondary to-secondary/80 p-8 rounded-[1.5rem] relative overflow-hidden hover:scale-[1.02] hover:shadow-xl transition-all duration-300 ease-out" style="transition-delay: 200ms;">', 1
            )
            
            # Card 3 (Tertiary)
            content = content.replace(
                '<div class="group premium-card bg-surface-container-lowest p-8 rounded-[1.5rem] relative overflow-hidden">',
                '<div class="group premium-card bg-gradient-to-br from-tertiary to-tertiary/80 p-8 rounded-[1.5rem] relative overflow-hidden hover:scale-[1.02] hover:shadow-xl transition-all duration-300 ease-out" style="transition-delay: 300ms;">', 1
            )
            
            # Card 4 (Neutral/Black)
            content = content.replace(
                '<div class="group premium-card bg-surface-container-lowest p-8 rounded-[1.5rem] relative overflow-hidden">',
                '<div class="group premium-card bg-gradient-to-br from-slate-800 to-slate-900 p-8 rounded-[1.5rem] relative overflow-hidden hover:scale-[1.02] hover:shadow-xl transition-all duration-300 ease-out" style="transition-delay: 400ms;">', 1
            )
            
            # Remove old Gradient Overlays
            content = content.replace('<!-- Gradient Overlay -->\n    <div class="absolute inset-0 bg-gradient-to-br from-primary to-primary/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-0"></div>\n', '')
            content = content.replace('<!-- Gradient Overlay -->\n    <div class="absolute inset-0 bg-gradient-to-br from-secondary to-secondary/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-0"></div>\n', '')
            content = content.replace('<!-- Gradient Overlay -->\n    <div class="absolute inset-0 bg-gradient-to-br from-tertiary to-tertiary/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-0"></div>\n', '')
            content = content.replace('<!-- Gradient Overlay -->\n    <div class="absolute inset-0 bg-gradient-to-br from-slate-800 to-slate-900 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-0"></div>\n', '')

            # Fix Text colors to be permanently white, remove group-hover text changes
            content = content.replace('group-hover:text-white transition-colors duration-300', 'text-white')
            content = content.replace('text-on-surface-variant leading-relaxed mb-6 group-hover:text-white/90 transition-colors duration-300', 'text-white/90 leading-relaxed mb-6')
            
            # Fix Icons to be permanently white/glassy
            content = content.replace('w-14 h-14 rounded-2xl bg-primary-fixed flex items-center justify-center text-primary mb-6 transition-all group-hover:scale-110 group-hover:bg-white/20 group-hover:text-white', 'w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-white mb-6')
            content = content.replace('w-14 h-14 rounded-2xl bg-secondary-fixed flex items-center justify-center text-secondary mb-6 transition-all group-hover:scale-110 group-hover:bg-white/20 group-hover:text-white', 'w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-white mb-6')
            content = content.replace('w-14 h-14 rounded-2xl bg-tertiary-fixed flex items-center justify-center text-tertiary mb-6 transition-all group-hover:scale-110 group-hover:bg-white/20 group-hover:text-white', 'w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-white mb-6')
            content = content.replace('w-14 h-14 rounded-2xl bg-slate-100 flex items-center justify-center text-slate-800 mb-6 transition-all group-hover:scale-110 group-hover:bg-white/20 group-hover:text-white', 'w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-white mb-6')

        with open(path, "w") as f:
            f.write(content)

fix_cards_and_nav()
print("Card gradients and nav button fixed!")
