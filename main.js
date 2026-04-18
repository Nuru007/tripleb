document.addEventListener("DOMContentLoaded", () => {
    // Scroll Reveal Observer
    const revealElements = document.querySelectorAll(".reveal-on-scroll");
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("reveal-visible");
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    revealElements.forEach(el => revealObserver.observe(el));

    // Stat Counter Observer
    const statCounters = document.querySelectorAll(".stat-counter");
    
    const animateValue = (obj, start, end, duration, prefix='', suffix='') => {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            // Ease-out cubic
            const easeOutProgress = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(easeOutProgress * (end - start) + start);
            
            // Format number if it's a float or large number (we handle this simply here, or assume integer targets)
            let currentDisplay = current;
            if (end % 1 !== 0) {
                 currentDisplay = (easeOutProgress * (end - start) + start).toFixed(1);
            }

            obj.innerHTML = prefix + currentDisplay + suffix;
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                obj.innerHTML = prefix + end + suffix; // ensure exact end
            }
        };
        window.requestAnimationFrame(step);
    };

    const statObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const targetStr = entry.target.getAttribute("data-target");
                const target = parseFloat(targetStr);
                const prefix = entry.target.getAttribute("data-prefix") || "";
                const suffix = entry.target.getAttribute("data-suffix") || "";
                
                animateValue(entry.target, 0, target, 2000, prefix, suffix);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });

    statCounters.forEach(el => statObserver.observe(el));

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
        }, 3000);
    }
});

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
