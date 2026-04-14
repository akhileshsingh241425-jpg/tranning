import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { FaArrowLeft, FaArrowRight, FaCheckCircle, FaQuoteLeft, FaChevronDown, FaChevronUp, FaPhone, FaEnvelope } from 'react-icons/fa';
import servicesDetailData from './serviceData';

const ServiceDetail = () => {
  const { slug } = useParams();
  const [activeAccordion, setActiveAccordion] = useState(null);
  const service = servicesDetailData.find(s => s.slug === slug);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [slug]);

  if (!service) {
    return (
      <div className="service-detail-not-found">
        <h2>Service Not Found</h2>
        <p>The service you're looking for doesn't exist.</p>
        <Link to="/" className="btn-back-home">
          <FaArrowLeft /> Back to Home
        </Link>
      </div>
    );
  }

  const ServiceIcon = service.icon;
  const currentIndex = servicesDetailData.findIndex(s => s.slug === slug);
  const prevService = servicesDetailData[(currentIndex - 1 + servicesDetailData.length) % servicesDetailData.length];
  const nextService = servicesDetailData[(currentIndex + 1) % servicesDetailData.length];

  const toggleAccordion = (index) => {
    setActiveAccordion(activeAccordion === index ? null : index);
  };

  return (
    <div className="service-detail-page">
      {/* Hero Section */}
      <section className="sd-hero">
        <div className="sd-hero-bg">
          <img src={service.heroImage} alt={service.title} />
          <div className="sd-hero-overlay"></div>
        </div>
        <div className="sd-hero-content">
          <Link to="/#services" className="sd-back-link">
            <FaArrowLeft /> Back to Services
          </Link>
          <div className="sd-hero-icon">
            <ServiceIcon />
          </div>
          <h1 className="sd-hero-title">{service.title}</h1>
          <p className="sd-hero-tagline">{service.tagline}</p>
          <div className="sd-hero-stats">
            {service.stats.map((stat, index) => (
              <div key={index} className="sd-stat">
                <span className="sd-stat-number">{stat.number}</span>
                <span className="sd-stat-label">{stat.label}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Overview Section */}
      <section className="sd-overview">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Overview</span>
            <h2>About This Service</h2>
          </div>
          <div className="sd-overview-content">
            <p className="sd-overview-text">{service.overview}</p>
            <div className="sd-benefits">
              <h3>Key Benefits</h3>
              <ul className="sd-benefits-list">
                {service.keyBenefits.map((benefit, index) => (
                  <li key={index}>
                    <FaCheckCircle className="sd-check-icon" />
                    <span>{benefit}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Sub-Services Section */}
      <section className="sd-sub-services">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">What We Offer</span>
            <h2>Detailed Service Breakdown</h2>
            <p>Comprehensive solutions tailored to your specific needs</p>
          </div>
          <div className="sd-sub-grid">
            {service.subServices.map((sub, index) => {
              const SubIcon = sub.icon;
              return (
                <div key={index} className="sd-sub-card">
                  <div className="sd-sub-icon">
                    <SubIcon />
                  </div>
                  <h3>{sub.title}</h3>
                  <p>{sub.description}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Process Section */}
      <section className="sd-process">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Our Process</span>
            <h2>How We Work</h2>
            <p>A proven methodology that delivers results</p>
          </div>
          <div className="sd-process-timeline">
            {service.process.map((step, index) => (
              <div key={index} className="sd-process-step">
                <div className="sd-step-number">{step.step}</div>
                <div className="sd-step-content">
                  <h3>{step.title}</h3>
                  <p>{step.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Technologies Section */}
      <section className="sd-technologies">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Technologies</span>
            <h2>Tools & Technologies We Use</h2>
          </div>
          <div className="sd-tech-grid">
            {service.technologies.map((tech, index) => (
              <div key={index} className="sd-tech-tag">
                {tech}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="sd-faq">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">FAQ</span>
            <h2>Frequently Asked Questions</h2>
          </div>
          <div className="sd-faq-list">
            {service.faq.map((item, index) => (
              <div 
                key={index} 
                className={`sd-faq-item ${activeAccordion === index ? 'active' : ''}`}
              >
                <button 
                  className="sd-faq-question" 
                  onClick={() => toggleAccordion(index)}
                >
                  <span>{item.question}</span>
                  {activeAccordion === index ? <FaChevronUp /> : <FaChevronDown />}
                </button>
                <div className={`sd-faq-answer ${activeAccordion === index ? 'open' : ''}`}>
                  <p>{item.answer}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="sd-cta">
        <div className="sd-container">
          <div className="sd-cta-content">
            <FaQuoteLeft className="sd-cta-quote" />
            <h2>Ready to Get Started?</h2>
            <p>Let's discuss how our {service.title.toLowerCase()} can help transform your business. Get in touch with our experts today.</p>
            <div className="sd-cta-buttons">
              <a href="/#contact" className="sd-btn-primary">
                <FaEnvelope /> Contact Us
              </a>
              <a href="tel:+1234567890" className="sd-btn-secondary">
                <FaPhone /> Call Now
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Navigation Between Services */}
      <section className="sd-navigation">
        <Link to={`/services/${prevService.slug}`} className="sd-nav-link prev">
          <FaArrowLeft />
          <div>
            <span className="sd-nav-label">Previous Service</span>
            <span className="sd-nav-title">{prevService.title}</span>
          </div>
        </Link>
        <Link to={`/services/${nextService.slug}`} className="sd-nav-link next">
          <div>
            <span className="sd-nav-label">Next Service</span>
            <span className="sd-nav-title">{nextService.title}</span>
          </div>
          <FaArrowRight />
        </Link>
      </section>
    </div>
  );
};

export default ServiceDetail;
