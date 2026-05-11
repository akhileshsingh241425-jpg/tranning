import React, { useState } from 'react';
import { FaEnvelope, FaClock, FaRocket, FaUsers } from 'react-icons/fa';

const EnquiryCareer = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    position: '',
    experience: '',
    resumeLink: '',
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
      service: 'Career Enquiry',
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
        setStatus({ type: 'success', message: 'Career application submitted successfully! Our HR team will review your profile and get back to you.' });
        setFormData({ name: '', email: '', phone: '', position: '', experience: '', resumeLink: '', message: '' });
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
    <section className="contact" id="enquiry-career">
      <div className="section-header">
        <span className="section-badge">Careers</span>
        <h2 className="section-title">
          Career at <span>TrainingProtec</span>
        </h2>
        <p className="section-description">
          Join our mission to transform tech education. We're building a team of passionate 
          individuals who want to make a real impact on how people learn and grow.
        </p>
      </div>

      <div className="contact-content">
        <div className="contact-info">
          <h3>Why Work With Us?</h3>
          <p>
            At TrainingProtec, we believe in innovation, collaboration, and continuous learning. 
            We offer a dynamic work environment, competitive compensation, and the opportunity 
            to shape the future of online education.
          </p>

          <div className="contact-details">
            <div className="contact-item">
              <div className="contact-icon">
                <FaRocket />
              </div>
              <div className="contact-item-text">
                <h4>Growth Opportunities</h4>
                <p>Fast-track your career with us</p>
              </div>
            </div>

            <div className="contact-item">
              <div className="contact-icon">
                <FaUsers />
              </div>
              <div className="contact-item-text">
                <h4>Great Team Culture</h4>
                <p>Work with passionate, like-minded people</p>
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

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="position">Position Interested In</label>
              <select 
                id="position" 
                name="position"
                value={formData.position}
                onChange={handleChange}
                required
              >
                <option value="">Select a position</option>
                <option value="instructor">Instructor / Trainer</option>
                <option value="content-developer">Content Developer</option>
                <option value="sales-marketing">Sales & Marketing</option>
                <option value="software-engineer">Software Engineer</option>
                <option value="student-counsellor">Student Counsellor</option>
                <option value="operations">Operations</option>
                <option value="other">Other</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="experience">Years of Experience</label>
              <select 
                id="experience" 
                name="experience"
                value={formData.experience}
                onChange={handleChange}
                required
              >
                <option value="">Select experience</option>
                <option value="fresher">Fresher (0-1 years)</option>
                <option value="1-3-years">1-3 years</option>
                <option value="3-5-years">3-5 years</option>
                <option value="5-plus-years">5+ years</option>
              </select>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="resumeLink">Resume / Portfolio Link</label>
            <input 
              type="url" 
              id="resumeLink" 
              name="resumeLink"
              value={formData.resumeLink}
              onChange={handleChange}
              placeholder="https://drive.google.com/your-resume or LinkedIn profile"
            />
          </div>

          <div className="form-group">
            <label htmlFor="message">Cover Note</label>
            <textarea 
              id="message" 
              name="message"
              value={formData.message}
              onChange={handleChange}
              placeholder="Tell us why you'd like to join TrainingProtec and what makes you a great fit..."
              required
            ></textarea>
          </div>

          {status.message && (
            <div className={`form-status ${status.type}`}>
              {status.message}
            </div>
          )}

          <button type="submit" className="form-submit" disabled={loading}>
            {loading ? 'Submitting...' : 'Submit Application'}
          </button>
        </form>
      </div>
    </section>
  );
};

export default EnquiryCareer;
