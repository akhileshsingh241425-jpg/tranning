import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import {
  FaTwitter,
  FaLinkedinIn,
  FaInstagram,
  FaYoutube,
  FaFacebook,
  FaEnvelope,
  FaPaperPlane
} from 'react-icons/fa';
import logo from '../assets/fevicon.png';

const Footer = () => {
  const [email, setEmail] = useState('');
  const [subscribeStatus, setSubscribeStatus] = useState(null); // 'success' | 'error' | null
  const [subscribeLoading, setSubscribeLoading] = useState(false);
  const location = useLocation();

  const handleNewsletterSubmit = async (e) => {
    e.preventDefault();
    if (!email) return;
    
    setSubscribeLoading(true);
    setSubscribeStatus(null);
    
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL || ''}/api/subscribe`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
      });
      
      const data = await response.json();
      
      if (data.success) {
        setSubscribeStatus('success');
        setEmail('');
      } else {
        setSubscribeStatus(data.message || 'Something went wrong');
      }
    } catch (err) {
      setSubscribeStatus('Network error. Please try again.');
    }
    
    setSubscribeLoading(false);
    
    // Auto-hide status message after 5 seconds
    setTimeout(() => setSubscribeStatus(null), 5000);
  };

  const scrollToSection = (e, sectionId) => {
    e.preventDefault();
    if (location.pathname === '/') {
      const element = document.getElementById(sectionId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    } else {
      window.location.href = '/#' + sectionId;
    }
  };

  return (
    <footer className="footer">
      {/* Newsletter Section */}
      <div className="footer-newsletter">
        <div className="newsletter-content">
          <h3>Stay Ahead in Your Career</h3>
          <p>Get free career guides, course updates, and industry insights delivered to your inbox.</p>
          <form className="newsletter-form" onSubmit={handleNewsletterSubmit}>
            <input
              type="email"
              placeholder="Enter your email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              disabled={subscribeLoading}
            />
            <button type="submit" disabled={subscribeLoading}>
              {subscribeLoading ? (
                <>
                  <span className="newsletter-spinner"></span> Subscribing...
                </>
              ) : (
                <>
                  <FaPaperPlane /> Subscribe
                </>
              )}
            </button>
          </form>
          {subscribeStatus && (
            <div className={`newsletter-status newsletter-${subscribeStatus === 'success' ? 'success' : 'error'}`}>
              {subscribeStatus === 'success'
                ? '🎉 Successfully subscribed! Check your inbox for a welcome email.'
                : subscribeStatus
              }
            </div>
          )}
        </div>
      </div>

      <div className="footer-content">
        <div className="footer-brand">
          <div className="footer-logo">
            <img src={logo} alt="TrainingProtec" className="footer-logo-img" />
            <span className="footer-logo-text">TrainingProtec</span>
          </div>
          <p>
            TrainingProtec is a global e-learning and certification training provider. 
            We help professionals and organizations worldwide acquire in-demand skills 
            through live instructor-led courses, hands-on projects, and certification support.
          </p>
          <div className="footer-contact-info">
            <div><FaEnvelope /> contact@trainingprotec.com</div>
          </div>
          <div className="footer-social">
            <a href="#" className="social-link" aria-label="Facebook"><FaFacebook /></a>
            <a href="#" className="social-link" aria-label="Twitter"><FaTwitter /></a>
            <a href="#" className="social-link" aria-label="Instagram"><FaInstagram /></a>
            <a href="#" className="social-link" aria-label="LinkedIn"><FaLinkedinIn /></a>
            <a href="#" className="social-link" aria-label="YouTube"><FaYoutube /></a>
          </div>
        </div>

        <div className="footer-links">
          <h4>Popular Courses</h4>
          <ul>
            <li><Link to="/courses/data-science-ai">Data Science & AI</Link></li>
            <li><Link to="/courses/cloud-computing-devops">Cloud Computing & DevOps</Link></li>
            <li><Link to="/courses/cyber-security">Cyber Security</Link></li>
            <li><Link to="/courses/web-development">Full Stack Web Development</Link></li>
            <li><Link to="/courses/digital-marketing">Digital Marketing</Link></li>
            <li><Link to="/courses/business-analytics">Business Analytics</Link></li>
            <li><Link to="/courses/ui-ux-design">UI/UX Design</Link></li>
            <li><Link to="/courses/mobile-app-development">Mobile App Development</Link></li>
          </ul>
        </div>

        <div className="footer-links">
          <h4>Resources</h4>
          <ul>
            <li><a href="/#blog" onClick={(e) => scrollToSection(e, 'blog')}>Blog & Articles</a></li>
            <li><a href="/#about" onClick={(e) => scrollToSection(e, 'about')}>About TrainingProtec</a></li>
            <li><a href="/#testimonials" onClick={(e) => scrollToSection(e, 'testimonials')}>Success Stories</a></li>
            <li><a href="/#features" onClick={(e) => scrollToSection(e, 'features')}>Why TrainingProtec</a></li>
            <li><a href="/#contact" onClick={(e) => scrollToSection(e, 'contact')}>Free Career Counselling</a></li>
            <li><a href="/#contact" onClick={(e) => scrollToSection(e, 'contact')}>Corporate Training</a></li>
          </ul>
        </div>

        <div className="footer-links">
          <h4>Company</h4>
          <ul>
            <li><a href="/#about" onClick={(e) => scrollToSection(e, 'about')}>About Us</a></li>
            <li><a href="/#contact" onClick={(e) => scrollToSection(e, 'contact')}>Contact Us</a></li>
            <li><Link to="/enquiry/instructor">Become an Instructor</Link></li>
            <li><Link to="/enquiry/partnership">Partnerships</Link></li>
            <li><Link to="/enquiry/career">Careers at TrainingProtec</Link></li>
            <li><Link to="/sitemap">Sitemap</Link></li>
          </ul>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; 2020 TrainingProtec. All rights reserved. | Global Professional Training Platform</p>
        <div className="footer-bottom-links">
          <Link to="/privacy">Privacy Policy</Link>
          <Link to="/terms">Terms and Conditions</Link>
          <Link to="/refund">Refund Policy</Link>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
