// Advanced Animations for Panache Dental Care
document.addEventListener('DOMContentLoaded', function() {
    
    // Typing Animation for Hero Section
    const typingElements = [
        {
            element: '.hero-section h1',
            text: 'Dr. Sandeep Prakash',
            speed: 100
        },
        {
            element: '.hero-section h2',
            text: 'Oral & Maxillo-Facial Surgeon',
            speed: 50
        }
    ];

    typingElements.forEach(({ element, text, speed }) => {
        const elementToType = document.querySelector(element);
        if (elementToType) {
            elementToType.textContent = '';
            typeText(elementToType, text, speed);
        }
    });

    function typeText(element, text, speed) {
        let index = 0;
        
        function type() {
            if (index < text.length) {
                element.textContent += text.charAt(index);
                index++;
                setTimeout(type, speed);
            } else {
                element.style.borderRight = '2px solid var(--primary-red)';
                setTimeout(() => {
                    element.style.borderRight = 'none';
                }, 2000);
            }
        }
        type();
    }

    // Intersection Observer for Scroll Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Add animations to different sections
    const animateElements = [
        '.doctor-card',
        '.section-title',
        '.education-card',
        '.service-card',
        '.contact-info',
        '.text-center .col-md-4'
    ];

    animateElements.forEach((selector, index) => {
        const elements = document.querySelectorAll(selector);
        elements.forEach((element, elemIndex) => {
            element.classList.add('animate-element');
            observer.observe(element);
        });
    });

    // Counter Animation for Statistics
    function animateCounter(element, target, duration = 2000) {
        let start = 0;
        const increment = target / (duration / 16);
        
        function updateCounter() {
            start += increment;
            if (start < target) {
                element.textContent = Math.floor(start) + '+';
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target + '+';
            }
        }
        updateCounter();
    }

    // Start counter animation when visible
    const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counters = [
                    { element: entry.target.querySelector('.col-4:nth-child(1) .h3'), target: 18 },
                    { element: entry.target.querySelector('.col-4:nth-child(2) .h3'), target: 1000 },
                    { element: entry.target.querySelector('.col-4:nth-child(3) .h3'), target: 15 }
                ];
                
                counters.forEach((counter, index) => {
                    if (counter.element) {
                        setTimeout(() => {
                            animateCounter(counter.element, counter.target);
                        }, index * 200);
                    }
                });
                
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const statsRow = document.querySelector('.hero-section .row.text-center');
    if (statsRow) {
        counterObserver.observe(statsRow);
    }

    // Floating animation for doctor cards
    const doctorCards = document.querySelectorAll('.doctor-card img');
    doctorCards.forEach((card, index) => {
        card.style.animation = `float ${3 + index * 0.5}s ease-in-out infinite`;
    });

    // Parallax effect for hero section
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallax = document.querySelector('.hero-section');
        if (parallax) {
            const speed = 0.3;
            parallax.style.transform = `translateY(${scrolled * speed}px)`;
        }
    });

    // Glitch effect for headings
    const headings = document.querySelectorAll('.section-title');
    headings.forEach(heading => {
        heading.addEventListener('mouseenter', function() {
            this.style.animation = 'glitch 0.3s ease-in-out';
            setTimeout(() => {
                this.style.animation = '';
            }, 300);
        });
    });

    // Pulse animation for CTA buttons
    const ctaButtons = document.querySelectorAll('.btn-primary-custom');
    ctaButtons.forEach(button => {
        button.classList.add('pulse-animation');
    });

    // Magnetic effect for buttons
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            this.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translate(0, 0)';
        });
    });
});