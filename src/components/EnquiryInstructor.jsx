import React, { useState } from 'react';
import { FaEnvelope, FaClock, FaChalkboardTeacher, FaLinkedin } from 'react-icons/fa';

const EnquiryInstructor = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    expertise: '',
    experience: '',
    linkedin: '',
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
      service: 'Become an Instructor',
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
        setStatus({ type: 'success', message: 'Application submitted successfully! We will review your profile and get back to you soon.' });
        setFormData({ name: '', email: '', phone: '', expertise: '', experience: '', linkedin: '', message: '' });
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
    <section className="contact" id="enquiry-instructor">
      <div className="section-header">
        <span className="section-badge">Become an Instructor</span>
        <h2 className="section-title">
          Share Your <span>Expertise</span>
        </h2>
        <p className="section-description">
          Join our team of industry experts and help shape the next generation of tech professionals. 
          Share your knowledge, grow your personal brand, and earn while you teach.
        </p>
      </div>

      <div className="contact-content">
        <div className="contact-info">
          <h3>Why Teach at TrainingProtec?</h3>
          <p>
            We're always looking for passionate professionals who want to make a difference. 
            As a TrainingProtec instructor, you'll reach thousands of learners worldwide, 
            get access to our cutting-edge platform, and join a community of elite educators.
          </p>

          <div className="contact-details">
            <div className="contact-item">
              <div className="contact-icon">
                <FaChalkboardTeacher />
              </div>
              <div className="contact-item-text">
                <h4>Flexible Schedule</h4>
                <p>Teach at your own pace and convenience</p>
              </div>
            </div>

            <div className="contact-item">
              <div className="contact-icon">
                <FaLinkedin />
              </div>
              <div className="contact-item-text">
                <h4>Grow Your Brand</h4>
                <p>Build your professional reputation and reach</p>
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
              <label htmlFor="expertise">Area of Expertise</label>
              <select 
                id="expertise" 
                name="expertise"
                value={formData.expertise}
                onChange={handleChange}
                required
              >
                <option value="">Select your expertise</option>
                <option value="data-science-ai">Data Science & AI</option>
                <option value="cloud-computing">Cloud Computing & DevOps</option>
                <option value="cyber-security">Cyber Security</option>
                <option value="web-development">Full Stack Web Development</option>
                <option value="digital-marketing">Digital Marketing</option>
                <option value="business-analytics">Business Analytics</option>
                <option value="ui-ux-design">UI/UX Design</option>
                <option value="mobile-development">Mobile App Development</option>
                <option value="other">Other</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="experience">Teaching Experience</label>
              <select 
                id="experience" 
                name="experience"
                value={formData.experience}
                onChange={handleChange}
                required
              >
                <option value="">Select experience level</option>
                <option value="no-experience">No prior teaching experience</option>
                <option value="1-2-years">1-2 years</option>
                <option value="3-5-years">3-5 years</option>
                <option value="5-plus-years">5+ years</option>
              </select>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="linkedin">LinkedIn Profile URL</label>
            <input 
              type="url" 
              id="linkedin" 
              name="linkedin"
              value={formData.linkedin}
              onChange={handleChange}
              placeholder="https://linkedin.com/in/yourprofile"
            />
          </div>

          <div className="form-group">
            <label htmlFor="message">Tell Us About Yourself</label>
            <textarea 
              id="message" 
              name="message"
              value={formData.message}
              onChange={handleChange}
              placeholder="Share your industry experience, courses you'd like to teach, and why you want to join TrainingProtec..."
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

export default EnquiryInstructor;
