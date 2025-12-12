/**
 * Custom footer web component with brutalist styling
 * @extends {HTMLElement}
 */
class CustomFooter extends HTMLElement {
    /**
     * Creates a new CustomFooter instance
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
            console.error('Failed to create shadow root for CustomFooter');
            return;
        }

        this._shadowRoot.innerHTML = `
            <style>
                :host {
                    display: block;
                    background-color: #1c1259;
                    color: #d5daeb;
                    padding: 3rem 2rem;
                    border-top: 5px solid #ee4266;
                }

                .footer-container {
                    max-width: 1200px;
                    margin: 0 auto;
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 2rem;
                }

                .footer-logo {
                    font-family: 'Urbanist', sans-serif;
                    font-size: 1.8rem;
                    color: #fcd307;
                    margin-bottom: 1rem;
                }

                .footer-links h3 {
                    font-family: 'Urbanist', sans-serif;
                    color: #ee4266;
                    margin-bottom: 1rem;
                    font-size: 1.2rem;
                }

                .footer-links ul {
                    list-style: none;
                    padding: 0;
                }

                .footer-links li {
                    margin-bottom: 0.5rem;
                }

                .footer-links a {
                    color: #d5daeb;
                    text-decoration: none;
                    transition: color 0.3s ease;
                }

                .footer-links a:hover {
                    color: #fcd307;
                }

                .social-links {
                    display: flex;
                    gap: 1rem;
                    margin-top: 1rem;
                }

                .social-links a {
                    color: #d5daeb;
                    font-size: 1.5rem;
                    transition: color 0.3s ease;
                }

                .social-links a:hover {
                    color: #ee4266;
                }

                .copyright {
                    text-align: center;
                    margin-top: 3rem;
                    padding-top: 1rem;
                    border-top: 1px solid rgba(213, 218, 235, 0.2);
                }

                @media (max-width: 768px) {
                    .footer-container {
                        grid-template-columns: 1fr;
                    }
                }
            </style>

            <div class="footer-container">
                <div class="footer-about">
                    <div class="footer-logo">BRUTAL FEEDBACK</div>
                    <p>We brutally honest about your feedback management. Because your customers deserve answers.</p>
                    <div class="social-links">
                        <a href="#"><i data-feather="twitter"></i></a>
                        <a href="#"><i data-feather="linkedin"></i></a>
                        <a href="#"><i data-feather="facebook"></i></a>
                    </div>
                </div>

                <div class="footer-links">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/pricing">Pricing</a></li>
                        <li><a href="/faq">FAQ</a></li>
                        <li><a href="/legal">Legal</a></li>
                    </ul>
                </div>

                <div class="footer-links">
                    <h3>Resources</h3>
                    <ul>
                        <li><a href="/blog">Blog</a></li>
                        <li><a href="/contact">Contact</a></li>
                        <li><a href="/support">Support</a></li>
                    </ul>
                </div>
            </div>

            <div class="copyright">
                <p>&copy; ${new Date().getFullYear()} Brutal Feedback. All rights reserved.</p>
            </div>
        `;
    }
}

/**
 * Register the custom footer element
 * @type {void}
 */
customElements.define('custom-footer', CustomFooter);
