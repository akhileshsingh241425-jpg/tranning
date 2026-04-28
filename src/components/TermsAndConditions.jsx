import React, { useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaArrowLeft, FaShieldAlt, FaLock, FaUndo, FaEnvelope, FaGlobe } from 'react-icons/fa';
import SEO from './SEO';

const termsSections = [
  {
    id: 1,
    title: "Introduction",
    content: "Welcome to Training Protec (\u201cwe\u201d, \u201cour\u201d, or \u201cus\u201d). This document outlines the Terms & Conditions, Privacy Policy, and Refund Policy governing your use of our website and services. By accessing our website or enrolling in any of our training programs, you agree to be bound by the terms stated in this policy."
  },
  {
    id: 2,
    title: "Services Offered",
    content: "Training Protec provides professional training services in IT and management certifications, including instructor-led group sessions, one-to-one training, exam preparation, project support, and job assistance services. The scope and delivery of services may vary depending on the course or package selected."
  },
  {
    id: 3,
    title: "User Responsibilities",
    content: "Users agree to provide accurate and complete information during registration or communication and to use our services only for lawful purposes. You are responsible for maintaining the confidentiality of your login credentials and agree not to share access to training materials or accounts. Any unauthorized use, duplication, or distribution of course content is strictly prohibited."
  },
  {
    id: 4,
    title: "Payments and Pricing",
    content: "All fees must be paid in full before access to any course or service is granted. Pricing for courses and services may change at any time without prior notice. The fees listed on our website or communicated by our team apply only to training services and do not include additional costs such as certification exam fees, third-party tools, or external services unless explicitly mentioned."
  },
  {
    id: 5,
    title: "Intellectual Property Rights",
    content: "All materials provided by Training Protec, including course content, videos, documents, branding, and resources, are the exclusive property of the company. These materials are intended solely for personal use by enrolled participants and may not be copied, modified, distributed, or resold without prior written consent."
  },
  {
    id: 6,
    title: "Service Modifications",
    content: "Training Protec reserves the right to modify course content, schedules, trainers, or delivery methods at any time to maintain quality and operational efficiency. In certain situations, batches may be rescheduled or canceled, and suitable alternatives will be offered where possible."
  },
  {
    id: 7,
    title: "Limitation of Liability",
    content: "Training Protec shall not be held responsible for any indirect, incidental, or consequential damages arising from the use of our services. We do not guarantee job placement or career outcomes, as these depend on individual performance, market conditions, and external factors. Additionally, we are not liable for technical issues caused by internet disruptions or third-party platforms."
  },
  {
    id: 8,
    title: "Termination of Services",
    content: "We reserve the right to suspend or terminate access to our services if a user violates these terms, engages in misconduct, or is found to be misusing our platform or resources."
  },
  {
    id: 9,
    title: "Governing Law",
    content: "This agreement shall be governed by and interpreted in accordance with the laws of India, and any disputes shall be subject to the jurisdiction of the appropriate courts."
  }
];

const privacySections = [
  {
    id: 10,
    title: "Information We Collect",
    content: "We may collect both non-personal and personal information when you interact with our website. Non-personal information includes technical data such as IP address, browser type, device information, and browsing behavior. Personal information is collected when you voluntarily provide it, such as during registration, inquiry, or payment, and may include your name, email address, phone number, and billing details."
  },
  {
    id: 11,
    title: "Use of Information",
    content: "The information collected is used to deliver training services, process payments, communicate updates, provide customer support, improve our website and offerings, and send promotional content where consent has been given. We ensure that the use of your data is relevant and limited to necessary business purposes."
  },
  {
    id: 12,
    title: "Sharing of Information",
    content: "Training Protec does not sell or rent your personal information to third parties. However, your data may be shared with trainers, service providers, payment processors, or legal authorities when required for service delivery or compliance with applicable laws. All such parties are expected to maintain confidentiality and data security."
  },
  {
    id: 13,
    title: "Data Protection",
    content: "We take appropriate measures to protect your personal information from unauthorized access, misuse, or disclosure. While we strive to use commercially acceptable methods to safeguard your data, no system can guarantee complete security."
  },
  {
    id: 15,
    title: "Third-Party Services",
    content: "Our website may include links to third-party websites or use external tools and platforms. Training Protec is not responsible for the privacy practices, policies, or performance of these third-party services, and users are encouraged to review their respective terms."
  },
  {
    id: 16,
    title: "Business Transfers",
    content: "In the event of a merger, acquisition, or sale of company assets, user information may be transferred as part of the business transaction. Such transfers will continue to be governed by the principles outlined in this policy."
  },
  {
    id: 17,
    title: "User Rights",
    content: "Users have the right to access, update, or request deletion of their personal information, as well as the right to opt out of marketing communications. Requests can be made by contacting us through the provided contact details."
  }
];

const refundSections = [
  {
    id: 18,
    title: "Refund Policy Overview",
    content: "Training Protec aims to maintain transparency and fairness in its refund practices while ensuring commitment to service delivery."
  },
  {
    id: 19,
    title: "Refund Before Course Start",
    content: "Users may request a full refund if cancellation is made at least 48 hours prior to the scheduled course start time. Any applicable transaction or processing charges may be deducted from the refund amount."
  },
  {
    id: 20,
    title: "Refund After Course Start",
    content: "Once the training has commenced, no refunds will be issued. However, depending on the situation, users may be offered alternatives such as batch rescheduling or course credit for future use."
  },
  {
    id: 21,
    title: "Demo Session Clause",
    content: "If a demo session is provided and the user is not satisfied, they may request a trainer replacement or a full refund, provided that no additional sessions have been attended after the demo."
  },
  {
    id: 22,
    title: "One-to-One Training Refunds",
    content: "For one-to-one training sessions, refund requests must be made before the second session. After this point, fees become non-refundable."
  },
  {
    id: 23,
    title: "Exam Support and Services",
    content: "Fees paid for exam assistance, certification support, or job-related services are non-refundable once the service has been initiated."
  },
  {
    id: 24,
    title: "No-Show Policy",
    content: "Failure to attend scheduled sessions without prior notice will not qualify for any refund or compensation."
  },
  {
    id: 25,
    title: "Refund Processing",
    content: "Approved refunds will be processed within 7 to 10 business days and will be issued using the original payment method."
  },
  {
    id: 26,
    title: "No Job Guarantee Disclaimer",
    content: "Training Protec provides training, guidance, and support; however, we do not guarantee job placement. Employment outcomes depend on individual skills, experience, and prevailing market conditions."
  },
  {
    id: 27,
    title: "Updates to This Policy",
    content: "We reserve the right to update or modify this policy at any time. Continued use of our website and services after any changes constitutes acceptance of the revised terms."
  }
];

const TermsAndConditions = ({ section }) => {
  const location = useLocation();

  // Determine which section to display based on prop or URL path
  const activeSection = section || 
    (location.pathname === '/privacy' ? 'privacy' : 
     location.pathname === '/refund' ? 'refund' : 
     'terms');

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location]);

  const showTerms = activeSection === 'terms';
  const showPrivacy = activeSection === 'privacy';
  const showRefund = activeSection === 'refund';

  // Dynamic hero title and description based on active section
  const getHeroContent = () => {
    switch (activeSection) {
      case 'terms':
        return { title: 'Terms & Conditions', desc: 'Effective Date: April 2026  |  Training Protec' };
      case 'privacy':
        return { title: 'Privacy Policy', desc: 'Effective Date: April 2026  |  Training Protec' };
      case 'refund':
        return { title: 'Refund Policy', desc: 'Effective Date: April 2026  |  Training Protec' };
      default:
        return { title: 'Terms, Privacy & Refund Policy', desc: 'Effective Date: April 2026  |  Training Protec' };
    }
  };

  const heroContent = getHeroContent();

  const getSeoContent = () => {
    switch (activeSection) {
      case 'terms':
        return { title: 'Terms & Conditions', description: "Read TrainingProtec's Terms & Conditions. Understand the guidelines governing the use of our website and services.", canonical: '/terms' };
      case 'privacy':
        return { title: 'Privacy Policy', description: "Read TrainingProtec's Privacy Policy. Learn how we collect, use, and protect your personal information.", canonical: '/privacy' };
      case 'refund':
        return { title: 'Refund Policy', description: "Read TrainingProtec's Refund Policy. Understand our fair and transparent refund practices and eligibility.", canonical: '/refund' };
      default:
        return { title: 'Terms, Privacy & Refund Policy', description: "Read TrainingProtec's Terms & Conditions, Privacy Policy, and Refund Policy. Understand your rights, data protection practices, and refund eligibility.", canonical: '/terms' };
    }
  };

  const seoContent = getSeoContent();

  return (
    <div className="terms-page">
      <SEO
        title={seoContent.title}
        description={seoContent.description}
        canonical={seoContent.canonical}
        noIndex={false}
      />
      {/* Hero */}
      <section className="terms-hero">
        <div className="terms-hero-overlay"></div>
        <div className="terms-hero-content">
          <Link to="/" className="terms-back-link">
            <FaArrowLeft /> Back to Home
          </Link>
          <h1>{heroContent.title}</h1>
          <p>{heroContent.desc}</p>
        </div>
      </section>

      {/* Quick Nav */}
      <div className="terms-quick-nav">
        <div className="terms-container">
          <Link to="/terms" className={`terms-nav-pill ${activeSection === 'terms' ? 'active' : ''}`}><FaShieldAlt /> Terms & Conditions</Link>
          <Link to="/privacy" className={`terms-nav-pill ${activeSection === 'privacy' ? 'active' : ''}`}><FaLock /> Privacy Policy</Link>
          <Link to="/refund" className={`terms-nav-pill ${activeSection === 'refund' ? 'active' : ''}`}><FaUndo /> Refund Policy</Link>
        </div>
      </div>

      <div className="terms-container terms-body">

        {/* Terms & Conditions */}
        {showTerms && (
        <section id="terms" className="terms-group">
          <div className="terms-group-header">
            <div className="terms-group-icon"><FaShieldAlt /></div>
            <div>
              <h2>Terms & Conditions</h2>
              <p>Guidelines governing the use of our website and services.</p>
            </div>
          </div>
          <div className="terms-cards">
            {termsSections.map((sec) => (
              <div className="terms-card" key={sec.id}>
                <div className="terms-card-num">{sec.id}</div>
                <div className="terms-card-body">
                  <h3>{sec.title}</h3>
                  <p>{sec.content}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
        )}

        {/* Privacy Policy */}
        {showPrivacy && (
        <section id="privacy" className="terms-group">
          <div className="terms-group-header">
            <div className="terms-group-icon"><FaLock /></div>
            <div>
              <h2>Privacy Policy</h2>
              <p>How we collect, use, and protect your personal information.</p>
            </div>
          </div>
          <div className="terms-cards">
            {privacySections.map((sec) => (
              <div className="terms-card" key={sec.id}>
                <div className="terms-card-num">{sec.id}</div>
                <div className="terms-card-body">
                  <h3>{sec.title}</h3>
                  <p>{sec.content}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
        )}

        {/* Refund Policy */}
        {showRefund && (
        <section id="refund" className="terms-group">
          <div className="terms-group-header">
            <div className="terms-group-icon"><FaUndo /></div>
            <div>
              <h2>Refund Policy</h2>
              <p>Our fair and transparent refund practices.</p>
            </div>
          </div>
          <div className="terms-cards">
            {refundSections.map((sec) => (
              <div className="terms-card" key={sec.id}>
                <div className="terms-card-num">{sec.id}</div>
                <div className="terms-card-body">
                  <h3>{sec.title}</h3>
                  <p>{sec.content}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
        )}

        {/* Contact */}
        <section className="terms-contact-box">
          <h3>Contact Information</h3>
          <p>If you have any questions or concerns regarding this policy, you may contact Training Protec:</p>
          <div className="terms-contact-links">
            <a href="mailto:contact@trainingprotec.com" className="terms-contact-link">
              <FaEnvelope /> contact@trainingprotec.com
            </a>
            <a href="https://www.trainingprotec.com" target="_blank" rel="noopener noreferrer" className="terms-contact-link">
              <FaGlobe /> www.trainingprotec.com
            </a>
          </div>
        </section>

      </div>
    </div>
  );
};

export default TermsAndConditions;
