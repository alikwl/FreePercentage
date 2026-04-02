/* 
  PROJECT: FreePercentage.com 
  FILE: assets/script.js 
  DESCRIPTION: Global JavaScript for theme management, mobile navigation, 
               FAQ accordions, and utility functions used across all tool pages.
*/

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initMobileNav();
    initFAQ();
    initSmoothScroll();
    initTOC();
});

/**
 * 1. DARK MODE TOGGLE
 * Handles theme switching and persists preference to localStorage
 */
function initTheme() {
    const toggleBtn = document.getElementById('darkModeToggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply stored theme on load
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            let theme = document.documentElement.getAttribute('data-theme');
            let newTheme = theme === 'light' ? 'dark' : 'light';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }
}

function updateThemeIcon(theme) {
    const toggleBtn = document.getElementById('darkModeToggle');
    if (toggleBtn) {
        toggleBtn.textContent = theme === 'light' ? '🌙' : '☀️';
    }
}

/**
 * 2. MOBILE NAVIGATION
 * Handles hamburger menu and mobile dropdowns
 */
function initMobileNav() {
    const hamburger = document.getElementById('hamburger');
    const mainNav = document.getElementById('mainNav');
    const dropdowns = document.querySelectorAll('.has-dropdown');

    if (hamburger && mainNav) {
        hamburger.addEventListener('click', (e) => {
            e.stopPropagation();
            mainNav.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!mainNav.contains(e.target) && !hamburger.contains(e.target)) {
                mainNav.classList.remove('active');
            }
        });
    }

    // Handle mobile dropdown toggles
    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('a');
        link.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dropdown.classList.toggle('active');
            }
        });
    });
}

/**
 * 3. FAQ ACCORDION
 * Logic for the expanding/collapsing FAQ sections on tool pages
 */
function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                // Close other open items (optional, for accordion effect)
                faqItems.forEach(otherItem => {
                    if (otherItem !== item) otherItem.classList.remove('active');
                });
                
                item.classList.toggle('active');
            });
        }
    });
}

/**
 * 4. SMOOTH SCROLLING
 * Smooth transition for anchor links (e.g., Table of Contents)
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * 5. TABLE OF CONTENTS GENERATOR
 * Automatically generates a TOC based on H2 and H3 tags in the .tool-main area
 */
function initTOC() {
    const tocContainer = document.querySelector('.toc-box ol');
    const mainContent = document.querySelector('.tool-main');
    
    // Only auto-generate if the TOC list is empty (manual lists take priority)
    if (tocContainer && mainContent && tocContainer.children.length === 0) {
        const headings = mainContent.querySelectorAll('h2, h3');
        
        headings.forEach((heading, index) => {
            // Skip "Related Tools" and "Embed" headings
            if (heading.textContent.includes('Other Useful') || heading.textContent.includes('Embed')) return;
            
            const id = heading.id || heading.textContent.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]/g, '');
            heading.id = id;
            
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = `#${id}`;
            a.textContent = heading.textContent;
            
            if (heading.tagName === 'H3') {
                li.style.marginLeft = '20px';
                li.style.fontSize = '0.9rem';
            }
            
            li.appendChild(a);
            tocContainer.appendChild(li);
        });
    }
}

/**
 * 6. GLOBAL UTILITY FUNCTIONS
 * Functions called by tool-specific scripts
 */

// Generic Copy to Clipboard
async function copyTextToClipboard(elementId, fallbackText = 'Copied!') {
    const text = elementId ? document.getElementById(elementId).textContent : fallbackText;
    try {
        await navigator.clipboard.writeText(text);
        return true;
    } catch (err) {
        console.error('Failed to copy: ', err);
        return false;
    }
}

// Specialized result copy for tools
function copyResult() {
    const resultVal = document.getElementById('resultValue');
    if (resultVal) {
        const success = copyTextToClipboard(resultVal.id);
        if (success) alert('Result copied to clipboard!');
    }
}

// Specialized embed code copy for tools
function copyEmbed() {
    const code = document.getElementById('embedCode');
    if (code) {
        const success = copyTextToClipboard(code.id);
        if (success) alert('Embed code copied to clipboard!');
    }
}