/**
 * Custom navbar web component with brutalist styling
 * @extends {HTMLElement}
 */
class CustomNavbar extends HTMLElement {
    /**
     * Creates a new CustomNavbar instance
     */
    constructor() {
        super();
        /** @type {ShadowRoot | null} */
        this._shadowRoot = null;
    }

    /**
     * Lifecycle callback invoked when element is connected to DOM
     * @returns {void}
     */
    connectedCallback() {
        this._shadowRoot = this.attachShadow({ mode: 'open' });

        if (!this._shadowRoot) {
            console.error('Failed to create shadow root for CustomNavbar');
            return;
        }

        this._shadowRoot.innerHTML = `
            <style>
                :host {
                    display: block;
                    position: fixed;
                    width: 100%;
                    top: 0;
                    left: 0;
                    z-index: 1000;
                    background-color: rgba(28, 18, 89, 0.9);
                    backdrop-filter: blur(5px);
                    border-bottom: 3px solid #ee4266;
                }
                
                nav {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 1rem 2rem;
                    max-width: 1200px;
                    margin: 0 auto;
                }
                
                .logo {
                    font-family: 'Urbanist', sans-serif;
                    font-weight: 900;
                    font-size: 1.5rem;
                    color: #fcd307;
                    text-decoration: none;
                }
                
                .nav-links {
                    display: flex;
                    gap: 2rem;
                }
                
                .nav-links a {
                    color: #d5daeb;
                    text-decoration: none;
                    font-family: 'Roboto', sans-serif;
                    font-weight: 700;
                    font-size: 1.1rem;
                    position: relative;
                    padding: 0.5rem 0;
                }
                
                .nav-links a::after {
                    content: '';
                    position: absolute;
                    bottom: 0;
                    left: 0;
                    width: 0;
                    height: 3px;
                    background-color: #ee4266;
                    transition: width 0.3s ease;
                }
                
                .nav-links a:hover::after {
                    width: 100%;
                }
                
                .cta-button {
                    background-color: #ee4266;
                    color: #1c1259;
                    padding: 0.5rem 1.5rem;
                    font-family: 'Urbanist', sans-serif;
                    font-weight: 900;
                    border: none;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                
                .cta-button:hover {
                    background-color: #fcd307;
                    transform: translateY(-2px);
                }
                
                @media (max-width: 768px) {
                    nav {
                        flex-direction: column;
                        padding: 1rem;
                    }
                    
                    .nav-links {
                        margin-top: 1rem;
                        flex-direction: column;
                        gap: 1rem;
                        align-items: center;
                    }
                }
            </style>
            
            <nav>
                <a href="/" class="logo">BRUTAL FEEDBACK</a>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/pricing">Pricing</a>
                    <a href="/faq">FAQ</a>
                    <a href="/legal">Legal</a>
                </div>
                <a href="/pricing" class="cta-button">GET STARTED</a>
            </nav>
        `;
    }
}

/**
 * Register the custom navbar element
 * @type {void}
 */
customElements.define('custom-navbar', CustomNavbar);