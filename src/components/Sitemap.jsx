import React, { useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaArrowLeft, FaHome, FaGraduationCap, FaBlog, FaUsers, FaShieldAlt, FaLock, FaUndo, FaChalkboardTeacher, FaHandshake, FaBriefcase, FaEnvelope, FaGlobe, FaSitemap } from 'react-icons/fa';
import SEO from './SEO';

const Sitemap = () => {
  const location = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location]);

  const sitemapSections = [
    {
      title: 'Main Pages',
      icon: <FaHome />,
      links: [
        { name: 'Home', url: '/' },
        { name: 'About TrainingProtec', url: '/#about' },
        { name: 'Our Features', url: '/#features' },
        { name: 'Success Stories', url: '/#testimonials' },
        { name: 'Blog & Articles', url: '/#blog' },
        { name: 'Contact Us / Free Career Counselling', url: '/#contact' },
      ]
    },
    {
      title: 'Courses',
      icon: <FaGraduationCap />,
      links: [
        { name: 'All Courses', url: '/#courses' },
        { name: 'Data Science & AI', url: '/courses/data-science-ai' },
        { name: 'Cloud Computing & DevOps', url: '/courses/cloud-computing-devops' },
        { name: 'Cyber Security', url: '/courses/cyber-security' },
        { name: 'Full Stack Web Development', url: '/courses/web-development' },
        { name: 'Digital Marketing', url: '/courses/digital-marketing' },
        { name: 'Business Analytics', url: '/courses/business-analytics' },
        { name: 'UI/UX Design', url: '/courses/ui-ux-design' },
        { name: 'Mobile App Development', url: '/courses/mobile-app-development' },
      ]
    },
    {
      title: 'Company',
      icon: <FaUsers />,
      links: [
        { name: 'About Us', url: '/#about' },
        { name: 'Contact Us', url: '/#contact' },
        { name: 'Become an Instructor', url: '/enquiry/instructor' },
        { name: 'Partnerships', url: '/enquiry/partnership' },
        { name: 'Careers at TrainingProtec', url: '/enquiry/career' },
      ]
    },
    {
      title: 'Policies',
      icon: <FaShieldAlt />,
      links: [
        { name: 'Terms & Conditions', url: '/terms' },
        { name: 'Privacy Policy', url: '/privacy' },
        { name: 'Refund Policy', url: '/refund' },
      ]
    }
  ];

  return (
    <div className="terms-page">
      <SEO
        title="Sitemap – TrainingProtec"
        description="Browse all pages on TrainingProtec. Find courses, company info, policies, and more."
        canonical="/sitemap"
        noIndex={false}
      />

      {/* Hero */}
      <section className="terms-hero">
        <div className="terms-hero-overlay"></div>
        <div className="terms-hero-content">
          <Link to="/" className="terms-back-link">
            <FaArrowLeft /> Back to Home
          </Link>
          <h1><FaSitemap /> Sitemap</h1>
          <p>Quick navigation to all pages on TrainingProtec</p>
        </div>
      </section>

      {/* Sitemap Content */}
      <div className="terms-container terms-body">
        <div className="sitemap-grid">
          {sitemapSections.map((section) => (
            <div className="sitemap-section" key={section.title}>
              <div className="terms-group-header">
                <div className="terms-group-icon">{section.icon}</div>
                <div>
                  <h2>{section.title}</h2>
                </div>
              </div>
              <ul className="sitemap-links">
                {section.links.map((link) => (
                  <li key={link.url + link.name}>
                    {link.url.startsWith('/#') ? (
                      <a href={link.url}>{link.name}</a>
                    ) : (
                      <Link to={link.url}>{link.name}</Link>
                    )}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Contact */}
        <section className="terms-contact-box">
          <h3>Can't Find What You're Looking For?</h3>
          <p>Reach out to us and we'll be happy to help.</p>
          <div className="terms-contact-links">
            <a href="mailto:contact@trainingprotec.com" className="terms-contact-link">
              <FaEnvelope /> contact@trainingprotec.com
            </a>
            <Link to="/#contact" className="terms-contact-link">
              <FaGlobe /> Contact Page
            </Link>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Sitemap;
