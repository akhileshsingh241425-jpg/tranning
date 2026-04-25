import React, { useState } from 'react';
import { Link } from 'react-router-dom';
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
  const currentYear = new Date().getFullYear();
  const [email, setEmail] = useState('');

  const handleNewsletterSubmit = (e) => {
    e.preventDefault();
    if (email) {
      alert('Thank you for subscribing!');
      setEmail('');
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
            />
            <button type="submit"><FaPaperPlane /> Subscribe</button>
          </form>
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
            <div><FaEnvelope /> support@trainingprotec.com</div>
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
            <li><a href="#courses">Data Science & AI</a></li>
            <li><a href="#courses">Cloud Computing & DevOps</a></li>
            <li><a href="#courses">Cyber Security</a></li>
            <li><a href="#courses">Full Stack Web Development</a></li>
            <li><a href="#courses">Digital Marketing</a></li>
            <li><a href="#courses">Business Analytics</a></li>
            <li><a href="#courses">UI/UX Design</a></li>
            <li><a href="#courses">Mobile App Development</a></li>
          </ul>
        </div>

        <div className="footer-links">
          <h4>Resources</h4>
          <ul>
            <li><a href="#blog">Blog & Articles</a></li>
            <li><a href="#about">About TrainingProtec</a></li>
            <li><a href="#testimonials">Success Stories</a></li>
            <li><a href="#features">Why TrainingProtec</a></li>
            <li><a href="#contact">Free Career Counselling</a></li>
            <li><a href="#contact">Corporate Training</a></li>
          </ul>
        </div>

        <div className="footer-links">
          <h4>Interview Prep</h4>
          <ul>
            <li><a href="#blog">Python Interview Questions</a></li>
            <li><a href="#blog">SQL Interview Questions</a></li>
            <li><a href="#blog">React Interview Questions</a></li>
            <li><a href="#blog">Data Science Interview Prep</a></li>
            <li><a href="#blog">AWS Interview Questions</a></li>
            <li><a href="#blog">DevOps Interview Questions</a></li>
          </ul>
        </div>

        <div className="footer-links">
          <h4>Company</h4>
          <ul>
            <li><a href="#about">About Us</a></li>
            <li><a href="#contact">Contact Us</a></li>
            <li><a href="#contact">Become an Instructor</a></li>
            <li><a href="#contact">Partnerships</a></li>
            <li><a href="#contact">Careers at TrainingProtec</a></li>
            <li><a href="#">Sitemap</a></li>
          </ul>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; {currentYear} TrainingProtec. All rights reserved. | Global Professional Training Platform</p>
        <div className="footer-bottom-links">
          <Link to="/terms">Privacy Policy</Link>
          <Link to="/terms">Terms of Service</Link>
          <a href="#">Refund Policy</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
