// Advanced Scroll Animations for Panache Dental
document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // SCROLL ANIMATION SYSTEM
    // ============================================
    
    // Configuration
    const animationConfig = {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px',
        once: false // Set to true if you want animation to run only once
    };
    
    // Track elements that have been animated
    const animatedElements = new Set();
    
    // Intersection Observer for scroll animations
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const element = entry.target;
            
            if (entry.isIntersecting) {
                // Add animation class when element comes into view
                element.classList.add('animate-in');
                element.classList.remove('animate-out');
                animatedElements.add(element);
            } else if (!animationConfig.once) {
                // Remove animation class when element goes out of view (reverse animation)
                element.classList.remove('animate-in');
                element.classList.add('animate-out');
            }
        });
    }, animationConfig);
    
    // Observe all elements with scroll animation classes
    const scrollElements = document.querySelectorAll('.scroll-left, .scroll-right, .scroll-up, .scroll-down');
    scrollElements.forEach(el => scrollObserver.observe(el));
    
    // ============================================
    // LEGACY ANIMATION SUPPORT
    // ============================================
    const legacyObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.animate-element, .reveal, .reveal-left, .reveal-right, .reveal-scale').forEach(el => {
        legacyObserver.observe(el);
    });
    
    // ============================================
    // SECTION VISIBILITY ANIMATION
    // ============================================
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else if (!animationConfig.once) {
                entry.target.classList.remove('visible');
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.section-fade-in').forEach(el => {
        sectionObserver.observe(el);
    });
    
    // ============================================
    // CARD SLIDE ANIMATIONS
    // ============================================
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('slide-in');
            } else if (!animationConfig.once) {
                entry.target.classList.remove('slide-in');
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.card-slide-left, .card-slide-right').forEach(el => {
        cardObserver.observe(el);
    });
    
    // ============================================
    // TYPING ANIMATION FOR HEADINGS
    // ============================================
    function initTypingAnimation() {
        const typingElements = document.querySelectorAll('.typing-text, .typewriter');
        
        typingElements.forEach(element => {
            const text = element.getAttribute('data-text') || element.textContent;
            element.textContent = '';
            element.setAttribute('data-text', text);
            
            let index = 0;
            const speed = parseInt(element.getAttribute('data-speed')) || 100;
            
            function type() {
                if (index < text.length) {
                    element.textContent += text.charAt(index);
                    index++;
                    setTimeout(type, speed);
                }
            }
            
            // Start typing when element is in view
            const typeObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && element.textContent === '') {
                        type();
                        typeObserver.unobserve(element);
                    }
                });
            }, { threshold: 0.5 });
            
            typeObserver.observe(element);
        });
    }
    
    initTypingAnimation();
    
    // ============================================
    // STAT BOX COUNTER ANIMATION
    // ============================================
    function animateCounters() {
        const counters = document.querySelectorAll('.stat-number');
        
        counters.forEach(counter => {
            const text = counter.textContent;
            const match = text.match(/(\d+)/);
            
            if (match) {
                const target = parseInt(match[0]);
                const suffix = text.replace(match[0], '');
                let current = 0;
                const increment = target / 50;
                
                const updateCounter = () => {
                    if (current < target) {
                        current += increment;
                        counter.textContent = Math.floor(current) + suffix;
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target + suffix;
                    }
                };
                
                const counterObserver = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            updateCounter();
                            counterObserver.unobserve(counter);
                        }
                    });
                }, { threshold: 0.5 });
                
                counterObserver.observe(counter);
            }
        });
    }
    
    animateCounters();
    
    // ============================================
    // HERO ANIMATIONS
    // ============================================
    function initHeroAnimations() {
        const heroElements = document.querySelectorAll('.hero-animate');
        
        heroElements.forEach((element, index) => {
            element.style.transitionDelay = `${index * 0.2}s`;
            setTimeout(() => {
                element.classList.add('fade-in');
            }, 100);
        });
    }
    
    // Run hero animations on load
    if (document.querySelector('.hero-section, .hero-new')) {
        initHeroAnimations();
    }
    
    // ============================================
    // STAGGERED ANIMATIONS FOR GRID ITEMS
    // ============================================
    function initStaggeredAnimations() {
        const grids = document.querySelectorAll('.row.g-4, .row.g-3, .row.g-2');
        
        grids.forEach(grid => {
            const items = grid.querySelectorAll('[class*="col-"]');
            
            items.forEach((item, index) => {
                // Add delay based on position
                const delay = (index % 4) * 0.1;
                item.style.transitionDelay = `${delay}s`;
                
                // Add scroll animation class
                if (index % 2 === 0) {
                    item.classList.add('scroll-left');
                } else {
                    item.classList.add('scroll-right');
                }
                
                scrollObserver.observe(item);
            });
        });
    }
    
    initStaggeredAnimations();
    
    // ============================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // ============================================
    // PARALLAX EFFECT
    // ============================================
    function initParallax() {
        const parallaxElements = document.querySelectorAll('.parallax-section');
        
        if (parallaxElements.length > 0) {
            window.addEventListener('scroll', () => {
                const scrolled = window.pageYOffset;
                
                parallaxElements.forEach(el => {
                    const speed = 0.5;
                    const yPos = -(scrolled * speed);
                    el.style.backgroundPositionY = `${yPos}px`;
                });
            });
        }
    }
    
    initParallax();
    
    // ============================================
    // IMAGE LAZY LOAD ANIMATION
    // ============================================
    function initImageAnimations() {
        const images = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.getAttribute('data-src');
                    img.removeAttribute('data-src');
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        }, { threshold: 0.1 });
        
        images.forEach(img => imageObserver.observe(img));
    }
    
    initImageAnimations();
    
    // ============================================
    // SCROLL TO TOP BUTTON
    // ============================================
    function createScrollTopButton() {
        const btn = document.createElement('button');
        btn.innerHTML = '<i class="fas fa-arrow-up"></i>';
        btn.className = 'scroll-top-btn';
        btn.style.cssText = `
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: var(--primary-red, #8B0000);
            color: white;
            border: none;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 1000;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        `;
        
        document.body.appendChild(btn);
        
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                btn.style.opacity = '1';
                btn.style.visibility = 'visible';
            } else {
                btn.style.opacity = '0';
                btn.style.visibility = 'hidden';
            }
        });
        
        btn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
    
    createScrollTopButton();
});
