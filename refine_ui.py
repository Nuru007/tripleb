import os
import re

css_updates = """
/* Mission & Vision specific */
.mission-card {
    background-color: #5E3A8C;
    color: white;
    border-radius: 2rem;
    transition: all 0.3s ease;
    border: none;
}

.mission-card:hover {
    transform: scale(1.02);
    box-shadow: 0 25px 50px -12px rgba(94, 58, 140, 0.3);
}

.mission-card .material-symbols-outlined {
    color: white;
}

.mission-card .icon-container {
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 1rem;
}

.vision-card {
    background-color: #D63384;
    color: white;
    border-radius: 2rem;
    transition: all 0.3s ease;
    border: none;
}

.vision-card:hover {
    transform: scale(1.02);
    box-shadow: 0 25px 50px -12px rgba(214, 51, 132, 0.3);
}

.vision-card .material-symbols-outlined {
    color: white;
}

.vision-card .icon-container {
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 1rem;
}
"""

def update_style_css():
    with open("style.css", "r") as f:
        content = f.read()
    
    # Replace old mission/vision styles
    old_css_regex = re.compile(r'/\* Mission & Vision specific \*/.*\.card-hover-transition:hover \{\s*transform: scale\(1\.02\);\s*\}', re.DOTALL)
    content = old_css_regex.sub(css_updates.strip(), content)
    
    with open("style.css", "w") as f:
        f.write(content)

def update_main_js():
    with open("main.js", "r") as f:
        content = f.read()
    
    # Update setInterval from 4000 to 3000, and rotate 4 items
    old_interval = """setInterval(() => {
            // Pick two random indices
            const i1 = Math.floor(Math.random() * 9);
            let i2 = Math.floor(Math.random() * 9);
            while(i1 === i2) i2 = Math.floor(Math.random() * 9);
            
            // Swap
            const temp = positions[i1];
            positions[i1] = positions[i2];
            positions[i2] = temp;
            
            updateGrid();
        }, 4000);"""
    
    new_interval = """setInterval(() => {
            // Pick 4 unique random indices to rotate
            let indices = [];
            while(indices.length < 4) {
                let r = Math.floor(Math.random() * 9);
                if(indices.indexOf(r) === -1) indices.push(r);
            }
            
            // Rotate their positions: 0->1, 1->2, 2->3, 3->0
            const temp = positions[indices[3]];
            positions[indices[3]] = positions[indices[2]];
            positions[indices[2]] = positions[indices[1]];
            positions[indices[1]] = positions[indices[0]];
            positions[indices[0]] = temp;
            
            updateGrid();
        }, 3000);"""
    
    content = content.replace(old_interval, new_interval)
    with open("main.js", "w") as f:
        f.write(content)

def update_html():
    html_files = ["home/index.html", "index.html", "who_we_are/index.html", "gallery/index.html", "contact_us/index.html"]
    
    for path in html_files:
        if not os.path.exists(path): continue
        with open(path, "r") as f:
            content = f.read()
            
        # Global Spacing Reduction
        content = content.replace('py-24 md:py-32', 'py-16 md:py-20')
        content = content.replace('py-24 px-6 md:px-12', 'py-16 md:py-20 px-6 md:px-12')
        content = content.replace('pt-12 pb-24 md:pt-24 md:pb-32', 'pt-8 pb-16 md:pt-16 md:pb-24')
        content = content.replace('mb-16', 'mb-12')
        content = content.replace('gap-16', 'gap-12')
        content = content.replace('p-12 md:p-20', 'p-10 md:p-16')
        content = content.replace('p-12 rounded-[2.5rem]', 'p-10 rounded-3xl')

        # Mission & Vision Redesign in who_we_are
        if path == "who_we_are/index.html":
            # Current HTML has title and text left-aligned, we need center alignment and simpler text per the reference
            
            # The structure to replace:
            old_mission = r'<!-- Mission Card -->\n<div class="mission-card card-hover-transition p-12 rounded-3xl relative overflow-hidden group duration-500">\n<div class="relative z-10">\n<div class="icon-container w-12 h-12 flex items-center justify-center rounded-xl mb-8">\n<span class="material-symbols-outlined" style="font-variation-settings: \'FILL\' 1;">target</span>\n</div>\n<h3 class="font-headline text-3xl font-bold mb-6">Our Mission</h3>\n<p class="text-xl text-on-surface-variant font-light leading-relaxed">\n                            To re-architect the way humanity interacts with social change, utilizing high-end design principles to foster empathy and drive institutional investment toward sustainable grassroots movements.\n                        </p>\n</div>\n<!-- Ambient Glow Effect -->\n<div class="absolute -right-24 -bottom-24 w-64 h-64 bg-primary/5 rounded-full blur-3xl group-hover:bg-primary/10 transition-colors"></div>\n</div>'
            
            new_mission = """<!-- Mission Card -->
<div class="mission-card p-12 relative overflow-hidden group flex flex-col items-center text-center justify-center min-h-[300px]">
    <div class="relative z-10 flex flex-col items-center">
        <div class="icon-container w-16 h-16 flex items-center justify-center mb-6 shadow-inner">
            <span class="material-symbols-outlined text-3xl" style="font-variation-settings: 'FILL' 1;">target</span>
        </div>
        <h3 class="font-headline text-3xl font-bold">Our Mission</h3>
        <p class="text-lg font-light leading-relaxed mt-4 opacity-90 max-w-sm">
            To re-architect the way humanity interacts with social change, utilizing high-end design principles to foster empathy and drive institutional investment.
        </p>
    </div>
</div>"""

            old_vision = r'<!-- Vision Card -->\n<div class="vision-card card-hover-transition p-12 rounded-3xl relative overflow-hidden group duration-500">\n<div class="relative z-10">\n<div class="icon-container w-12 h-12 flex items-center justify-center rounded-xl mb-8">\n<span class="material-symbols-outlined" style="font-variation-settings: \'FILL\' 1;">visibility</span>\n</div>\n<h3 class="font-headline text-3xl font-bold mb-6">Our Vision</h3>\n<p class="text-xl text-on-surface-variant font-light leading-relaxed">\n                            A world where the standard for social contribution is not measured by the scale of the struggle, but by the elegance of the solution and the dignity preserved for every human involved.\n                        </p>\n</div>\n<!-- Ambient Glow Effect -->\n<div class="absolute -right-24 -bottom-24 w-64 h-64 bg-tertiary/5 rounded-full blur-3xl group-hover:bg-tertiary/10 transition-colors"></div>\n</div>'

            new_vision = """<!-- Vision Card -->
<div class="vision-card p-12 relative overflow-hidden group flex flex-col items-center text-center justify-center min-h-[300px]">
    <div class="relative z-10 flex flex-col items-center">
        <div class="icon-container w-16 h-16 flex items-center justify-center mb-6 shadow-inner">
            <span class="material-symbols-outlined text-3xl" style="font-variation-settings: 'FILL' 1;">visibility</span>
        </div>
        <h3 class="font-headline text-3xl font-bold">Our Vision</h3>
        <p class="text-lg font-light leading-relaxed mt-4 opacity-90 max-w-sm">
            A world where the standard for social contribution is not measured by the scale of the struggle, but by the elegance of the solution and dignity.
        </p>
    </div>
</div>"""
            # Use regex sub for reliable replacement ignoring slight whitespace differences
            content = re.sub(r'<!-- Mission Card -->[\s\S]*?</div>\n</div>', new_mission, content, count=1)
            content = re.sub(r'<!-- Vision Card -->[\s\S]*?</div>\n</div>', new_vision, content, count=1)

        with open(path, "w") as f:
            f.write(content)

update_style_css()
update_main_js()
update_html()
print("Refinements applied.")
