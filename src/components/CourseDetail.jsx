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
          faq: (data.faq && data.faq.length > 0) ? data.faq : (localCourse && localCourse.faq) || [],
          stats: (data.detailStats && data.detailStats.length > 0) ? data.detailStats : (localCourse && localCourse.stats) || [],
          topicWiseContent: (data.topicWiseContent && data.topicWiseContent.length > 0) ? data.topicWiseContent : (localCourse && localCourse.topicWiseContent) || [],
          eligibility: data.eligibility || data.prerequisites || (localCourse && localCourse.eligibility),
          why_join: data.why_join || (localCourse && localCourse.why_join),
          certification: data.certification || (localCourse && localCourse.certification),
          reviewsList: (data.reviewsList && data.reviewsList.length > 0) ? data.reviewsList : (localCourse && localCourse.reviewsList) || [],
          projectsList: (data.projectsList && data.projectsList.length > 0) ? data.projectsList : (localCourse && localCourse.projectsList) || [],
          toolsCovered: (data.tools_covered && Array.isArray(data.tools_covered)) ? data.tools_covered : (typeof data.tools_covered === 'string' ? data.tools_covered.split(',').map(t => t.trim()).filter(t => t) : []) || (localCourse && localCourse.toolsCovered) || [],
          skillsCovered: (data.skills_covered && Array.isArray(data.skills_covered)) ? data.skills_covered : (typeof data.skills_covered === 'string' ? data.skills_covered.split(',').map(s => s.trim()).filter(s => s) : []) || (localCourse && localCourse.skillsCovered) || [],
          targetAudience: data.target_audience || (localCourse && localCourse.targetAudience),
          trainingSchedule: data.training_schedule || (localCourse && localCourse.trainingSchedule),
          mode: data.mode || (localCourse && localCourse.mode),
          language: data.language || (localCourse && localCourse.language) || 'English',
          emiOptions: data.emi_options || (localCourse && localCourse.emiOptions),
          discountPercent: data.discount_percent || (localCourse && localCourse.discountPercent),
          originalPrice: data.originalPrice ? `$${data.originalPrice}` : (localCourse && localCourse.originalPrice),
          technologies: (data.technologies_list && typeof data.technologies_list === 'string') 
            ? data.technologies_list.split(',').map(t => t.trim()).filter(t => t)
            : (data.technologies && data.technologies.length > 0) ? data.technologies : (localCourse && localCourse.technologies) || []
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
    <div className="wiki-course-detail">
      <SEO
        title={`${course.title} Course | Online Training`}
        description={course.overview ? course.overview.slice(0, 155) : `Enroll in ${course.title} training at TrainingProtec.`}
        keywords={`${course.title} course, ${course.title} training, online ${course.title}`}
        canonical={`/courses/${slug}`}
        ogType="article"
      />

      {/* Back Link */}
      <div style={{marginBottom: '20px'}}>
        <Link to="/courses" style={{color: '#3366cc', textDecoration: 'none', fontSize: '14px'}}>← Back to Courses</Link>
      </div>

      {/* Header */}
      <div className="wiki-course-header">
        <h1>{course.title}</h1>
        {course.tagline && <p className="tagline">{course.tagline}</p>}
        
        {/* Quick Info Table */}
        <table className="wiki-table" style={{marginTop: '15px'}}>
          <tbody>
            <tr>
              <th>Price</th>
              <td>{course.price}</td>
              <th>Duration</th>
              <td>{course.duration}</td>
            </tr>
            <tr>
              <th>Level</th>
              <td>{course.level}</td>
              <th>Rating</th>
              <td>{course.rating || '4.5'} ⭐</td>
            </tr>
            <tr>
              <th>Students</th>
              <td>{course.learners || '0'}</td>
              <th>Reviews</th>
              <td>{course.reviews || '0'}</td>
            </tr>
            {course.mode && (
            <tr>
              <th>Mode</th>
              <td colSpan="3">{course.mode}</td>
            </tr>
            )}
          </tbody>
        </table>
</div>

      {/* About Course */}
      {course.overview && (
      <div className="wiki-section">
        <h2>About This Course</h2>
        <p>{course.overview}</p>
      </div>
      )}

      {/* What You'll Learn */}
      {course.keyBenefits && course.keyBenefits.length > 0 && (
      <div className="wiki-section">
        <h2>What You'll Learn</h2>
        <ul>
          {course.keyBenefits.map((benefit, index) => (
            <li key={index}>{benefit}</li>
          ))}
        </ul>
      </div>
      )}

      

      {/* Course Curriculum - Simple List */}
      {course.topicWiseContent && course.topicWiseContent.length > 0 && (
      <div className="wiki-section">
        <h2>Course Curriculum</h2>
        {course.topicWiseContent.map((group, gIndex) => (
          <div key={gIndex} style={{marginBottom: '20px'}}>
            <h3 style={{fontSize: '16px', fontWeight: 'bold', marginBottom: '10px'}}>{gIndex + 1}. {group.heading}</h3>
            {group.items && group.items.length > 0 && (
              <ul style={{marginLeft: '20px'}}>
                {group.items.map((item, iIndex) => (
                  <li key={iIndex} style={{marginBottom: '5px'}}>{item.title}</li>
                ))}
              </ul>
            )}
          </div>
        ))}
      </div>
      )}

      {/* Projects - Simple */}
      {course.projectsList && course.projectsList.length > 0 && (
      <div className="wiki-section">
        <h2>Industry Projects</h2>
        <ul>
          {course.projectsList.map((project, index) => (
            <li key={index}>
              <strong>{project.title}</strong>: {project.description}
            </li>
          ))}
        </ul>
      </div>
      )}

      {/* Why Join - Simple */}
      {course.why_join && course.why_join.length > 0 && (
      <div className="wiki-section">
        <h2>Why Join This Program</h2>
        <ul>
          {course.why_join.map((item, index) => (
            <li key={index}><strong>{item.title}</strong>: {item.description}</li>
          ))}
        </ul>
      </div>
      )}

      
      )}

      {/* Skills - Simple */}
      {course.skillsCovered && course.skillsCovered.length > 0 && (
      <div className="wiki-section">
        <h2>Skills You'll Gain</h2>
        <div className="wiki-tags">
          {course.skillsCovered.map((skill, index) => (
            <span key={index}>{skill}</span>
          ))}
        </div>
      </div>
      )}

      {/* Student Reviews - Simple */}
      {course.reviewsList && course.reviewsList.length > 0 && (
      <div className="wiki-section">
        <h2>Student Reviews</h2>
        {course.reviewsList.map((review, index) => (
          <div key={index} className="wiki-review">
            <p>"{review.text}"</p>
            <strong>{review.name}</strong>
            <span> - {review.role}</span>
          </div>
        ))}
      </div>
      )}

      {/* FAQ - Simple */}
      {course.faq && course.faq.length > 0 && (
      <div className="wiki-section">
        <h2>Frequently Asked Questions</h2>
        {course.faq.map((item, index) => (
          <div key={index} className="wiki-faq">
            <div className="wiki-faq-question">{item.question}</div>
            <div className="wiki-faq-answer">{item.answer}</div>
          </div>
        ))}
      </div>
      )}

      {/* CTA - Simple */}
      <div className="wiki-section" style={{textAlign: 'center', background: '#f8f9fa', padding: '30px'}}>
        <h2>Ready to Start?</h2>
        <p>Enroll in this course today.</p>
        <a href={`mailto:contact@trainingprotec.com?subject=${encodeURIComponent(`Enrollment: ${course.title}`)}`} 
           style={{display: 'inline-block', background: '#0066cc', color: '#fff', padding: '12px 24px', borderRadius: '5px', textDecoration: 'none', marginTop: '10px'}}>
          Enroll Now - {course.price}
        </a>
      </div>

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

      {/* Navigation - Simple */}
      {allSlugs.length > 1 && (
      <div className="wiki-section" style={{display: 'flex', justifyContent: 'space-between', borderTop: '1px solid #a2a9b1', paddingTop: '20px'}}>
        {prevCourse && <Link to={`/courses/${prevCourse.slug}`} style={{color: '#3366cc'}}>← {prevCourse.title}</Link>}
        {nextCourse && <Link to={`/courses/${nextCourse.slug}`} style={{color: '#3366cc'}}>{nextCourse.title} →</Link>}
      </div>
      )}
    </div>
  );
};

export default CourseDetail;