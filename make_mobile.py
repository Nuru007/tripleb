import os
import re

def make_mobile():
    html_files = ["home/index.html", "index.html", "who_we_are/index.html", "gallery/index.html", "contact_us/index.html"]
    
    for path in html_files:
        if not os.path.exists(path): continue
        with open(path, "r") as f:
            content = f.read()
            
        # 1. Add Mobile Menu Button
        support_us_btn_end = "Support Us\n                </a>"
        new_support_us_end = """Support Us
                </a>
                <button id="mobile-menu-btn" class="md:hidden flex items-center justify-center p-2 text-on-surface hover:text-primary transition-colors focus:outline-none">
                    <span class="material-symbols-outlined text-3xl" style="font-variation-settings: 'FILL' 0;">menu</span>
                </button>"""
        content = content.replace(support_us_btn_end, new_support_us_end)
        
        # 2. Add Mobile Dropdown Menu
        header_end = "</div>\n</header>"
        if "id=\"mobile-menu\"" not in content:
            new_header_end = """</div>
    <!-- Mobile Navigation Dropdown -->
    <div id="mobile-menu" class="hidden md:hidden absolute top-full left-0 w-full bg-white/95 backdrop-blur-xl shadow-[0_20px_40px_0_rgba(21,25,53,0.1)] border-t border-slate-200/50 flex-col items-center py-8 gap-6 z-50">
        <a class="text-slate-800 font-bold text-xl hover:text-pink-600 transition-colors font-headline" href="/">Home</a>
        <a class="text-slate-800 font-bold text-xl hover:text-pink-600 transition-colors font-headline" href="/who_we_are/">Who We Are</a>
        <a class="text-slate-800 font-bold text-xl hover:text-pink-600 transition-colors font-headline" href="/gallery/">Gallery</a>
        <a class="text-slate-800 font-bold text-xl hover:text-pink-600 transition-colors font-headline" href="/contact_us/">Contact Us</a>
    </div>
</header>"""
            content = content.replace(header_end, new_header_end)
        
        # 3. Hide Floating Stat Cards on Mobile
        if path in ["home/index.html", "index.html"]:
            content = content.replace('flex items-center gap-4 animate-float border', 'hidden md:flex items-center gap-4 animate-float border')
        
        with open(path, "w") as f:
            f.write(content)
            
make_mobile()

# Update main.js
with open("main.js", "r") as f:
    js_content = f.read()

if "mobile-menu-btn" not in js_content:
    js_content += """

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const iconSpan = mobileBtn?.querySelector('.material-symbols-outlined');
    
    if (mobileBtn && mobileMenu) {
        mobileBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            mobileMenu.classList.toggle('flex');
            if (mobileMenu.classList.contains('hidden')) {
                iconSpan.textContent = 'menu';
            } else {
                iconSpan.textContent = 'close';
            }
        });
    }
});
"""
    with open("main.js", "w") as f:
        f.write(js_content)
        
print("Mobile responsiveness added.")
