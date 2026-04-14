import React from 'react';
import { Link } from 'react-router-dom';
import { 
  FaShieldAlt, 
  FaClipboardCheck, 
  FaCode, 
  FaGraduationCap, 
  FaBug, 
  FaBullhorn,
  FaArrowRight
} from 'react-icons/fa';
import socMonitoring from '../assets/images/services/soc-monitoring.jpg';
import penetrationTesting from '../assets/images/services/penetration-testing.jpg';
import cloudSecurity from '../assets/images/services/cloud-security.jpg';
import securityConsulting from '../assets/images/services/security-consulting.jpg';
import incidentResponse from '../assets/images/services/incident-response.jpg';
import securityTraining from '../assets/images/services/security-training.jpg';

const services = [
  {
    icon: <FaShieldAlt />,
    title: "Cybersecurity Services",
    description: "Pinpoint vulnerabilities before attackers do with thorough penetration testing.",
    image: socMonitoring,
    slug: "cybersecurity-services"
  },
  {
    icon: <FaClipboardCheck />,
    title: "Compliance & Regulatory Audits",
    description: "Navigate complex regulations smoothly with our detailed audit services.",
    image: penetrationTesting,
    slug: "compliance-regulatory-audits"
  },
  {
    icon: <FaCode />,
    title: "Software & Web Development",
    description: "Build secure, reliable software tailored to your business needs.",
    image: cloudSecurity,
    slug: "software-web-development"
  },
  {
    icon: <FaGraduationCap />,
    title: "Training & Skill Development",
    description: "Build future-ready talent through hands-on, industry-aligned training and certification programs.",
    image: securityConsulting,
    slug: "training-skill-development"
  },
  {
    icon: <FaBug />,
    title: "Quality & Assurance Testing",
    description: "Deliver flawless performance with rigorous testing that ensures reliability, security, and scalability.",
    image: incidentResponse,
    slug: "quality-assurance-testing"
  },
  {
    icon: <FaBullhorn />,
    title: "Digital Marketing",
    description: "Accelerate business growth with strategic, data-driven digital marketing solutions that deliver measurable results.",
    image: securityTraining,
    slug: "digital-marketing"
  }
];

const Services = () => {
  return (
    <section className="services" id="services">
      <div className="section-header">
        <span className="section-badge">Our Services</span>
        <h2 className="section-title">
          What We <span>Offer</span>
        </h2>
        <p className="section-description">
          Comprehensive cybersecurity, development, and digital solutions 
          to protect and grow your business.
        </p>
      </div>

      <div className="services-grid">
        {services.map((service, index) => (
          <div className="service-card" key={index}>
            <div className="service-image">
              <img src={service.image} alt={service.title} />
            </div>
            <div className="service-content">
              <div className="service-icon">
                {service.icon}
              </div>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
                <Link to={`/services/${service.slug}`} className="service-link">
                  Learn More <FaArrowRight />
                </Link>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Services;
