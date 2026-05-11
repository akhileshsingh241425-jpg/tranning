import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { FaArrowLeft, FaArrowRight, FaCheckCircle, FaQuoteLeft, FaChevronDown, FaChevronUp, FaClock, FaGraduationCap, FaTag, FaSpinner, FaEnvelope, FaBookOpen, FaClipboardList, FaCertificate, FaBriefcase, FaUser, FaStar, FaTrend, FaDollarSign, FaJob, FaUsers, FaProjectDiagram, FaHeadset, FaRedo, FaMoneyBillWave } from 'react-icons/fa';
import coursesDetailData from './courseData';
import SEO from './SEO';

const renderParagraphs = (text, className = '') => {
  if (!text) return null;
  const paragraphs = text.split(/\n\n+/).filter(p => p.trim());
  if (paragraphs.length <= 1) {
    return <p className={className}>{text}</p>;
  }
  return paragraphs.map((p, i) => <p key={i} className={className}>{p.trim()}</p>);
};

const CourseDetail = () => {
  const { slug } = useParams();
  const [activeAccordion, setActiveAccordion] = useState(null);
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [allSlugs, setAllSlugs] = useState([]);
  const [curriculumOpen, setCurriculumOpen] = useState(0);

  useEffect(() => {
    window.scrollTo(0, 0);
    setLoading(true);
    setActiveAccordion(null);

    fetch(`${process.env.REACT_APP_API_URL || ''}/api/courses/${slug}`)
      .then(res => {
        if (!res.ok) throw new Error('Not found');
        return res.json();
      })
      .then(data => {
        const localCourse = coursesDetailData.find(c => c.slug === data.slug);
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
            ? data.modulesDetail.map((m, i) => ({
                title: m.title,
                description: m.description,
                topics: m.topics || (localCourse && localCourse.subServices && localCourse.subServices[i] && localCourse.subServices[i].topics) || []
              }))
            : (localCourse && localCourse.subServices) || [],
          process: (data.learningPath && data.learningPath.length > 0)
            ? data.learningPath.map(s => ({ step: s.step, title: s.title, description: s.description }))
            : (localCourse && localCourse.process) || [],
          technologies: (data.technologies && data.technologies.length > 0) ? data.technologies : (localCourse && localCourse.technologies) || [],
          faq: (data.faq && data.faq.length > 0) ? data.faq : (localCourse && localCourse.faq) || [],
          stats: (data.detailStats && data.detailStats.length > 0) ? data.detailStats : (localCourse && localCourse.stats) || [],
          topicWiseContent: (data.topicWiseContent && data.topicWiseContent.length > 0) ? data.topicWiseContent : (localCourse && localCourse.topicWiseContent) || [],
          eligibility: data.eligibility || (localCourse && localCourse.eligibility),
          why_join: data.why_join || (localCourse && localCourse.why_join),
          certification: data.certification || (localCourse && localCourse.certification),
          reviewsList: (data.reviewsList && data.reviewsList.length > 0) ? data.reviewsList : (localCourse && localCourse.reviewsList) || []
        });
        setLoading(false);
      })
      .catch(() => {
        const localCourse = coursesDetailData.find(c => c.slug === slug);
        if (localCourse) {
          setCourse({ ...localCourse, price: localCourse.price });
        }
        setLoading(false);
      });

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

  return (
    <div className="service-detail-page">
      <SEO
        title={`${course.title} Course | Online Training`}
        description={course.overview ? course.overview.slice(0, 155) : `Enroll in ${course.title} training at TrainingProtec.`}
        keywords={`${course.title} course, ${course.title} training, online ${course.title}`}
        canonical={`/courses/${slug}`}
        ogType="article"
      />

      {/* 1. Hero Section */}
      <section className="sd-hero">
        <div className="sd-hero-bg">
          <img 
            src={course.heroImage || 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1200&q=80'} 
            alt={course.title}
            onError={(e) => { e.target.src = 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1200&q=80'; }}
          />
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

      {/* 2. Eligibility */}
      <section className="sd-prerequisites">
        <div className="sd-container" style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 24px' }}>
          <div className="sd-prereq-box">
            <h3><FaClipboardList /> Eligibility</h3>
            <p>{course.eligibility || 'This course is ideal for professionals looking to enhance their skills. No prior experience required.'}</p>
            <div className="sd-prereq-tags">
              <span className="sd-prereq-tag"><FaCheckCircle /> Beginners</span>
              <span className="sd-prereq-tag"><FaCheckCircle /> Working Professionals</span>
              <span className="sd-prereq-tag"><FaCheckCircle /> Career Changers</span>
              <span className="sd-prereq-tag"><FaCheckCircle /> Students & Graduates</span>
            </div>
          </div>
        </div>
      </section>

      {/* 3. Overview + CTA */}
      {course.overview && (
      <section className="sd-overview">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Overview</span>
            <h2>About This Course</h2>
          </div>
          <div className="sd-overview-content">
            {renderParagraphs(course.overview, 'sd-overview-text')}
            {course.keyBenefits && course.keyBenefits.length > 0 && (
            <div className="sd-overview-grid">
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
              {course.price && (
              <div className="sd-cta-sidebar">
                <div className="sd-cta-box">
                  <div className="sd-cta-badge"><FaStar /> 41% Off</div>
                  <h3>Enroll Now</h3>
                  <ul className="sd-cta-list">
                    <li><FaCheckCircle /> Lifetime access</li>
                    <li><FaCheckCircle /> Industry projects</li>
                    <li><FaCheckCircle /> Certificate</li>
                    <li><FaCheckCircle /> Resume help</li>
                    <li><FaCheckCircle /> Interview prep</li>
                    <li><FaCheckCircle /> 24/7 support</li>
                  </ul>
                  <div className="sd-cta-price">
                    <span className="sd-cur-price">{course.price}</span>
                    <span className="sd-old-price">$25,424</span>
                    <span className="sd-discount">41% OFF</span>
                  </div>
                  <a href={`mailto:contact@trainingprotec.com?subject=${encodeURIComponent(`Enrollment: ${course.title}`)}`} className="sd-btn-enroll">Enroll Now</a>
                  <button 
                    onClick={() => document.getElementById('course-detail-modal').style.display = 'flex'}
                    className="sd-btn-download"
                  >
                    ⚡ Quick Overview
                  </button>
                </div>
              </div>
              )}
            </div>
            )}
          </div>
        </div>
      </section>
      )}

      

      {/* 4. Course Curriculum */}
      {course.topicWiseContent && course.topicWiseContent.length > 0 && (
      <section className="sd-curriculum">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Curriculum</span>
            <h2>Course Curriculum</h2>
            <p>Complete syllabus with detailed lessons</p>
          </div>
          <div className="sd-curriculum-sections">
            {course.topicWiseContent.map((group, gIndex) => (
              <div key={gIndex} className={`sd-curriculum-section ${curriculumOpen === gIndex ? 'active' : (curriculumOpen === -1 && gIndex === 0 ? 'active' : '')}`}>
                <button className="sd-curriculum-section-header" onClick={() => setCurriculumOpen(curriculumOpen === gIndex ? -1 : gIndex)}>
                  <div className="sd-section-num">{gIndex + 1}</div>
                  <div className="sd-section-info">
                    <h3>{group.heading}</h3>
                    <div className="sd-section-meta">
                      <span><FaBookOpen /> {group.items ? group.items.length : 0} Lessons</span>
                      <span><FaClock /> {group.items ? Math.floor(group.items.length * 3.5) + ':00' : '0:00'}</span>
                    </div>
                  </div>
                  <div className="sd-section-toggle"><FaChevronDown /></div>
                </button>
                <div className="sd-curriculum-body">
                  <div className="sd-curriculum-inner">
                    {group.items && group.items.map((item, iIndex) => (
                      <div key={iIndex} className="sd-lesson-item">
                        <i className="fas fa-play-circle sd-lesson-icon"></i>
                        <span className="sd-lesson-name">{item.title}</span>
                        <span className="sd-lesson-duration">{item.subtopics ? item.subtopics.length * 5 : 5}:00</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
      )}

      {/* 5. How to Prepare */}
      {course.why_join && course.why_join.length > 0 && (
      <section className="sd-prepare">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Career Prep</span>
            <h2>How to Prepare for a Career</h2>
          </div>
          <div className="sd-prepare-grid">
            {course.why_join.map((item, index) => (
              <div key={index} className="sd-prepare-card">
                <div className="sd-prepare-icon"><i className={`fas ${item.icon}`}></i></div>
                <h3>{item.title}</h3>
                <p>{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
      )}

      {/* 6. Certification */}
      {course.certification && course.certification.title && (
      <section className="sd-cert-simple">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Certification</span>
            <h2>Exam & <strong>Certification</strong></h2>
          </div>
          <div className="sd-cert-simple-content">
            <div className="sd-cert-main">
              <FaCertificate className="sd-cert-icon" />
              <h3>{course.certification.title}</h3>
              <div className="sd-cert-points">
                <ul>
                  <li>Validates your ability to design and deploy scalable, secure systems on cloud</li>
                  <li>Recognized by top companies worldwide</li>
                  <li>Boosts your career with higher salary packages</li>
                  <li>Demonstrates expert-level cloud architecture skills</li>
                </ul>
              </div>
            </div>
            <div className="sd-cert-details-grid">
              <div className="sd-cert-detail"><FaClock /><div><h4>Duration</h4><p>130 min</p></div></div>
              <div className="sd-cert-detail"><FaBookOpen /><div><h4>Questions</h4><p>65</p></div></div>
              <div className="sd-cert-detail"><FaRedo /><div><h4>Validity</h4><p>2 Years</p></div></div>
              <div className="sd-cert-detail"><FaMoneyBillWave /><div><h4>Avg Salary</h4><p>$113K/yr</p></div></div>
            </div>
            <div className="sd-cert-roles">
              <h4><FaBriefcase /> Job Roles:</h4>
              <div className="sd-cert-role-tags">
                <span>Solutions Architect</span>
                <span>Cloud Architect</span>
                <span>DevOps Engineer</span>
                <span>Cloud Engineer</span>
              </div>
            </div>
          </div>
        </div>
      </section>
      )}

      {/* 7. Skills Covered */}
      {course.technologies && course.technologies.length > 0 && (
      <section className="sd-skills-simple">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Skills</span>
            <h2>Skills Covered</h2>
          </div>
          <div className="sd-skills-simple-grid">
            {course.technologies.map((tech, index) => (
              <div key={index} className="sd-skill-simple-item">
                <FaCheckCircle />
                <span>{tech}</span>
              </div>
            ))}
          </div>
        </div>
      </section>
      )}

      {/* 8. Why Join */}
      <section className="sd-why-join-demo">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Why Join</span>
            <h2>Why Join this <strong>Program</strong></h2>
          </div>
          <div className="sd-why-grid">
            <div className="sd-why-card"><FaProjectDiagram /><h3>Expert Curriculum</h3><p>Designed with industry experts</p></div>
            <div className="sd-why-card"><FaUsers /><h3>Expert Trainers</h3><p>Learn from practitioners</p></div>
            <div className="sd-why-card"><FaBriefcase /><h3>Real Projects</h3><p>Hands-on experience</p></div>
            <div className="sd-why-card"><FaHeadset /><h3>24/7 Support</h3><p>Mentor assistance</p></div>
          </div>
        </div>
      </section>

      {/* 8b. Student Reviews - What Students Say */}
      {course.reviewsList && course.reviewsList.length > 0 && (
      <section className="sd-testimonials">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Testimonials</span>
            <h2>What Our <strong>Students Say</strong></h2>
          </div>
          <div className="sd-testimonials-grid">
            {course.reviewsList.map((review, index) => (
              <div key={index} className="sd-testimonial-card">
                <div className="sd-testimonial-quote">
                  <FaQuoteLeft />
                </div>
                <p className="sd-testimonial-text">{review.text}</p>
                <div className="sd-testimonial-author">
                  <div className="sd-author-avatar">
                    {review.name.charAt(0)}
                  </div>
                  <div className="sd-author-info">
                    <h4>{review.name}</h4>
                    <span>{review.role}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
      )}

      {/* 9. Technologies */}
      {course.technologies && course.technologies.length > 0 && (
      <section className="sd-technologies">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">Tools</span>
            <h2>What You'll Work With</h2>
          </div>
          <div className="sd-tech-grid">
            {course.technologies.map((tech, index) => (
              <div key={index} className="sd-tech-tag">{tech}</div>
            ))}
          </div>
        </div>
      </section>
      )}

      {/* 10. FAQ */}
      {course.faq && course.faq.length > 0 && (
      <section className="sd-faq">
        <div className="sd-container">
          <div className="sd-section-header">
            <span className="sd-badge">FAQ</span>
            <h2>Frequently Asked Questions</h2>
          </div>
          <div className="sd-faq-list">
            {course.faq.map((item, index) => (
              <div key={index} className={`sd-faq-item ${activeAccordion === index ? 'active' : ''}`}>
                <button className="sd-faq-question" onClick={() => setActiveAccordion(activeAccordion === index ? null : index)}>
                  <span>{item.question}</span>
                  {activeAccordion === index ? <FaChevronUp /> : <FaChevronDown />}
                </button>
                <div className={`sd-faq-answer ${activeAccordion === index ? 'open' : ''}`}>
                  {renderParagraphs(item.answer)}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
      )}

      {/* 11. Final CTA */}
      <section className="sd-cta">
        <div className="sd-container">
          <div className="sd-cta-content">
            <FaQuoteLeft className="sd-cta-quote" />
            <h2>Ready to Start Learning?</h2>
            <p>Enroll in {course.title} today and take the first step toward mastering new skills.</p>
            <div className="sd-cta-buttons">
              <a href={`mailto:contact@trainingprotec.com?subject=${encodeURIComponent(`Enrollment: ${course.title}`)}`} className="sd-btn-primary">
                <FaEnvelope /> Enroll Now — {course.price}
              </a>
              <a href="/#courses" className="sd-btn-secondary">
                <FaArrowLeft /> Browse More Courses
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Course Detail Modal */}
      <div id="course-detail-modal" className="course-modal" onClick={(e) => { if(e.target.id === 'course-detail-modal') e.target.style.display = 'none' }}>
        <div className="modal-content">
          <button className="modal-close" onClick={() => document.getElementById('course-detail-modal').style.display = 'none'}>✕</button>
          
          <div className="modal-header">
            <h2>{course.title}</h2>
            <p className="modal-tagline">{course.tagline}</p>
            <div className="modal-stats">
              <span>⭐ {course.rating || '4.5'} Rating</span>
              <span>👥 {course.learners || '10K+'} Students</span>
              <span>⏱️ {course.duration}</span>
              <span>📊 {course.level}</span>
            </div>
          </div>

          <div className="modal-body">
            <div className="modal-section">
              <h3>📚 Overview</h3>
              <p>{course.overview}</p>
            </div>

            {course.keyBenefits && course.keyBenefits.length > 0 && (
            <div className="modal-section">
              <h3>🎯 What You'll Learn</h3>
              <ul className="benefits-list">
                {course.keyBenefits.map((b, i) => (
                  <li key={i}><span>✓</span> {b}</li>
                ))}
              </ul>
            </div>
            )}

            {course.technologies && course.technologies.length > 0 && (
            <div className="modal-section">
              <h3>💻 Skills Covered</h3>
              <div className="skills-grid">
                {course.technologies.map((t, i) => (
                  <span key={i} className="skill-tag">{t}</span>
                ))}
              </div>
            </div>
            )}

            <div className="modal-section">
              <h3>📖 Course Details</h3>
              <div className="details-grid">
                <div className="detail-card">
                  <span>⏱️</span>
                  <strong>Duration</strong>
                  <p>{course.duration}</p>
                </div>
                <div className="detail-card">
                  <span>📚</span>
                  <strong>Modules</strong>
                  <p>{course.modules || '12'} Modules</p>
                </div>
                <div className="detail-card">
                  <span>💼</span>
                  <strong>Projects</strong>
                  <p>{course.projects || '5'} Projects</p>
                </div>
                <div className="detail-card">
                  <span>🏆</span>
                  <strong>Certificate</strong>
                  <p>Yes</p>
                </div>
              </div>
            </div>

            {course.certification && (
            <div className="modal-section">
              <h3>🏆 Certification</h3>
              <div className="cert-box">
                <h4>{course.certification.title}</h4>
                {course.certification.faqs && course.certification.faqs.slice(0, 3).map((f, i) => (
                  <p key={i}><strong>• {f.title}:</strong> {f.text}</p>
                ))}
              </div>
            </div>
            )}

            <div className="modal-price-section">
              <div className="price-box">
                <span className="current-price">{course.price}</span>
                <span className="old-price">$25,424</span>
                <span className="discount-tag">41% OFF</span>
              </div>
              <a href={`mailto:contact@trainingprotec.com?subject=${encodeURIComponent(`Enrollment: ${course.title}`)}`} className="modal-enroll-btn">Enroll Now</a>
            </div>
          </div>
        </div>
      </div>

      {/* 12. Navigation */}
      {allSlugs.length > 1 && (
      <section className="sd-navigation">
        <div className="sd-container">
          <div className="sd-nav-links">
            {prevCourse && (
            <Link to={`/courses/${prevCourse.slug}`} className="sd-nav-prev">
              <FaArrowLeft />
              <div><span>Previous</span><h4>{prevCourse.title}</h4></div>
            </Link>
            )}
            {nextCourse && (
            <Link to={`/courses/${nextCourse.slug}`} className="sd-nav-next">
              <div><span>Next</span><h4>{nextCourse.title}</h4></div>
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