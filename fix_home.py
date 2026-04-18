import re

def fix_home():
    with open("home/index.html", "r") as f:
        content = f.read()

    # 1. Update Grid Images
    grid_regex = re.compile(r'<div class="dynamic-grid-item premium-image-hover"><img src="[^"]+" alt="Impact (\d+)"></div>')
    
    def repl_grid(match):
        num = match.group(1)
        return f'<div class="dynamic-grid-item premium-image-hover"><img src="https://picsum.photos/600/600?random={num}" alt="Impact {num}"></div>'
    
    content = grid_regex.sub(repl_grid, content)

    # 2. Update What We Do Cards
    # We will find each card block and rewrite it.
    
    card1_old = r'<div class="group premium-card bg-surface-container-lowest p-10 rounded-3xl hover:bg-primary/5">\s*<div class="w-14 h-14 rounded-2xl bg-primary-fixed flex items-center justify-center text-primary mb-8 transition-transform group-hover:scale-110">\s*<span class="material-symbols-outlined" style="[^"]*">child_care</span>\s*</div>\s*<h4 class="text-xl font-bold mb-4 font-headline"[^>]*>Kids Development</h4>\s*<p class="text-on-surface-variant leading-relaxed mb-6"[^>]*>Nurturing the next generation through holistic play-based learning and psychological support systems.</p>\s*</div>'
    
    card1_new = """<div class="group premium-card bg-surface-container-lowest p-10 rounded-3xl relative overflow-hidden">
    <!-- Gradient Overlay -->
    <div class="absolute inset-0 bg-gradient-to-br from-primary to-primary/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-0"></div>
    <!-- Content -->
    <div class="relative z-10 transition-colors duration-300">
        <div class="w-14 h-14 rounded-2xl bg-primary-fixed flex items-center justify-center text-primary mb-8 transition-all group-hover:scale-110 group-hover:bg-white/20 group-hover:text-white">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">child_care</span>
        </div>
        <h4 class="text-xl font-bold mb-4 font-headline group-hover:text-white transition-colors duration-300">Kids Development</h4>
        <p class="text-on-surface-variant leading-relaxed mb-6 group-hover:text-white/90 transition-colors duration-300">Nurturing the next generation through holistic play-based learning and psychological support systems.</p>
    </div>
</div>"""

    card2_old = r'<div class="group premium-card bg-surface-container-lowest p-10 rounded-3xl hover:bg-secondary/5">\s*<div class="w-14 h-14 rounded-2xl bg-secondary-fixed flex items-center justify-center text-secondary mb-8 transition-transform group-hover:scale-110">\s*<span class="material-symbols-outlined" style="[^"]*">female</span>\s*</div>\s*<h4 class="text-xl font-bold mb-4 font-headline"[^>]*>Women Empowerment</h4>\s*<p class="text-on-surface-variant leading-relaxed mb-6"[^>]*>Unlocking potential through vocational training, entrepreneurship mentorship, and health advocacy.</p>\s*</div>'
    
    card2_new = """<div class="group premium-card bg-surface-container-lowest p-10 rounded-3xl relative overflow-hidden">
    <!-- Gradient Overlay -->
    <div class="absolute inset-0 bg-gradient-to-br from-secondary to-secondary/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-0"></div>
    <!-- Content -->
    <div class="relative z-10 transition-colors duration-300">
        <div class="w-14 h-14 rounded-2xl bg-secondary-fixed flex items-center justify-center text-secondary mb-8 transition-all group-hover:scale-110 group-hover:bg-white/20 group-hover:text-white">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">female</span>
        </div>
        <h4 class="text-xl font-bold mb-4 font-headline group-hover:text-white transition-colors duration-300">Women Empowerment</h4>
        <p class="text-on-surface-variant leading-relaxed mb-6 group-hover:text-white/90 transition-colors duration-300">Unlocking potential through vocational training, entrepreneurship mentorship, and health advocacy.</p>
    </div>
</div>"""

    card3_old = r'<div class="group premium-card bg-surface-container-lowest p-10 rounded-3xl hover:bg-tertiary/5">\s*<div class="w-14 h-14 rounded-2xl bg-tertiary-fixed flex items-center justify-center text-tertiary mb-8 transition-transform group-hover:scale-110">\s*<span class="material-symbols-outlined" style="[^"]*">auto_stories</span>\s*</div>\s*<h4 class="text-xl font-bold mb-4 font-headline"[^>]*>Education &amp; Learning</h4>\s*<p class="text-on-surface-variant leading-relaxed mb-6"[^>]*>Bridging the digital divide with tech-enabled classrooms and community-driven literacy programs.</p>\s*</div>'
    
    card3_new = """<div class="group premium-card bg-surface-container-lowest p-10 rounded-3xl relative overflow-hidden">
    <!-- Gradient Overlay -->
    <div class="absolute inset-0 bg-gradient-to-br from-tertiary to-tertiary/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-0"></div>
    <!-- Content -->
    <div class="relative z-10 transition-colors duration-300">
        <div class="w-14 h-14 rounded-2xl bg-tertiary-fixed flex items-center justify-center text-tertiary mb-8 transition-all group-hover:scale-110 group-hover:bg-white/20 group-hover:text-white">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">auto_stories</span>
        </div>
        <h4 class="text-xl font-bold mb-4 font-headline group-hover:text-white transition-colors duration-300">Education &amp; Learning</h4>
        <p class="text-on-surface-variant leading-relaxed mb-6 group-hover:text-white/90 transition-colors duration-300">Bridging the digital divide with tech-enabled classrooms and community-driven literacy programs.</p>
    </div>
</div>"""

    card4_old = r'<div class="group premium-card bg-surface-container-lowest p-10 rounded-3xl hover:bg-on-surface/5">\s*<div class="w-14 h-14 rounded-2xl bg-surface-container-highest flex items-center justify-center text-on-surface mb-8 transition-transform group-hover:scale-110">\s*<span class="material-symbols-outlined" style="[^"]*">handshake</span>\s*</div>\s*<h4 class="text-xl font-bold mb-4 font-headline"[^>]*>Community Support</h4>\s*<p class="text-on-surface-variant leading-relaxed mb-6"[^>]*>Strengthening local bonds through shared resources, crisis intervention, and urban development.</p>\s*</div>'

    card4_new = """<div class="group premium-card bg-surface-container-lowest p-10 rounded-3xl relative overflow-hidden">
    <!-- Gradient Overlay -->
    <div class="absolute inset-0 bg-gradient-to-br from-on-surface to-on-surface/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-0"></div>
    <!-- Content -->
    <div class="relative z-10 transition-colors duration-300">
        <div class="w-14 h-14 rounded-2xl bg-surface-container-highest flex items-center justify-center text-on-surface mb-8 transition-all group-hover:scale-110 group-hover:bg-white/20 group-hover:text-white">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">handshake</span>
        </div>
        <h4 class="text-xl font-bold mb-4 font-headline group-hover:text-white transition-colors duration-300">Community Support</h4>
        <p class="text-on-surface-variant leading-relaxed mb-6 group-hover:text-white/90 transition-colors duration-300">Strengthening local bonds through shared resources, crisis intervention, and urban development.</p>
    </div>
</div>"""

    content = re.sub(card1_old, card1_new, content)
    content = re.sub(card2_old, card2_new, content)
    content = re.sub(card3_old, card3_new, content)
    content = re.sub(card4_old, card4_new, content)

    with open("home/index.html", "w") as f:
        f.write(content)
        
fix_home()
print("Done")
