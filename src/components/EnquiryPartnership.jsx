import React, { useState } from 'react';
import { FaEnvelope, FaClock, FaHandshake, FaGlobe } from 'react-icons/fa';

const EnquiryPartnership = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    organization: '',
    partnershipType: '',
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
    
    const payload = {
      ...formData,
      service: 'Partnership Enquiry',
    };

    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL || ''}/api/contact`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });
      
      const data = await response.json();
      
      if (data.success) {
        setStatus({ type: 'success', message: 'Partnership enquiry submitted successfully! Our team will reach out to you within 24 hours.' });
        setFormData({ name: '', email: '', phone: '', organization: '', partnershipType: '', message: '' });
      } else {
        setStatus({ type: 'error', message: 'Something went wrong. Please try again.' });
      }
    } catch (error) {
      setStatus({ type: 'error', message: 'Server not connected. Please try again later.' });
    }
    
    setLoading(false);
    setTimeout(() => setStatus({ type: '', message: '' }), 5000);
  };

  return (
    <section className="contact" id="enquiry-partnership">
      <div className="section-header">
        <span className="section-badge">Partnerships</span>
        <h2 className="section-title">
          Partner With <span>TrainingProtec</span>
        </h2>
        <p className="section-description">
          Collaborate with us to create impactful learning experiences. Whether you're a university, 
          corporate organization, or tech company — let's build something great together.
        </p>
      </div>

      <div className="contact-content">
        <div className="contact-info">
          <h3>Partnership Opportunities</h3>
          <p>
            TrainingProtec partners with leading organizations worldwide to deliver cutting-edge 
            training solutions. From co-branded courses to enterprise training programs, 
            we offer flexible partnership models tailored to your needs.
          </p>

          <div className="contact-details">
            <div className="contact-item">
              <div className="contact-icon">
                <FaHandshake />
              </div>
              <div className="contact-item-text">
                <h4>Co-Branded Courses</h4>
                <p>Create courses together with your brand</p>
              </div>
            </div>

            <div className="contact-item">
              <div className="contact-icon">
                <FaGlobe />
              </div>
              <div className="contact-item-text">
                <h4>Global Reach</h4>
                <p>Access our network of 80,000+ learners</p>
              </div>
            </div>

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
            <label htmlFor="organization">Organization / Company Name</label>
            <input 
              type="text" 
              id="organization" 
              name="organization"
              value={formData.organization}
              onChange={handleChange}
              placeholder="Your company or organization name"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="partnershipType">Type of Partnership</label>
            <select 
              id="partnershipType" 
              name="partnershipType"
              value={formData.partnershipType}
              onChange={handleChange}
              required
            >
              <option value="">Select partnership type</option>
              <option value="corporate-training">Corporate Training</option>
              <option value="co-branded-courses">Co-Branded Courses</option>
              <option value="university-partnership">University / Academic Partnership</option>
              <option value="reseller">Reseller / Affiliate Partnership</option>
              <option value="technology">Technology Partnership</option>
              <option value="other">Other</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="message">Partnership Details</label>
            <textarea 
              id="message" 
              name="message"
              value={formData.message}
              onChange={handleChange}
              placeholder="Tell us about your organization and what kind of partnership you're interested in..."
              required
            ></textarea>
          </div>

          {status.message && (
            <div className={`form-status ${status.type}`}>
              {status.message}
            </div>
          )}

          <button type="submit" className="form-submit" disabled={loading}>
            {loading ? 'Submitting...' : 'Submit Enquiry'}
          </button>
        </form>
      </div>
    </section>
  );
};

export default EnquiryPartnership;
