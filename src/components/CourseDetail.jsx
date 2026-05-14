import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { FaClock, FaGraduationCap, FaStar, FaUsers, FaChevronRight, FaSpinner, FaArrowLeft, FaBook, FaCertificate, FaLaptop } from 'react-icons/fa';
import coursesDetailData from './courseData';
import SEO from './SEO';

const CourseDetail = () => {
  const { slug } = useParams();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [allSlugs, setAllSlugs] = useState([]);
  const [curriculumOpen, setCurriculumOpen] = useState(0);
  const [subtopicOpen, setSubtopicOpen] = useState({});
  const [showSchedule, setShowSchedule] = useState(true);
  const [showCorporate, setShowCorporate] = useState(false);

  useEffect(() => {
    window.scrollTo(0, 0);
    setLoading(true);

    fetch(`/api/courses/${slug}`)
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
      <div style={{ textAlign: 'center', padding: '5rem 2rem' }}>
        <FaSpinner style={{ fontSize: '2rem', color: '#0066cc', animation: 'spin 1s linear infinite' }} />
        <p style={{ marginTop: '1rem', color: '#64748b' }}>Loading course...</p>
      </div>
    );
  }

  if (!course) {
    return (
      <div style={{ textAlign: 'center', padding: '5rem 2rem' }}>
        <h2>Course Not Found</h2>
        <p>The course you are looking for does not exist.</p>
        <Link to="/" style={{ color: '#0066cc' }}>Back to Home</Link>
      </div>
    );
  }

  const currentIndex = allSlugs.findIndex(c => c.slug === slug);
  const prevCourse = allSlugs.length > 0 ? allSlugs[(currentIndex - 1 + allSlugs.length) % allSlugs.length] : null;
  const nextCourse = allSlugs.length > 0 ? allSlugs[(currentIndex + 1) % allSlugs.length] : null;

  return (
    <div style={{ width: '100%', margin: 0, padding: 0, fontFamily: 'Inter, Arial, sans-serif', background: '#f8fafc', color: '#202122', fontSize: '16px', lineHeight: '1.8' }}>
      <SEO
        title={`${course.title} Course | Online Training`}
        description={course.overview ? course.overview.slice(0, 155) : `Enroll in ${course.title} training at TrainingProtec.`}
        keywords={`${course.title} course, ${course.title} training, online ${course.title}`}
        canonical={`/courses/${slug}`}
        ogType="article"
      />

      {/* Hero Section */}
      <div style={{
        background: course.heroImage ? `url(${course.heroImage})` : 'linear-gradient(135deg, #0a0a23 0%, #003366 50%, #0a0a23 100%)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        padding: '80px 5%',
        color: '#fff',
        position: 'relative'
      }}>
        <div style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.6)' }}></div>
        <div style={{ position: 'relative', maxWidth: '1200px', margin: '0 auto' }}>
          <Link to="/" style={{ color: '#fff', display: 'inline-flex', alignItems: 'center', gap: '8px', marginBottom: '20px' }}>
            <FaArrowLeft /> Back to Courses
          </Link>
          <h1 style={{
            fontSize: '2.5rem',
            fontWeight: '700',
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
          
          <a href="#enroll" style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '8px',
            padding: '0.9rem 2rem',
            background: 'linear-gradient(135deg, #0066cc, #7c3aed)',
            color: '#fff',
            borderRadius: '8px',
            fontWeight: '600',
            textDecoration: 'none'
          }}>
            Enroll Now
          </a>
        </div>
      </div>

      {/* Breadcrumb */}
      <div style={{ padding: '16px 5%', background: '#f1f5f9', borderBottom: '1px solid #e2e8f0' }}>
        <div style={{ maxWidth: '1400px', margin: '0 auto' }}>
          <nav style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '14px', color: '#64748b' }}>
            <Link to="/" style={{ color: '#0066cc', textDecoration: 'none' }}>Home</Link>
            <span style={{ color: '#94a3b8' }}>/</span>
            <span style={{ color: '#94a3b8' }}>Courses</span>
            <span style={{ color: '#94a3b8' }}>/</span>
            <span style={{ color: '#1e293b', fontWeight: '600' }}>{course.title}</span>
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <div style={{ padding: '40px 5%', maxWidth: '1400px', margin: '0 auto' }}>
        <div style={{ display: 'flex', gap: '40px', alignItems: 'flex-start' }}>
          {/* Left Content */}
          <div style={{ flex: '1', minWidth: 0 }}>
          {/* Quick Info Stats Cards */}
          <div style={{
            display: 'flex',
            gap: '16px',
            margin: '25px 0',
            flexWrap: 'wrap',
            justifyContent: 'center'
          }}>
            <div style={{
              background: '#fff',
              border: '2px solid #e2e8f0',
              padding: '20px 25px',
              textAlign: 'center',
              borderRadius: '12px',
              flex: 1,
              minWidth: '140px'
            }}>
              <FaClock style={{ fontSize: '24px', color: '#0066cc', marginBottom: '8px' }} />
              <strong style={{ display: 'block', fontSize: '26px', fontWeight: '700', color: '#1e293b' }}>{course.duration}</strong>
              <span style={{ fontSize: '15px', color: '#64748b', fontWeight: '500' }}>Duration</span>
            </div>
            <div style={{
              background: '#fff',
              border: '2px solid #e2e8f0',
              padding: '20px 25px',
              textAlign: 'center',
              borderRadius: '12px',
              flex: 1,
              minWidth: '140px'
            }}>
              <FaGraduationCap style={{ fontSize: '24px', color: '#0066cc', marginBottom: '8px' }} />
              <strong style={{ display: 'block', fontSize: '26px', fontWeight: '700', color: '#1e293b' }}>{course.level}</strong>
              <span style={{ fontSize: '15px', color: '#64748b', fontWeight: '500' }}>Level</span>
            </div>
            <div style={{
              background: '#fff',
              border: '2px solid #e2e8f0',
              padding: '20px 25px',
              textAlign: 'center',
              borderRadius: '12px',
              flex: 1,
              minWidth: '140px'
            }}>
              <FaUsers style={{ fontSize: '24px', color: '#0066cc', marginBottom: '8px' }} />
              <strong style={{ display: 'block', fontSize: '26px', fontWeight: '700', color: '#1e293b' }}>{typeof course.learners === 'number' ? course.learners.toLocaleString() : course.learners}</strong>
              <span style={{ fontSize: '15px', color: '#64748b', fontWeight: '500' }}>Students</span>
            </div>
<div style={{
              background: '#fff',
              border: '1px solid #e2e8f0',
              padding: '20px 25px',
              textAlign: 'center',
              borderRadius: '12px',
              flex: 1,
              minWidth: '140px'
            }}>
              <FaStar style={{ fontSize: '24px', color: '#f59e0b', marginBottom: '8px' }} />
              <strong style={{ display: 'block', fontSize: '26px', fontWeight: '700', color: '#1e293b' }}>{course.rating}</strong>
              <span style={{ fontSize: '15px', color: '#64748b', fontWeight: '500' }}>{typeof course.reviews === 'number' ? course.reviews.toLocaleString() : course.reviews} Reviews</span>
            </div>
          </div>

          {/* Course Features Bar */}
          <div style={{ display: 'flex', gap: '12px', marginBottom: '25px', flexWrap: 'wrap' }}>
            {course.mode && (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: '#fff', border: '1px solid #e2e8f0', padding: '10px 18px', borderRadius: '10px', flex: 1, minWidth: '150px' }}>
                <FaLaptop style={{ color: '#0066cc', fontSize: '18px' }} />
                <span style={{ fontSize: '15px', color: '#475569' }}><strong style={{ color: '#1e293b' }}>Mode:</strong> {course.mode}</span>
              </div>
            )}
            {course.language && (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: '#fff', border: '1px solid #e2e8f0', padding: '10px 18px', borderRadius: '10px', flex: 1, minWidth: '150px' }}>
                <FaBook style={{ color: '#0066cc', fontSize: '18px' }} />
                <span style={{ fontSize: '15px', color: '#475569' }}><strong style={{ color: '#1e293b' }}>Language:</strong> {course.language}</span>
              </div>
            )}
            {course.certification && (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: '#fff', border: '1px solid #e2e8f0', padding: '10px 18px', borderRadius: '10px', flex: 1, minWidth: '150px' }}>
                <FaCertificate style={{ color: '#0066cc', fontSize: '18px' }} />
                <span style={{ fontSize: '15px', color: '#475569' }}>Certificate</span>
              </div>
            )}
          </div>

          {/* About Course */}
          {course.overview && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>About This Course</h2>
            <p style={{ color: '#475569', fontSize: '16px', lineHeight: '1.75' }}>{course.overview}</p>
          </div>
          )}

          {/* Course Objectives */}
          {course.courseObjectives && course.courseObjectives.length > 0 && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>Course Objectives</h2>
            <ul style={{ paddingLeft: '25px', color: '#475569' }}>
              {course.courseObjectives.map((obj, idx) => (
                <li key={idx} style={{ marginBottom: '8px' }}>{obj}</li>
              ))}
            </ul>
          </div>
          )}

          {/* Course Features */}
          {course.why_join && course.why_join.length > 0 && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>Course Features</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '15px' }}>
              {course.why_join.map((item, index) => (
                <div key={index} style={{ padding: '15px', background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '10px' }}>
                  <h4 style={{ margin: '0 0 5px', color: '#1e293b' }}>{typeof item === 'object' ? item.title : item.split(' - ')[0]}</h4>
                  <p style={{ margin: 0, fontSize: '14px', color: '#64748b' }}>{typeof item === 'object' ? item.description : item.split(' - ')[1] || ''}</p>
                </div>
              ))}
            </div>
          </div>
          )}

          {/* What You'll Learn */}
          {course.keyBenefits && course.keyBenefits.length > 0 && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>What You'll Learn</h2>
            <ul style={{ paddingLeft: '25px', color: '#475569' }}>
              {course.keyBenefits.map((benefit, index) => (
                <li key={index} style={{ marginBottom: '8px' }}>{benefit}</li>
              ))}
            </ul>
          </div>
          )}

          {/* Pre-requisites */}
          {course.eligibility && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>Pre-requisites</h2>
            <div dangerouslySetInnerHTML={{ __html: course.eligibility }} />
          </div>
          )}

          {/* Course Curriculum */}
          {course.topicWiseContent && course.topicWiseContent.length > 0 && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>Course Curriculum</h2>
            {course.topicWiseContent.map((group, gIndex) => (
              <div key={gIndex} style={{ border: '1px solid #a2a9b1', marginBottom: '12px', borderRadius: '6px', overflow: 'hidden' }}>
                <div 
                  style={{ background: '#f8f9fa', padding: '12px 15px', cursor: 'pointer', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}
                  onClick={() => setCurriculumOpen(curriculumOpen === gIndex ? -1 : gIndex)}
                >
                  <span>Module {gIndex + 1}: {group.heading}</span>
                  <FaChevronRight style={{ transform: curriculumOpen === gIndex ? 'rotate(90deg)' : 'rotate(0)', transition: 'transform 0.3s' }} />
                </div>
                {curriculumOpen === gIndex && group.items && group.items.length > 0 && (
                  <div style={{ padding: '15px' }}>
                    {group.items.map((item, iIndex) => (
                      <div key={iIndex}>
                        <div 
                          style={{ padding: '8px', cursor: 'pointer', background: '#fff', border: '1px solid #eaecf0', marginBottom: '5px', borderRadius: '4px' }}
                          onClick={() => setSubtopicOpen(prev => ({...prev, [`${gIndex}-${iIndex}`]: prev[`${gIndex}-${iIndex}`] ? false : true}))}
                        >
                          {item.title}
                        </div>
                        {subtopicOpen[`${gIndex}-${iIndex}`] && item.subtopics && item.subtopics.length > 0 && (
                          <ul style={{ marginLeft: '20px', color: '#54595d', fontSize: '14px' }}>
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
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>Skills You'll Gain</h2>
            <div style={{ display: 'flex', flexWrap: 'wrap', padding: '10px 0' }}>
              {course.skillsCovered.map((skill, index) => (
                <span key={index} style={{ display: 'inline-block', marginRight: '20px', marginBottom: '10px', color: '#0066cc', fontSize: '18px', fontWeight: '500' }}>{skill}</span>
              ))}
            </div>
          </div>
          )}

          {/* Exam Details */}
          {(course.exam_code || course.certification) && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>Exam Details</h2>
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <tbody>
                <tr><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}><strong>Exam Code</strong></td><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}>{course.exam_code || 'N/A'}</td></tr>
                <tr><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}><strong>Questions</strong></td><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}>{course.exam_questions || 'N/A'}</td></tr>
                <tr><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}><strong>Duration</strong></td><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}>{course.exam_duration || 'N/A'}</td></tr>
                <tr><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}><strong>Passing Score</strong></td><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}>{course.exam_passing_score || 'N/A'}</td></tr>
                {course.exam_format && <tr><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}><strong>Format</strong></td><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}>{course.exam_format}</td></tr>}
                {course.exam_languages && <tr><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}><strong>Languages</strong></td><td style={{ padding: '8px', border: '1px solid #e2e8f0' }}>{course.exam_languages}</td></tr>}
              </tbody>
            </table>
          </div>
          )}

          {/* Reviews */}
          {course.reviewsList && course.reviewsList.length > 0 && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>Reviews</h2>
            {course.reviewsList.map((review, index) => (
              <div key={index} style={{ border: '1px solid #e2e8f0', padding: '18px', marginBottom: '14px', background: '#fafafa', borderRadius: '10px' }}>
                <p>"{typeof review === 'object' ? review.text : review.split(' | ')[2] || ''}"</p>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginTop: '10px' }}>
                  <div style={{
                    width: '32px',
                    height: '32px',
                    borderRadius: '50%',
                    background: '#a2a9b1',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: '#fff',
                    fontWeight: 'bold'
                  }}>
                    {(typeof review === 'object' ? review.name : review.split(' | ')[0] || 'U').charAt(0)}
                  </div>
                  <div>
                    <strong>{typeof review === 'object' ? review.name : review.split(' | ')[0] || ''}</strong>
                    <span style={{ display: 'block', color: '#64748b', fontSize: '14px' }}>{typeof review === 'object' ? review.role : review.split(' | ')[1] || ''}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
          )}

          {/* FAQ */}
          {course.faq && course.faq.length > 0 && (
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', padding: '25px', marginBottom: '18px', borderRadius: '12px' }}>
            <h2 style={{ fontFamily: 'Poppins, sans-serif', fontSize: '26px', fontWeight: '600', color: '#1e293b', marginTop: 0, paddingBottom: '10px', borderBottom: '2px solid #e2e8f0' }}>Frequently Asked Questions</h2>
            {course.faq.map((item, index) => (
              <div key={index} style={{ marginBottom: '12px', border: '1px solid #e2e8f0', borderRadius: '10px', overflow: 'hidden' }}>
                <div style={{ background: 'linear-gradient(135deg, #f8fafc, #f1f5f9)', padding: '16px 20px', fontWeight: '600', color: '#1e293b', fontSize: '16px' }}>Q: {item.question || item.Q || item.q || ''}</div>
                <div style={{ padding: '18px 20px', color: '#475569', fontSize: '15px' }}>A: {item.answer || item.A || item.a || ''}</div>
              </div>
            ))}
          </div>
          )}

          {/* Still Unsure */}
          <div style={{ background: '#f8f9fa', border: '1px solid #a2a9b1', padding: '20px', textAlign: 'center', borderRadius: '6px', marginTop: '20px' }}>
            <h3>Still unsure?</h3>
            <p>We're just a click away!</p>
            <a href="mailto:contact@trainingprotec.com?subject=Course Inquiry">Contact Us</a>
          </div>

          {/* CTA */}
          <div style={{ background: '#e8f0fe', border: '1px solid #36c', padding: '20px', textAlign: 'center', borderRadius: '6px', marginTop: '20px' }}>
            <h3>Ready to Start?</h3>
            <p>Enroll in this course today and transform your career.</p>
            <a href={`mailto:contact@trainingprotec.com?subject=${encodeURIComponent(`Enrollment: ${course.title}`)}`}>
              Enroll Now - {course.price}
            </a>
          </div>
        </div>

        {/* Right Sidebar */}
        <div style={{ flex: '0 0 30%', position: 'sticky', top: '20px', alignSelf: 'flex-start' }}>
          {/* Enroll Now Card */}
          <div style={{ background: '#fff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '24px', marginBottom: '20px' }}>
            <h3 style={{ margin: '0 0 16px 0', fontSize: '22px', fontWeight: '700', color: '#1e293b', fontFamily: 'Poppins, sans-serif' }}>Enroll Now</h3>
            
            <div style={{ marginBottom: '18px', display: 'flex', alignItems: 'baseline', gap: '12px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '32px', fontWeight: '800', color: '#0066cc' }}>{String(course.price).replace('$','')}</span>
              {course.originalPrice && (
                <>
                  <span style={{ fontSize: '18px', color: '#94a3b8', textDecoration: 'line-through' }}>{String(course.originalPrice).replace('$','')}</span>
                  <span style={{ background: '#dcfce7', color: '#16a34a', padding: '4px 10px', borderRadius: '20px', fontSize: '13px', fontWeight: '600' }}>
                    {Math.round((1 - (parseInt(String(course.price).replace(/\D/g,'')) || 0) / (parseInt(String(course.originalPrice).replace(/\D/g,'')) || 1)) * 100)}% OFF
                  </span>
                </>
              )}
            </div>

            <form onSubmit={(e) => {
              e.preventDefault();
              alert('Thank you! We will contact you soon.');
            }}>
              <input type="hidden" name="course" value={course.title} />
              <div style={{ marginBottom: '12px' }}>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: '600', color: '#475569', marginBottom: '6px' }}>Select Course</label>
                <select name="course_select" defaultValue={course.title} style={{ width: '100%', padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px', color: '#1e293b', background: '#f8fafc' }}>
                  {allSlugs.map((c, i) => (
                    <option key={i} value={c.title}>{c.title}</option>
                  ))}
                </select>
              </div>
              <div style={{ marginBottom: '12px' }}>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: '600', color: '#475569', marginBottom: '6px' }}>Full Name <span style={{ color: '#ef4444' }}>*</span></label>
                <input type="text" name="name" required placeholder="Enter your name" style={{ width: '100%', padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px' }} />
              </div>
              <div style={{ marginBottom: '12px' }}>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: '600', color: '#475569', marginBottom: '6px' }}>Email <span style={{ color: '#ef4444' }}>*</span></label>
                <input type="email" name="email" required placeholder="Enter your email" style={{ width: '100%', padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px' }} />
              </div>
              <div style={{ marginBottom: '12px' }}>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: '600', color: '#475569', marginBottom: '6px' }}>Phone</label>
                <input type="tel" name="phone" placeholder="Enter your phone" style={{ width: '100%', padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px' }} />
              </div>
              <div style={{ marginBottom: '14px' }}>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: '600', color: '#475569', marginBottom: '6px' }}>Message</label>
                <textarea name="message" rows="2" placeholder="Any questions?" style={{ width: '100%', padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px', resize: 'none' }}></textarea>
              </div>

              <div style={{ padding: '16px', background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '10px', marginBottom: '14px' }}>
                <div 
                  onClick={() => setShowSchedule(!showSchedule)}
                  style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer', marginBottom: showSchedule ? '12px' : 0 }}
                >
                  <h4 style={{ margin: 0, fontSize: '15px', fontWeight: '700', color: '#1e293b' }}>Training Schedule</h4>
                  <span style={{ fontSize: '18px', fontWeight: '700', color: '#0066cc', width: '24px', height: '24px', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#e0f2fe', borderRadius: '6px' }}>{showSchedule ? '-' : '+'}</span>
                </div>
                {showSchedule && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#10b981', flexShrink: 0 }}></span>
                      <span style={{ fontSize: '13px', color: '#475569' }}>Weekend (Sat-Sun): <strong style={{ color: '#1e293b' }}>{course.start_date || 'Every Saturday'}</strong></span>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#10b981', flexShrink: 0 }}></span>
                      <span style={{ fontSize: '13px', color: '#475569' }}>Weekdays (Mon-Fri): <strong style={{ color: '#1e293b' }}>{course.start_date || 'Every Monday'}</strong></span>
                    </div>
                    <div style={{ fontSize: '12px', color: '#64748b', marginLeft: '16px' }}>
                      {course.trainingSchedule ? course.trainingSchedule.replace(/\n/g, ' | ') : '07:00 PM - 10:00 PM IST'}
                    </div>
                  </div>
                )}
              </div>

              <button type="submit" style={{ width: '100%', background: 'linear-gradient(135deg, #0066cc, #0052a3)', color: '#fff', border: 'none', padding: '12px', borderRadius: '8px', fontSize: '15px', fontWeight: '600', cursor: 'pointer', marginBottom: '10px' }}>
                Submit Enquiry
              </button>
            </form>

            <div style={{ marginTop: '16px', paddingTop: '14px', borderTop: '1px solid #f1f5f9' }}>
              <div style={{ marginBottom: '12px' }}>
                <h4 style={{ margin: '0 0 12px 0', fontSize: '15px', fontWeight: '600', color: '#1e293b' }}>Course Features</h4>
                <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                  {['Lifetime Access', 'Industry Projects', 'Certificate of Completion', '24/7 Support'].map((item) => (
                    <li key={item} style={{ padding: '6px 0', borderBottom: '1px solid #f1f5f9', fontSize: '14px', color: '#475569', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ color: '#16a34a', fontSize: '16px' }}>&#10003;</span> {item}
                    </li>
                  ))}
                </ul>
              </div>

              <div 
                onClick={() => setShowCorporate(!showCorporate)}
                style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer' }}
              >
                <h4 style={{ margin: '0', fontSize: '15px', fontWeight: '600', color: '#1e293b' }}>For One to One Classes OR Corporate Training</h4>
                <span style={{ fontSize: '18px', fontWeight: '700', color: '#0066cc', width: '24px', height: '24px', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#e0f2fe', borderRadius: '6px', flexShrink: 0 }}>{showCorporate ? '-' : '+'}</span>
              </div>
              {showCorporate && (
              <form onSubmit={(e) => {
                e.preventDefault();
                alert('Thank you! Our team will contact you soon.');
              }} style={{ marginTop: '12px' }}>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  <input type="text" name="corp_name" placeholder="Full Name" style={{ padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px' }} />
                  <input type="email" name="corp_email" placeholder="Email" style={{ padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px' }} />
                  <input type="tel" name="corp_phone" placeholder="Phone" style={{ padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px' }} />
                  <textarea name="corp_message" placeholder="Message" rows="2" style={{ padding: '10px 12px', border: '1px solid #e2e8f0', borderRadius: '8px', fontSize: '14px', resize: 'none' }}></textarea>
                  <button type="submit" style={{ padding: '12px', background: '#f8fafc', color: '#0066cc', border: '2px solid #0066cc', borderRadius: '8px', fontSize: '14px', fontWeight: '600', cursor: 'pointer' }}>
                    Request Demo Class
                  </button>
                </div>
              </form>
              )}
            </div>
          </div>
        </div>
        </div>
      </div>
    </div>
  );
};

export default CourseDetail;