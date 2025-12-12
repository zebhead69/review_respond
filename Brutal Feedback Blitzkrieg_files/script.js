/**
 * @typedef {Object} IntersectionObserverConfig
 * @property {number} threshold - Threshold for intersection detection
 */

/**
 * Initializes scroll animations and hover effects when DOM is loaded
 * @returns {void}
 */
function initializeAnimations() {
    // Add intersection observer for scroll animations
    /** @type {NodeListOf<HTMLElement>} */
    const sections = document.querySelectorAll('section');

    /** @type {IntersectionObserverConfig} */
    const observerConfig = {
        threshold: 0.1
    };

    /**
     * Callback for intersection observer
     * @param {IntersectionObserverEntry[]} entries - Array of intersection observer entries
     * @returns {void}
     */
    const observerCallback = (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting && entry.target instanceof HTMLElement) {
                entry.target.classList.add('animate-fadeIn');
            }
        });
    };

    const observer = new IntersectionObserver(observerCallback, observerConfig);

    sections.forEach((section) => {
        observer.observe(section);
    });

    // Add brutalist hover effects to all buttons
    /** @type {NodeListOf<HTMLElement>} */
    const buttons = document.querySelectorAll('a, button');

    /**
     * Handles mouse enter event
     * @this {HTMLElement}
     * @returns {void}
     */
    function handleMouseEnter() {
        this.style.transform = 'scale(1.05)';
    }

    /**
     * Handles mouse leave event
     * @this {HTMLElement}
     * @returns {void}
     */
    function handleMouseLeave() {
        this.style.transform = 'scale(1)';
    }

    buttons.forEach((button) => {
        button.addEventListener('mouseenter', handleMouseEnter);
        button.addEventListener('mouseleave', handleMouseLeave);
    });
}

// Scroll animations
document.addEventListener('DOMContentLoaded', initializeAnimations);

/**
 * Handles form submission with email validation
 * @param {SubmitEvent} e - Form submit event
 * @this {HTMLFormElement}
 * @returns {void}
 */
function handleFormSubmit(e) {
    e.preventDefault();

    /** @type {HTMLInputElement | null} */
    const emailInput = this.querySelector('input[type="email"]');

    if (!emailInput) {
        console.error('Email input not found in form');
        return;
    }

    const email = emailInput.value;

    if (!email || !email.includes('@')) {
        alert('Please enter a valid email address');
        return;
    }

    alert(`Brutal honesty incoming! We'll contact you at ${email} within 24 hours. No bullshit.`);
    this.reset();
}

// Form submission handling
/** @type {HTMLFormElement | null} */
const form = document.querySelector('form');

if (form) {
    form.addEventListener('submit', handleFormSubmit);
}