import React, { useState, useEffect, useRef } from 'react';
import { FaGraduationCap, FaUsers, FaHandshake, FaChartLine, FaBriefcase, FaGlobe } from 'react-icons/fa';

const statsData = [
  { number: 150, suffix: '+', label: 'Certifications Offered', icon: FaGraduationCap },
  { number: 50, suffix: '+', label: 'Expert Trainers', icon: FaUsers },
  { number: 30, suffix: '+', label: 'Corporate Clients', icon: FaHandshake },
  { number: 95, suffix: '%', label: 'Learner Satisfaction', icon: FaChartLine },
  { number: 20, suffix: '+', label: 'Training Domains', icon: FaBriefcase },
  { number: 10, suffix: '+', label: 'Countries Served', icon: FaGlobe }
];

const formatNumber = (num) => {
  if (num >= 1000000) return (num / 100000).toFixed(0) + ',00,000';
  if (num >= 1000) return Math.floor(num).toLocaleString('en-IN');
  return Math.floor(num).toString();
};

const Stats = () => {
  const [counters, setCounters] = useState(statsData.map(() => 0));
  const [hasAnimated, setHasAnimated] = useState(false);
  const sectionRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && !hasAnimated) {
          setHasAnimated(true);
          animateCounters();
        }
      },
      { threshold: 0.3 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => observer.disconnect();
  }, [hasAnimated]);

  const animateCounters = () => {
    statsData.forEach((stat, index) => {
      let start = 0;
      const end = stat.number;
      const duration = 2000;
      const increment = end / (duration / 16);

      const timer = setInterval(() => {
        start += increment;
        if (start >= end) {
          start = end;
          clearInterval(timer);
        }
        setCounters(prev => {
          const newCounters = [...prev];
          newCounters[index] = start;
          return newCounters;
        });
      }, 16);
    });
  };

  return (
    <section className="stats-section" ref={sectionRef}>
      <div className="stats-header">
        <span className="section-badge">Our Impact</span>
        <h2 className="section-title">Trusted by <span>Professionals</span> Worldwide</h2>
        <p className="section-description">Join a growing community of learners upgrading their careers with TrainingProtec</p>
      </div>
      <div className="stats-container">
        {statsData.map((stat, index) => {
          const IconComponent = stat.icon;
          return (
            <div className="stat-item" key={index}>
              <div className="stat-icon"><IconComponent /></div>
              <span className="stat-number">
                {stat.display && counters[index] >= stat.number
                  ? stat.display
                  : formatNumber(counters[index])}
                {stat.suffix}
              </span>
              <span className="stat-label">{stat.label}</span>
            </div>
          );
        })}
      </div>
    </section>
  );
};

export default Stats;
