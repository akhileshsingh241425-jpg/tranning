import React from 'react';
import { FaCheckCircle, FaArrowRight, FaAward, FaHandshake, FaGlobeAsia, FaBullseye, FaEye, FaRocket, FaUsers, FaLaptopCode, FaBriefcase, FaChalkboardTeacher, FaCertificate, FaProjectDiagram, FaHeadset } from 'react-icons/fa';
import logo from '../assets/fevicon.png';
import teamImg from '../assets/images/about/team.jpg';

const whyChooseUs = [
  { icon: <FaChalkboardTeacher />, text: "Industry-Expert Trainers" },
  { icon: <FaProjectDiagram />, text: "Practical & Job-Oriented Learning" },
  { icon: <FaRocket />, text: "Flexible Batches (Weekday/Weekend)" },
  { icon: <FaHeadset />, text: "24/7 Learner Support" },
  { icon: <FaCertificate />, text: "Global Certification Preparation" },
  { icon: <FaUsers />, text: "Personalized Training Options" },
];

const whatWeDo = [
  "Certification Training Programs (150+ certifications)",
  "Corporate Training & Workforce Upskilling",
  "One-to-One Customized Learning",
  "Exam Preparation & Assistance",
  "Live Project Support",
  "Job Interview Preparation"
];

const ourApproach = [
  "Instructor-led live sessions",
  "One-on-one personalized training",
  "Hands-on projects & real-time scenarios",
  "Certification exam support",
  "Career guidance and interview preparation"
];

const About = () => {
  return (
    <section className="about" id="about">
      {/* Main About Hero */}
      <div className="about-hero-header">
        <img src={logo} alt="TrainingProtec" className="about-hero-logo" />
        <span className="section-badge">About TrainingProtec</span>
        <h2 className="about-hero-title">
          Transforming Careers Through <span>Industry-Focused</span> Certification Training
        </h2>
        <p className="about-hero-subtitle">
          Empowering professionals and organizations worldwide since day one with globally recognized certifications.
        </p>
      </div>

      {/* Content Grid */}
      <div className="about-content">
        <div className="about-image">
          <img 
            src={teamImg} 
            alt="TrainingProtec Learning" 
          />
          <div className="about-stats">
            <div className="stat-box">
              <h3>150+</h3>
              <p>Certifications</p>
            </div>
            <div className="stat-box">
              <h3>150+</h3>
              <p>Countries</p>
            </div>
          </div>
        </div>

        <div className="about-text">
          <p>
            At TrainingProtec, we are committed to transforming careers through high-quality, 
            industry-focused certification training. Since our inception, we have empowered 
            professionals and organizations worldwide with the skills, knowledge, and confidence 
            needed to thrive in today's rapidly evolving digital landscape.
          </p>
          <p>
            We specialize in delivering globally recognized IT and management certification training 
            across domains such as Cybersecurity, Cloud Computing, Project Management, Data Science, 
            and Digital Technologies—fields where demand for skilled professionals continues to grow 
            at an unprecedented pace.
          </p>
          
          <div className="about-badges">
            <div className="about-badge-item">
              <FaGlobeAsia className="badge-icon" />
              <span>150+ Countries Served</span>
            </div>
            <div className="about-badge-item">
              <FaAward className="badge-icon" />
              <span>150+ Certifications</span>
            </div>
            <div className="about-badge-item">
              <FaHandshake className="badge-icon" />
              <span>Trusted Globally</span>
            </div>
          </div>

          <a href="#courses" style={{textDecoration:'none'}}>
            <button className="btn-primary" style={{ marginTop: '2rem' }}>
              Explore Courses <FaArrowRight />
            </button>
          </a>
        </div>
      </div>

      {/* Who We Are + Our Journey - Side by Side Cards */}
      <div className="about-cards-row">
        <div className="about-info-card">
          <div className="about-info-card-icon"><FaUsers /></div>
          <h3>Who We Are</h3>
          <p>
            TrainingProtec is a global e-learning and certification training provider based in India, 
            serving professionals and enterprises across 150+ countries. Our learning ecosystem is built 
            around practical knowledge, real-world application, and career outcomes.
          </p>
          <div className="about-features">
            {ourApproach.map((item, index) => (
              <div className="about-feature" key={index}>
                <FaCheckCircle />
                <span>{item}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="about-info-card">
          <div className="about-info-card-icon"><FaRocket /></div>
          <h3>Our Journey</h3>
          <p>
            TrainingProtec started with a vision to bridge the gap between industry demand and skilled 
            professionals. From a small team, we have grown into a trusted training provider supporting 
            thousands of learners globally.
          </p>
          <div className="about-features">
            {whatWeDo.map((item, index) => (
              <div className="about-feature" key={index}>
                <FaCheckCircle />
                <span>{item}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Mission & Vision */}
      <div className="about-mission-vision">
        <div className="mission-card">
          <FaBullseye className="mv-icon" />
          <h3>Our Mission</h3>
          <p>
            To empower individuals and organizations with industry-relevant skills and certifications 
            that drive career growth, innovation, and success.
          </p>
        </div>
        <div className="mission-card">
          <FaEye className="mv-icon" />
          <h3>Our Vision</h3>
          <p>
            To become a globally trusted leader in professional training by delivering high-impact 
            learning experiences that shape the future workforce.
          </p>
        </div>
      </div>

      {/* Why Choose Us - Card Grid */}
      <div className="about-section about-why-section">
        <div className="about-section-header" style={{justifyContent: 'center'}}>
          <FaBriefcase className="section-icon" />
          <h2>Why Choose TrainingProtec</h2>
        </div>
        <div className="about-why-grid">
          {whyChooseUs.map((item, index) => (
            <div className="about-why-card" key={index}>
              <div className="about-why-card-icon">{item.icon}</div>
              <span>{item.text}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default About;
