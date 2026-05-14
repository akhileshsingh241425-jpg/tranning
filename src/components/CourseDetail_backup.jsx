import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { FaClock, FaGraduationCap, FaStar, FaUsers, FaChevronRight, FaSpinner, FaArrowLeft, FaArrowRight } from 'react-icons/fa';
import coursesDetailData from './courseData';
import SEO from './SEO';

const CourseDetail = () => {
  const { slug } = useParams();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [allSlugs, setAllSlugs] = useState([]);
  const [curriculumOpen, setCurriculumOpen] = useState(0);
  const [subtopicOpen, setSubtopicOpen] = useState({});

  useEffect(() => {
    window.scrollTo(0, 0);
    setLoading(true);

    fetch(`/api/courses/${slug}`)
      .then(res => {
        if (!res.ok) throw new Error('Not found');
        return res.json();
      })
      .then(data => {
        console.log('API Response for course:', slug, data);
        const localCourse = coursesDetailData.find(c => c.slug === data.slug);
        setCourse({
          slug: data.slug,
          title: data.title,
          tagline: data.tagline || (localCourse && localCourse.tagline) || data.description,
          heroImage: data.heroImage || data.image || (localCourse && localCourse.heroImage),
          price: data.price ? `$${data.price}` : (localCourse && localCourse.price),
          originalPrice: data.original_price ? `$${data.original_price}` : (localCourse && localCourse.originalPrice),
          rating: data.rating || (localCourse && localCourse.rating) || '4.5',
          reviews: data.reviews || (localCourse && localCourse.reviews) || '0',
          learners: data.learners || (localCourse && localCourse.learners) || '0',
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
          start_date: data.start_date || (localCourse && localCourse.start_date),
          next_batch: data.next_batch || (localCourse && localCourse.next_batch),
          mode: data.mode || (localCourse && localCourse.mode),
          language: data.language || (localCourse && localCourse.language) || 'English',
          emiOptions: data.emi_options || (localCourse && localCourse.emiOptions),
          discountPercent: data.discount_percent || (localCourse && localCourse.discountPercent),
          technologies: (data.technologies_list && typeof data.technologies_list === 'string') 
            ? data.technologies_list.split(',').map(t => t.trim()).filter(t => t)
            : (data.technologies && data.technologies.length > 0) ? data.technologies : (localCourse && localCourse.technologies) || [],
          courseObjectives: (data.courseObjectives && data.courseObjectives.length > 0) ? data.courseObjectives : (localCourse && localCourse.courseObjectives) || [],
          modules: data.modules || (localCourse && localCourse.modules),
          projects: data.projects || (localCourse && localCourse.projects),
          exam_code: data.exam_code || (localCourse && localCourse.exam_code),
          exam_questions: data.exam_questions || (localCourse && localCourse.exam_questions),
          exam_duration: data.exam_duration || (localCourse && localCourse.exam_duration),
          exam_passing_score: data.exam_passing_score || (localCourse && localCourse.exam_passing_score),
          exam_format: data.exam_format || (localCourse && localCourse.exam_format),
          exam_languages: data.exam_languages || (localCourse && localCourse.exam_languages)
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

    fetch(`/api/courses`)
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
    <div className="wiki-course-detail" style={{animation: 'fadeIn 0.5s ease-out'}}>
      <SEO
        title={`${course.title} Course | Online Training`}
        description={course.overview ? course.overview.slice(0, 155) : `Enroll in ${course.title} training at TrainingProtec.`}
        keywords={`${course.title} course, ${course.title} training, online ${course.title}`}
        canonical={`/courses/${slug}`}
        ogType="article"
      />

      <style>{`
        .wiki-course-detail {
          max-width: 100%;
          margin: 0;
          padding: 0;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
          background: #f6f6f6;
          color: #202122;
          font-size: 14px;
        }
        .wiki-course-detail a { color: #0645ad; text-decoration: none; }
        .wiki-course-detail a:hover { text-decoration: underline; }
        .wiki-course-header {
          background: #fff;
          border: 1px solid #a7d7f9;
          border-radius: 2px;
          padding: 30px 35px;
          margin-bottom: 20px;
        }
        .wiki-course-header h1 {
          font-size: 32px;
          font-weight: 600;
          color: #202122;
          margin: 0 0 10px;
        }
        .wiki-section {
          background: #fff;
          border: 1px solid #a2a9b1;
          padding: 25px 30px;
          margin-bottom: 15px;
          border-radius: 2px;
        }
        .wiki-section h2 {
          font-size: 24px;
          font-weight: 600;
          border-bottom: 1px solid #a2a9b1;
          padding-bottom: 10px;
          margin-bottom: 15px;
          color: #202122;
        }
        .wiki-section h3 {
          font-size: 18px;
          font-weight: 400;
          margin: 15px 0 10px;
        }
        .wiki-section ul { margin: 0; padding-left: 20px; }
        .wiki-section li { margin-bottom: 8px; }
        .wiki-section p { margin: 0 0 10px; }
        .hero-banner {
          background: #eaecf0;
          border: 1px solid #a2a9b1;
          border-radius: 2px;
          padding: 30px;
          margin-bottom: 20px;
          text-align: center;
        }
        .hero-banner h2 { margin: 0; color: #202122; }
.stats-grid {
          display: flex;
          gap: 16px;
          margin: 25px 0;
          flex-wrap: wrap;
          justify-content: center;
        }
        .stats-card {
          background: #fff;
          border: 2px solid #e2e8f0;
          padding: 20px 25px;
          text-align: center;
          border-radius: 12px;
          font-size: 22px;
          flex: 1;
          min-width: 140px;
        }
        .stats-card strong { display: block; font-size: 26px; font-weight: 700; color: #1e293b; }
        .stats-card span { font-size: 15px; color: #64748b; font-weight: 500; }
        .stats-card svg { font-size: 24px; color: #0066cc; margin-bottom: 8px; }
        .tag-pill {
          display: inline;
          background: transparent;
          color: #0066cc;
          padding: 0;
          border-radius: 0;
          font-size: 18px;
          font-weight: 500;
          margin: 0 15px 0 0;
        }
        .curriculum-card {
          border: 1px solid #a2a9b1;
          margin-bottom: 12px;
          border-radius: 6px;
        }
        .curriculum-header {
          background: #f8f9fa;
          padding: 12px 15px;
          cursor: pointer;
          display: flex;
          justify-content: space-between;
          align-items: center;
          font-weight: 500;
        }
        .curriculum-header:hover { background: #e8f0fe; }
        .curriculum-content {
          padding: 15px;
          border-top: 1px solid #a2a9b1;
        }
        .curriculum-item {
          padding: 8px 12px;
          background: #f8f9fa;
          margin-bottom: 8px;
          border-radius: 2px;
          cursor: pointer;
        }
        .curriculum-item:hover { background: #e8f0fe; }
        .curriculum-subtopics {
          margin-left: 20px;
          padding-left: 10px;
          border-left: 2px solid #a2a9b1;
          margin-top: 8px;
        }
        .curriculum-subtopics li {
          font-size: 13px;
          color: #54595d;
          margin: 4px 0;
        }
        .project-card {
          background: #f8f9fa;
          border: 1px solid #eaecf0;
          padding: 15px;
          margin-bottom: 10px;
          border-radius: 2px;
        }
        .project-card h4 { margin: 0 0 5px; font-size: 15px; }
        .project-card p { margin: 0; font-size: 13px; color: #54595d; }
        .review-card {
          background: #f8f9fa;
          border: 1px solid #eaecf0;
          padding: 15px;
          margin-bottom: 10px;
          border-radius: 2px;
        }
        .review-card p { font-style: italic; margin: 0 0 10px; }
        .reviewer-info { display: flex; align-items: center; gap: 10px; }
        .reviewer-avatar {
          width: 32px;
          height: 32px;
          background: #a2a9b1;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          color: #fff;
          font-weight: bold;
        }
        .faq-item {
          background: #f8f9fa;
          border: 1px solid #eaecf0;
          padding: 15px;
          margin-bottom: 10px;
          border-radius: 2px;
        }
        .faq-question { font-weight: 600; margin-bottom: 8px; }
        .faq-answer { color: #54595d; }
        .cta-box {
          background: #f8f9fa;
          border: 1px solid #a2a9b1;
          padding: 20px;
          text-align: center;
          border-radius: 2px;
          margin-top: 20px;
        }
        .cta-box a {
          display: inline-block;
          background: #36c;
          color: #fff;
          padding: 10px 20px;
          border-radius: 2px;
          text-decoration: none;
        }
        .cta-box a:hover { background: #447; }
        .enrollment-form-box {
          background: #fff;
          border: 1px solid #a2a9b1;
          padding: 20px;
          border-radius: 2px;
        }
        .enrollment-form-box h3 { margin-top: 0; }
        .enrollment-form-box input,
        .enrollment-form-box select,
        .enrollment-form-box textarea {
          width: 100%;
          padding: 8px;
          border: 1px solid #a2a9b1;
          border-radius: 2px;
          margin-bottom: 10px;
          box-sizing: border-box;
        }
        .enrollment-form-box button {
          width: 100%;
          background: #36c;
          color: #fff;
          border: none;
          padding: 10px;
          border-radius: 2px;
          cursor: pointer;
        }
        .enrollment-form-box button:hover { background: #447; }
        .course-features-list {
          list-style: none;
          padding: 0;
          margin: 10px 0;
        }
        .course-features-list li {
          padding: 5px 0;
          border-bottom: 1px solid #eaecf0;
        }
      `}</style>

      {/* Hero Section - Home Page Style */}
      <section className="course-hero" style={{
        position: 'relative',
        minHeight: '92vh',
        display: 'flex',
        alignItems: 'center',
        overflow: 'hidden',
        marginTop: '-80px',
        backgroundImage: course.heroImage ? `url(${course.heroImage})` : 'linear-gradient(135deg, #0a0a23 0%, #003366 50%, #0a0a23 100%)',
        backgroundSize: 'cover',
        backgroundPosition: 'center'
      }}>
        <div style={{
          position: 'absolute',
          inset: 0,
          background: 'linear-gradient(135deg, rgba(10, 10, 35, 0.88) 0%, rgba(0, 52, 102, 0.78) 50%, rgba(10, 10, 35, 0.88) 100%)'
        }}></div>
        
        <div style={{
          position: 'relative',
          zIndex: 2,
          maxWidth: '1200px',
          margin: '0 auto',
          padding: '5rem 5% 4rem',
          width: '100%'
        }}>
          <div style={{maxWidth: '750px', animation: 'fadeUp 0.8s ease-out'}}>
            <span style={{
              display: 'inline-flex',
              alignItems: 'center',
              padding: '0.5rem 1.2rem',
              background: 'rgba(255,255,255,0.1)',
              border: '1px solid rgba(255,255,255,0.15)',
              borderRadius: '30px',
              fontSize: '0.85rem',
              color: '#fff',
              fontWeight: '500',
              marginBottom: '1.5rem'
            }}>
              <FaGraduationCap style={{marginRight: '8px', color: '#f59e0b'}} />
              Professional Certification Course
            </span>
            
            <h1 style={{
              fontFamily: 'Inter, sans-serif',
              fontSize: '3.2rem',
              fontWeight: '800',
              color: '#fff',
              lineHeight: '1.15',
              marginBottom: '1.2rem'
            }}>
              {course.title}
            </h1>
            
            {course.tagline && (
              <p style={{
                fontSize: '1.15rem',
                color: 'rgba(255,255,255,0.85)',
                lineHeight: '1.7',
                marginBottom: '1.5rem'
              }}>
                {course.tagline}
              </p>
            )}
            
            <div style={{
              display: 'flex',
              gap: '1rem',
              marginBottom: '2rem',
              flexWrap: 'wrap'
            }}>
              <span style={{display: 'flex', alignItems: 'center', gap: '8px', color: 'rgba(255,255,255,0.9)', fontSize: '0.95rem'}}>
                <FaClock style={{color: '#f59e0b'}} /> {course.duration}
              </span>
              <span style={{display: 'flex', alignItems: 'center', gap: '8px', color: 'rgba(255,255,255,0.9)', fontSize: '0.95rem'}}>
                <FaGraduationCap style={{color: '#f59e0b'}} /> {course.level}
              </span>
              <span style={{display: 'flex', alignItems: 'center', gap: '8px', color: 'rgba(255,255,255,0.9)', fontSize: '0.95rem'}}>
                <FaUsers style={{color: '#f59e0b'}} /> {typeof course.learners === 'number' ? course.learners.toLocaleString() : course.learners} Students
              </span>
              <span style={{display: 'flex', alignItems: 'center', gap: '8px', color: 'rgba(255,255,255,0.9)', fontSize: '0.95rem'}}>
                <FaStar style={{color: '#f59e0b'}} /> {course.rating} ({typeof course.reviews === 'number' ? course.reviews.toLocaleString() : course.reviews} Reviews)
              </span>
            </div>
            
            <div style={{
              display: 'flex',
              gap: '1rem',
              flexWrap: 'wrap'
            }}>
              <a href="#enroll" style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '8px',
                padding: '0.9rem 2rem',
                background: 'linear-gradient(135deg, #0066cc, #7c3aed)',
                color: '#fff',
                borderRadius: '8px',
                fontWeight: '600',
                textDecoration: 'none',
                transition: 'transform 0.3s ease'
              }}>
                Enroll Now <FaArrowRight />
              </a>
              <a href="#curriculum" style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '8px',
                padding: '0.9rem 2rem',
                background: 'rgba(255,255,255,0.1)',
                border: '1px solid rgba(255,255,255,0.3)',
                color: '#fff',
                borderRadius: '8px',
                fontWeight: '600',
                textDecoration: 'none',
                backdropFilter: 'blur(10px)'
              }}>
                View Curriculum
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Two Column Layout */}
      <div className="course-detail-container" style={{padding: '40px 20px', maxWidth: '100%', margin: '0'}}>
        {/* Left Side - Course Content (60%) */}
        <div className="course-content-left">
          {/* Header */}
          <div className="wiki-course-header" style={{animation: 'fadeIn 0.5s ease-out', padding: '25px 30px'}}>
            
            {/* Quick Info Stats Cards */}
            <div className="stats-grid">
              <div className="stats-card">
                <FaClock />
                <strong>{course.duration}</strong>
                <span>Duration</span>
              </div>
              <div className="stats-card">
                <FaGraduationCap />
                <strong>{course.level}</strong>
                <span>Level</span>
              </div>
              <div className="stats-card">
                <FaUsers />
                <strong>{typeof course.learners === 'number' ? course.learners.toLocaleString() : course.learners}</strong>
                <span>Students</span>
              </div>
              <div className="stats-card">
                <FaStar style={{color: '#f59e0b'}} />
                <strong>{course.rating}</strong>
                <span>{typeof course.reviews === 'number' ? course.reviews.toLocaleString() : course.reviews} Reviews</span>
              </div>
            </div>
          </div>

      {/* About Course */}
      {course.overview && (
      <div className="wiki-section">
        <h2>About This Course</h2>
        <p>{course.overview}</p>
      </div>
      )}

      {/* Course Objectives */}
      {course.courseObjectives && course.courseObjectives.length > 0 && (
      <div className="wiki-section">
        <h2>Course Objectives</h2>
        <ul>
          {course.courseObjectives.map((obj, idx) => (
            <li key={idx}>{obj}</li>
          ))}
        </ul>
      </div>
      )}

      {/* Why Join / Course Features */}
      {course.why_join && course.why_join.length > 0 && (
      <div className="wiki-section">
        <h2>Course Features</h2>
        <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '15px'}}>
          {course.why_join.map((item, index) => (
            <div key={index} style={{padding: '15px', background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '10px'}}>
              <h4 style={{margin: '0 0 5px', color: '#1e293b'}}>{typeof item === 'object' ? item.title : item.split(' - ')[0]}</h4>
              <p style={{margin: 0, fontSize: '14px', color: '#64748b'}}>{typeof item === 'object' ? item.description : item.split(' - ')[1] || ''}</p>
            </div>
          ))}
        </div>
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

      {/* Pre-requisites */}
      {course.eligibility && (
      <div className="wiki-section">
        <h2>Pre-requisites</h2>
        <div dangerouslySetInnerHTML={{__html: course.eligibility}} />
      </div>
      )}

      {/* Course Curriculum - Expandable */}
      {course.topicWiseContent && course.topicWiseContent.length > 0 && (
      <div className="wiki-section">
        <h2>Course Curriculum</h2>
        {course.topicWiseContent.map((group, gIndex) => (
          <div key={gIndex} className="curriculum-card">
            <div className="curriculum-header" onClick={() => setCurriculumOpen(curriculumOpen === gIndex ? -1 : gIndex)}>
              <span>Module {gIndex + 1}: {group.heading}</span>
              <FaChevronRight style={{transform: curriculumOpen === gIndex ? 'rotate(90deg)' : 'rotate(0)'}} />
            </div>
            {curriculumOpen === gIndex && group.items && group.items.length > 0 && (
              <div className="curriculum-content">
                {group.items.map((item, iIndex) => (
                  <div key={iIndex}>
                    <div className="curriculum-item" onClick={() => setSubtopicOpen(prev => ({...prev, [`${gIndex}-${iIndex}`]: prev[`${gIndex}-${iIndex}`] ? false : true}))}>
                      {item.title}
                    </div>
                    {subtopicOpen[`${gIndex}-${iIndex}`] && item.subtopics && item.subtopics.length > 0 && (
                      <ul className="curriculum-subtopics">
                        {item.subtopics.map((sub, sIndex) => (
                          <li key={sIndex}>{sub}</li>
                        ))}
                      </ul>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
      )}

      {/* Skills */}
      {course.skillsCovered && course.skillsCovered.length > 0 && (
      <div className="wiki-section">
        <h2>Skills You'll Gain</h2>
        <div style={{
          display: 'flex', 
          flexWrap: 'wrap', 
          gap: '0',
          padding: '10px 0'
        }}>
          {course.skillsCovered.map((skill, index) => (
            <span key={index} className="tag-pill" style={{
              display: 'inline-block',
              marginRight: '20px',
              marginBottom: '10px'
            }}>{skill}</span>
          ))}
        </div>
      </div>
      )}

      {/* Exam Details */}
      {(course.exam_code || course.certification) && (
      <div className="wiki-section">
        <h2>Exam Details</h2>
        <table style={{width: '100%', borderCollapse: 'collapse'}}>
          <tbody>
            <tr><td style={{padding: '8px', border: '1px solid #a2a9b1'}}><strong>Exam Code</strong></td><td style={{padding: '8px', border: '1px solid #a2a9b1'}}>{course.exam_code || 'N/A'}</td></tr>
            <tr><td style={{padding: '8px', border: '1px solid #a2a9b1'}}><strong>Questions</strong></td><td style={{padding: '8px', border: '1px solid #a2a9b1'}}>{course.exam_questions || 'N/A'}</td></tr>
            <tr><td style={{padding: '8px', border: '1px solid #a2a9b1'}}><strong>Duration</strong></td><td style={{padding: '8px', border: '1px solid #a2a9b1'}}>{course.exam_duration || 'N/A'}</td></tr>
            <tr><td style={{padding: '8px', border: '1px solid #a2a9b1'}}><strong>Passing Score</strong></td><td style={{padding: '8px', border: '1px solid #a2a9b1'}}>{course.exam_passing_score || 'N/A'}</td></tr>
            {course.exam_format && <tr><td style={{padding: '8px', border: '1px solid #a2a9b1'}}><strong>Format</strong></td><td style={{padding: '8px', border: '1px solid #a2a9b1'}}>{course.exam_format}</td></tr>}
            {course.exam_languages && <tr><td style={{padding: '8px', border: '1px solid #a2a9b1'}}><strong>Languages</strong></td><td style={{padding: '8px', border: '1px solid #a2a9b1'}}>{course.exam_languages}</td></tr>}
          </tbody>
        </table>
      </div>
      )}

      {/* Learner Reviews */}
      {course.reviewsList && course.reviewsList.length > 0 && (
      <div className="wiki-section">
        <h2>Reviews</h2>
        <div style={{display: 'grid', gap: '15px'}}>
          {course.reviewsList.map((review, index) => (
            <div key={index} className="review-card">
              <p>"{typeof review === 'object' ? review.text : review.split(' | ')[2] || ''}"</p>
              <div className="reviewer-info">
                <div className="reviewer-avatar">
                  {(typeof review === 'object' ? review.name : review.split(' | ')[0] || 'U').charAt(0)}
                </div>
                <div>
                  <strong>{typeof review === 'object' ? review.name : review.split(' | ')[0] || ''}</strong>
                  <span style={{display: 'block', color: '#54595d', fontSize: '12px'}}>{typeof review === 'object' ? review.role : review.split(' | ')[1] || ''}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
      )}

      {/* FAQ */}
      {course.faq && course.faq.length > 0 && (
      <div className="wiki-section">
        <h2>Frequently Asked Questions</h2>
        {course.faq.map((item, index) => (
          <div key={index} className="faq-item">
            <div className="faq-question">Q: {item.question || item.Q || item.q || ''}</div>
            <div className="faq-answer">A: {item.answer || item.A || item.a || ''}</div>
          </div>
        ))}
      </div>
      )}

      {/* Still Unsure */}
      <div className="cta-box">
        <h3>Still unsure?</h3>
        <p>We're just a click away!</p>
        <a href="mailto:contact@trainingprotec.com?subject=Course Inquiry">Contact Us</a>
      </div>

      {/* CTA */}
      <div className="cta-box" style={{background: '#e8f0fe', borderColor: '#36c'}}>
        <h3>Ready to Start?</h3>
        <p>Enroll in this course today and transform your career.</p>
        <a href={`mailto:contact@trainingprotec.com?subject=${encodeURIComponent(`Enrollment: ${course.title}`)}`}>
          Enroll Now - {course.price}
        </a>
      </div>

      {/* Close Left Content */}
        </div>

        {/* Right Sidebar */}
        <div className="course-sidebar-right">
          <div className="enrollment-form-box">
            <h3>Enroll Now</h3>
            <div style={{marginBottom: '15px'}}>
              <span style={{fontSize: '28px', fontWeight: 'bold', color: '#202122'}}>{course.price}</span>
              {course.originalPrice && <span style={{fontSize: '16px', color: '#72777d', textDecoration: 'line-through', marginLeft: '10px'}}>{course.originalPrice}</span>}
              {course.discountPercent && <span style={{marginLeft: '10px', background: '#36c', color: '#fff', padding: '2px 8px', borderRadius: '2px', fontSize: '12px'}}>{course.discountPercent}% OFF</span>}
            </div>

            <form onSubmit={(e) => {
              e.preventDefault();
              const formData = new FormData(e.target);
              Object.fromEntries(formData.entries());
              alert('Thank you! We will contact you soon.');
            }}>
              <input type="hidden" name="course" value={course.title} />
              <div>
                <label>Select Course</label>
                <select name="course_select" defaultValue={course.title}>
                  {allSlugs.map((c, i) => (
                    <option key={i} value={c.title}>{c.title}</option>
                  ))}
                </select>
              </div>
              <div>
                <label>Full Name *</label>
                <input type="text" name="name" required placeholder="Enter your name" />
              </div>
              <div>
                <label>Email *</label>
                <input type="email" name="email" required placeholder="Enter your email" />
              </div>
              <div>
                <label>Phone</label>
                <input type="tel" name="phone" placeholder="Enter your phone" />
              </div>
              <div>
                <label>Message</label>
                <textarea name="message" rows="3" placeholder="Any questions?"></textarea>
              </div>
              <button type="submit">Submit Enquiry</button>
            </form>

            <div style={{marginTop: '15px', paddingTop: '15px', borderTop: '1px solid #eaecf0'}}>
              <h4>Course Features</h4>
              <ul className="course-features-list">
                <li>Lifetime Access</li>
                <li>Industry Projects</li>
                <li>Certificate of Completion</li>
                <li>24/7 Support</li>
              </ul>
            </div>
          </div>

          {/* Training Schedule Box */}
          {course.trainingSchedule && (
          <div style={{background: '#fff', border: '2px solid #0066cc', borderRadius: '12px', padding: '20px', marginTop: '20px'}}>
            <h3 style={{marginTop: 0, color: '#1e293b', fontSize: '18px', borderBottom: '2px solid #0066cc', paddingBottom: '10px'}}>Upcoming Batch</h3>
            <div style={{marginBottom: '15px'}}>
              <div style={{display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px'}}>
                <span style={{width: '10px', height: '10px', borderRadius: '50%', background: '#10b981'}}></span>
                <span style={{color: '#475569', fontSize: '14px'}}>Weekdays (Mon-Fri)</span>
              </div>
              {course.start_date && (
                <div style={{fontSize: '16px', fontWeight: '600', color: '#1e293b', marginBottom: '5px'}}>
                  {course.start_date}
                </div>
              )}
              {course.trainingSchedule && (
                <div style={{fontSize: '14px', color: '#64748b'}}>
                  {course.trainingSchedule.split('\n')[0]}
                </div>
              )}
            </div>
            <div style={{borderTop: '1px solid #e2e8f0', paddingTop: '15px'}}>
              <h4 style={{margin: '0 0 10px 0', color: '#1e293b', fontSize: '14px'}}>For One to One Classes OR Corporate Training</h4>
              <div style={{display: 'flex', flexDirection: 'column', gap: '10px'}}>
                <input type="text" name="full_name" placeholder="Full Name" style={{padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px'}} />
                <input type="email" name="email_address" placeholder="Email" style={{padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px'}} />
                <input type="tel" name="phone_number" placeholder="Phone" style={{padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px'}} />
                <textarea name="message_details" placeholder="Message" rows="2" style={{padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px', resize: 'none'}}></textarea>
                <button type="button" style={{padding: '12px', background: 'linear-gradient(135deg, #0066cc, #0052a3)', color: '#fff', border: 'none', borderRadius: '8px', fontSize: '14px', fontWeight: '600', cursor: 'pointer'}}>
                  Request Demo Class
                </button>
              </div>
            </div>
          </div>
          )}
        </div>

      {/* Navigation */}
      {allSlugs.length > 1 && (
      <div style={{display: 'flex', justifyContent: 'space-between', marginTop: '30px', paddingTop: '20px', borderTop: '1px solid #e2e8f0'}}>
        {prevCourse && <Link to={`/courses/${prevCourse.slug}`} style={{color: '#0066cc', display: 'flex', alignItems: 'center', gap: '8px'}}>{"<"} {prevCourse.title}</Link>}
        {nextCourse && <Link to={`/courses/${nextCourse.slug}`} style={{color: '#0066cc', display: 'flex', alignItems: 'center', gap: '8px'}}>{nextCourse.title} {">"}</Link>}
      </div>
      )}
    </div>
  );
};

export default CourseDetail;

