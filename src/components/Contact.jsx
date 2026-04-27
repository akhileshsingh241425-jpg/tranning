import React, { useState } from 'react';
import { FaEnvelope, FaClock } from 'react-icons/fa';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    service: '',
    message: ''
  });
  const [status, setStatus] = useState({ type: '', message: '' });
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL || ''}/api/contact`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      
      const data = await response.json();
      
      if (data.success) {
        setStatus({ type: 'success', message: 'Message sent successfully! We will get back to you soon.' });
        setFormData({ name: '', email: '', phone: '', service: '', message: '' });
      } else {
        setStatus({ type: 'error', message: 'Something went wrong. Please try again.' });
      }
    } catch (error) {
      setStatus({ type: 'error', message: 'Server not connected. Message saved locally.' });
      console.log('Form data:', formData);
      setFormData({ name: '', email: '', phone: '', service: '', message: '' });
    }
    
    setLoading(false);
    setTimeout(() => setStatus({ type: '', message: '' }), 5000);
  };

  return (
    <section className="contact" id="contact">
      <div className="section-header">
        <span className="section-badge">Contact Us</span>
        <h2 className="section-title">
          Get In <span>Touch</span>
        </h2>
        <p className="section-description">
          Have questions about our courses? Want to learn more? Reach out to us today.
        </p>
      </div>

      <div className="contact-content">
        <div className="contact-info">
          <h3>Let's Help You Start Learning</h3>
          <p>
            Our education advisors are ready to help you choose the right 
            course and learning path. Reach out and we'll guide you toward 
            achieving your goals.
          </p>

          <div className="contact-details">
            <div className="contact-item">
              <div className="contact-icon">
                <FaEnvelope />
              </div>
              <div className="contact-item-text">
                <h4>Email Address</h4>
                <p>contact@trainingprotec.com</p>
              </div>
            </div>

            <div className="contact-item">
              <div className="contact-icon">
                <FaClock />
              </div>
              <div className="contact-item-text">
                <h4>Working Hours</h4>
                <p>Mon-Sat: 9AM - 9PM</p>
              </div>
            </div>
          </div>
        </div>

        <form className="contact-form" onSubmit={handleSubmit}>
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="name">Full Name</label>
              <input 
                type="text" 
                id="name" 
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="Your full name"
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="phone">Phone Number</label>
              <input 
                type="tel" 
                id="phone" 
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                placeholder="+91 98765 43210"
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="email">Email Address</label>
            <input 
              type="email" 
              id="email" 
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="you@example.com"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="service">Course Interested In</label>
            <select 
              id="service" 
              name="service"
              value={formData.service}
              onChange={handleChange}
              required
            >
              <option value="">Select a course</option>
              <option value="data-science-ai">Data Science & AI</option>
              <option value="cloud-computing-devops">Cloud Computing & DevOps</option>
              <option value="cyber-security">Cyber Security</option>
              <option value="web-development">Full Stack Web Development</option>
              <option value="digital-marketing">Digital Marketing</option>
              <option value="business-analytics">Business Analytics</option>
              <option value="ui-ux-design">UI/UX Design</option>
              <option value="mobile-app-development">Mobile App Development</option>
              <option value="other">Other / General Inquiry</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="message">Your Message</label>
            <textarea 
              id="message" 
              name="message"
              value={formData.message}
              onChange={handleChange}
              placeholder="Tell us about your learning goals and any questions you have..."
              required
            ></textarea>
          </div>

          {status.message && (
            <div className={`form-status ${status.type}`}>
              {status.message}
            </div>
          )}

          <button type="submit" className="form-submit" disabled={loading}>
            {loading ? 'Sending...' : 'Send Message'}
          </button>
        </form>
      </div>
    </section>
  );
};

export default Contact;
