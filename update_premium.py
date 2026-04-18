import os
import re

css_additions = """
/* Premium Hover Effects */
.premium-image-hover {
    transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.premium-image-hover:hover {
    transform: scale(1.03) translateY(-4px);
    box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.2);
}

.premium-card {
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    border: 1px solid rgba(0, 0, 0, 0.04);
}

.premium-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1);
}

/* 3x3 Grid Wrapper */
.dynamic-grid-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 16/9;
    max-height: 80vh;
}

@media (max-width: 768px) {
    .dynamic-grid-wrapper {
        aspect-ratio: 1;
    }
}

.dynamic-grid-item {
    position: absolute;
    width: calc(33.333% - 1rem);
    height: calc(33.333% - 1rem);
    transition: all 2s cubic-bezier(0.25, 1, 0.25, 1);
    border-radius: 1.5rem;
    overflow: hidden;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.1);
}

.dynamic-grid-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
"""

js_additions = """
    // Dynamic 3x3 Grid Logic
    const gridItems = document.querySelectorAll('.dynamic-grid-item');
    if (gridItems.length === 9) {
        // Initialize positions
        let positions = [];
        for(let row=0; row<3; row++) {
            for(let col=0; col<3; col++) {
                positions.push({row, col});
            }
        }
        
        const updateGrid = () => {
            gridItems.forEach((item, index) => {
                const pos = positions[index];
                item.style.top = `calc(${pos.row * 33.333}% + 0.5rem)`;
                item.style.left = `calc(${pos.col * 33.333}% + 0.5rem)`;
            });
        };
        
        updateGrid();
        
        // Randomly swap positions every 4 seconds
        setInterval(() => {
            // Pick two random indices
            const i1 = Math.floor(Math.random() * 9);
            let i2 = Math.floor(Math.random() * 9);
            while(i1 === i2) i2 = Math.floor(Math.random() * 9);
            
            // Swap
            const temp = positions[i1];
            positions[i1] = positions[i2];
            positions[i2] = temp;
            
            updateGrid();
        }, 4000);
    }
"""

grid_html = """
<!-- Dynamic Image Grid Section -->
<section class="py-24 px-6 md:px-12 bg-surface-container-low reveal-on-scroll">
    <div class="max-w-screen-xl mx-auto">
        <div class="text-center mb-16 space-y-4">
            <h2 class="text-4xl md:text-5xl font-extrabold tracking-tighter font-headline text-on-surface">Moments of Impact</h2>
            <p class="text-xl text-on-surface-variant font-light max-w-2xl mx-auto">A glimpse into the communities we empower and the progress we curate.</p>
        </div>
        
        <div class="dynamic-grid-wrapper">
            <!-- 9 Images -->
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1593113514676-5f01cec7653c?auto=format&fit=crop&w=600&q=80" alt="Impact 1"></div>
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&w=600&q=80" alt="Impact 2"></div>
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1542810634-71277d95dc8c?auto=format&fit=crop&w=600&q=80" alt="Impact 3"></div>
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?auto=format&fit=crop&w=600&q=80" alt="Impact 4"></div>
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1511632765486-a01980e01a18?auto=format&fit=crop&w=600&q=80" alt="Impact 5"></div>
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1559027615-cd4628902d4a?auto=format&fit=crop&w=600&q=80" alt="Impact 6"></div>
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1529390079861-591de354faf5?auto=format&fit=crop&w=600&q=80" alt="Impact 7"></div>
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=600&q=80" alt="Impact 8"></div>
            <div class="dynamic-grid-item premium-image-hover"><img src="https://images.unsplash.com/photo-1509099836639-18ba1795216d?auto=format&fit=crop&w=600&q=80" alt="Impact 9"></div>
        </div>
    </div>
</section>
"""

# 1. Update style.css
with open("style.css", "a") as f:
    f.write(css_additions)

# 2. Update main.js
with open("main.js", "r") as f:
    main_js = f.read()

if "Dynamic 3x3 Grid Logic" not in main_js:
    # insert before the closing '});' of DOMContentLoaded
    main_js = main_js.rsplit("});", 1)
    main_js = main_js[0] + js_additions + "});"
    with open("main.js", "w") as f:
        f.write(main_js)

# 3. Update HTML files
html_files = ["home/index.html", "index.html", "who_we_are/index.html", "gallery/index.html"]

for path in html_files:
    if not os.path.exists(path): continue
    
    with open(path, "r") as f:
        content = f.read()
        
    # Apply global premium image hover to Hero images
    # We find `<img class="w-full h-full object-cover animate-zoom"`
    # Or `<img class="w-full h-full object-cover animate-float"`
    content = content.replace('class="w-full h-full object-cover animate-zoom"', 'class="w-full h-full object-cover animate-zoom premium-image-hover"')
    content = content.replace('class="w-full h-full object-cover animate-float"', 'class="w-full h-full object-cover animate-float premium-image-hover"')
    content = content.replace('class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"', 'class="w-full h-full object-cover premium-image-hover"')
    
    if path in ["home/index.html", "index.html"]:
        # Remove "Join us in making an impact" section (lines 265 to 276 approx)
        # We can use regex to find the section containing "Become a Catalyst"
        # Since it's a multi-line HTML string, we need to be careful.
        cta_regex = re.compile(r'<!-- CTA Section -->\n<section class="py-24 px-6 md:px-12 bg-surface-container-low reveal-on-scroll">\s*<div class="max-w-4xl mx-auto text-center space-y-10">[\s\S]*?</section>')
        content = cta_regex.sub(grid_html, content)
        
        # What We Do cards: remove "Learn More" links
        # ` <a class="inline-flex items-center text-primary font-bold group-hover:gap-3 transition-all" href="/contact_us/" style="">\n                        Learn More <span class="material-symbols-outlined ml-1 text-sm" style="">arrow_forward</span>\n</a>`
        # We can just use a regex to match and remove any <a ...>Learn More ...</a> inside What We Do section
        learn_more_regex = re.compile(r'<a class="inline-flex[^>]*>\s*Learn More.*?</a>', re.DOTALL)
        content = learn_more_regex.sub('', content)
        
        # Add .premium-card to cards
        content = content.replace('group bg-surface-container-lowest p-10 rounded-[2rem] hover:bg-primary/5 transition-all duration-300 border border-outline-variant/10', 'group premium-card bg-surface-container-lowest p-12 rounded-[2.5rem] hover:bg-primary/5')
        content = content.replace('group bg-surface-container-lowest p-10 rounded-[2rem] hover:bg-secondary/5 transition-all duration-300 border border-outline-variant/10', 'group premium-card bg-surface-container-lowest p-12 rounded-[2.5rem] hover:bg-secondary/5')
        content = content.replace('group bg-surface-container-lowest p-10 rounded-[2rem] hover:bg-tertiary/5 transition-all duration-300 border border-outline-variant/10', 'group premium-card bg-surface-container-lowest p-12 rounded-[2.5rem] hover:bg-tertiary/5')
        content = content.replace('group bg-surface-container-lowest p-10 rounded-[2rem] hover:bg-on-surface/5 transition-all duration-300 border border-outline-variant/10', 'group premium-card bg-surface-container-lowest p-12 rounded-[2.5rem] hover:bg-on-surface/5')
        
    with open(path, "w") as f:
        f.write(content)
print("Applied premium updates.")
