import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { FaArrowLeft, FaArrowRight, FaCheckCircle, FaQuoteLeft, FaChevronDown, FaChevronUp, FaClock, FaGraduationCap, FaTag, FaSpinner, FaEnvelope } from 'react-icons/fa';
import coursesDetailData from './courseData';
import SEO from './SEO';

const CourseDetail = () => {
  const { slug } = useParams();
  const [activeAccordion, setActiveAccordion] = useState(null);
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [allSlugs, setAllSlugs] = useState([]);

  useEffect(() => {
    window.scrollTo(0, 0);
    setLoading(true);
    setActiveAccordion(null);

    // Try API first, fallback to local data
    fetch(`${process.env.REACT_APP_API_URL || ''}/api/courses/${slug}`)
      .then(res => {
        if (!res.ok) throw new Error('Not found');
        return res.json();
      })
      .then(data => {
        // Find matching local data for rich detail fields
        const localCourse = coursesDetailData.find(c => c.slug === data.slug);

        // Map API data and merge with local data when API fields are empty
        setCourse({
          slug: data.slug,
          title: data.title,
          tagline: data.tagline || (localCourse && localCourse.tagline) || data.description,
          heroImage: data.heroImage || data.image || (localCourse && localCourse.heroImage),
          price: data.price ? `$${data.price}` : (localCourse && localCourse.price),
          duration: data.duration || (localCourse && localCourse.duration),
          level: data.level || (localCourse && localCourse.level),
          overview: data.overview || (localCourse && localCourse.overview) || data.description,
          keyBenefits: (data.keyBenefits && data.keyBenefits.length > 0) ? data.keyBenefits : (localCourse && localCourse.keyBenefits) || [],
          subServices: (data.modulesDetail && data.modulesDetail.length > 0)
            ? data.modulesDetail.map(m => ({ title: m.title, description: m.description }))
            : (localCourse && localCourse.subServices) || [],
          process: (data.learningPath && data.learningPath.length > 0)
            ? data.learningPath.map(s => ({ step: s.step, title: s.title, description: s.description }))
            : (localCourse && localCourse.process) || [],
          technologies: (data.technologies && data.technologies.length > 0) ? data.technologies : (localCourse && localCourse.technologies) || [],
          faq: (data.faq && data.faq.length > 0) ? data.faq : (localCourse && localCourse.faq) || [],
          stats: (data.detailStats && data.detailStats.length > 0) ? data.detailStats : (localCourse && localCourse.stats) || []
        });
        setLoading(false);
      })
      .catch(() => {
        // Fallback to local courseData.js
        const localCourse = coursesDetailData.find(c => c.slug === slug);
        if (localCourse) {
          setCourse({
            ...localCourse,
            price: localCourse.price,
          });
        }
        setLoading(false);
      });

    // Get all course slugs for navigation
    fetch(`${process.env.REACT_APP_API_URL || ''}/api/courses`)
      .then(res => res.ok ? res.json() : Promise.reject())
      .then(data => {
        if (data && data.length > 0) {
          setAllSlugs(data.map(c => ({ slug: c.slug, title: c.title })));
        } else {
          setAllSlugs(coursesDetailData.map(c => ({ slug: c.slug, title: c.title })));
        }
      })
      .catch(() => {
        setAllSlugs(coursesDetailData.map(c => ({ slug: c.slug, title: c.title })));
      });
  }, [slug]);

  if (loading) {
    return (
      <div className="service-detail-not-found" style={{ textAlign: 'center', padding: '5rem 2rem' }}>
        <FaSpinner className="spin" style={{ fontSize: '2rem', color: '#0066cc', animation: 'spin 1s linear infinite' }} />
        <p style={{ marginTop: '1rem', color: '#64748b' }}>Loading course...</p>
      </div>
    );
  }

  if (!course) {
    return (
      <div className="service-detail-not-found">
        <h2>Course Not Found</h2>
        <p>The course you're looking for doesn't exist.</p>
        <Link to="/" className="btn-back-home">
          <FaArrowLeft /> Back to Home
        </Link>
      </div>
    );
  }

  const currentIndex = allSlugs.findIndex(c => c.slug === slug);
  const prevCourse = allSlugs.length > 0 ? allSlugs[(currentIndex - 1 + allSlugs.length) % allSlugs.length] : null;
  const nextCourse = allSlugs.length > 0 ? allSlugs[(currentIndex + 1) % allSlugs.length] : null;

  const toggleAccordion = (index) => {
    setActiveAccordion(activeAccordion === index ? null : index);
  };

  return (
    <div className="service-detail-page">
      <SEO
        title={`${course.title} Course | Online Training`}
        description={course.overview ? course.overview.slice(0, 155) : `Enroll in ${course.title} training at TrainingProtec. Live classes, expert instructors, real projects and job assistance.`}
        keywords={`${course.title} course, ${course.title} training, online ${course.title}, TrainingProtec ${course.title}`}
        canonical={`/courses/${slug}`}
        ogType="article"
      />
      {/* Hero Section */}
      <section className="sd-hero">
        <div className="sd-hero-bg">
          <img src={course.heroImage} alt={course.title} />
          <div className="sd-hero-overlay"></div>
        </div>
        <div className="sd-hero-content">
          <Link to="/#courses" className="sd-back-link">
            <FaArrowLeft /> Back to Courses
          </Link>
          <div className="sd-hero-icon">
            <FaGraduationCap />
          </div>
          <h1 className="sd-hero-title">{course.title}</h1>
          <p className="sd-hero-tagline">{course.tagline}</p>
          <div className="sd-hero-stats">
            {course.stats && course.stats.length > 0 && course.stats.map((stat, index) => (
              <div key={index} className="sd-stat">
                <span className="sd-stat-number">{stat.number}</span>
                <span className="sd-stat-label">{stat.label}</span>
              </div>
            ))}
          </div>
          <div className="course-detail-meta">
            <span className="course-meta-item"><FaTag /> {course.price}</span>
            <span className="course-meta-item"><FaClock /> {course.duration}</span>
            <span className="course-meta-item"><FaGraduationCap /> {course.level}</span>
          </div>
        </div>
      </section>

      {/* Overview Section */}
      {course.overview && (
      <section className="sd-overview">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Overview</span>
            <h2>About This Course</h2>
          </div>
          <div className="sd-overview-content">
            <p className="sd-overview-text">{course.overview}</p>
            {course.keyBenefits && course.keyBenefits.length > 0 && (
            <div className="sd-benefits">
              <h3>What You'll Learn</h3>
              <ul className="sd-benefits-list">
                {course.keyBenefits.map((benefit, index) => (
                  <li key={index}>
                    <FaCheckCircle className="sd-check-icon" />
                    <span>{benefit}</span>
                  </li>
                ))}
              </ul>
            </div>
            )}
          </div>
        </div>
      </section>
      )}

      {/* Modules Section */}
      {course.subServices && course.subServices.length > 0 && (
      <section className="sd-sub-services">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Curriculum</span>
            <h2>Course Modules</h2>
            <p>Comprehensive modules designed for progressive learning</p>
          </div>
          <div className="sd-sub-grid">
            {course.subServices.map((module, index) => {
              return (
                <div key={index} className="sd-sub-card">
                  <div className="sd-sub-icon">
                    <FaCheckCircle />
                  </div>
                  <h3>{module.title}</h3>
                  <p>{module.description}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>
      )}

      {/* Learning Path Section */}
      {course.process && course.process.length > 0 && (
      <section className="sd-process">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Learning Path</span>
            <h2>Your Journey</h2>
            <p>A structured path from fundamentals to mastery</p>
          </div>
          <div className="sd-process-timeline">
            {course.process.map((step, index) => (
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
      )}

      {/* Technologies Section */}
      {course.technologies && course.technologies.length > 0 && (
      <section className="sd-technologies">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Tools & Technologies</span>
            <h2>What You'll Work With</h2>
          </div>
          <div className="sd-tech-grid">
            {course.technologies.map((tech, index) => (
              <div key={index} className="sd-tech-tag">
                {tech}
              </div>
            ))}
          </div>
        </div>
      </section>
      )}

      {/* FAQ Section */}
      {course.faq && course.faq.length > 0 && (
      <section className="sd-faq">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">FAQ</span>
            <h2>Frequently Asked Questions</h2>
          </div>
          <div className="sd-faq-list">
            {course.faq.map((item, index) => (
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
      )}

      {/* CTA Section */}
      <section className="sd-cta">
        <div className="sd-container">
          <div className="sd-cta-content">
            <FaQuoteLeft className="sd-cta-quote" />
            <h2>Ready to Start Learning?</h2>
            <p>Enroll in {course.title} today and take the first step toward mastering new skills. Join thousands of successful students.</p>
            <div className="sd-cta-buttons">
              <a
                href={`mailto:contact@trainingprotec.com?subject=${encodeURIComponent(`Enrollment Inquiry: ${course.title}`)}&body=${encodeURIComponent(`Hi! I want to enroll in the ${course.title} course.\n\nCourse Details:\n- Course: ${course.title}\n- Price: ${course.price}\n- Duration: ${course.duration}\n- Level: ${course.level}\n\nPlease share enrollment details. Thank you!`)}`}
                className="sd-btn-primary"
              >
                <FaEnvelope /> Enroll Now — {course.price}
              </a>
              <a href="/#courses" className="sd-btn-secondary">
                <FaArrowLeft /> Browse More Courses
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Navigation Between Courses */}
      {allSlugs.length > 1 && (
      <section className="sd-navigation">
        <div className="sd-container">
          <div className="sd-nav-links">
            {prevCourse && (
            <Link to={`/courses/${prevCourse.slug}`} className="sd-nav-prev">
              <FaArrowLeft />
              <div>
                <span>Previous Course</span>
                <h4>{prevCourse.title}</h4>
              </div>
            </Link>
            )}
            {nextCourse && (
            <Link to={`/courses/${nextCourse.slug}`} className="sd-nav-next">
              <div>
                <span>Next Course</span>
                <h4>{nextCourse.title}</h4>
              </div>
              <FaArrowRight />
            </Link>
            )}
          </div>
        </div>
      </section>
      )}
    </div>
  );
};

export default CourseDetail;
