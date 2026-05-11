import React from 'react';
import { 
  FaCertificate, 
  FaChalkboardTeacher, 
  FaProjectDiagram, 
  FaHeadset, 
  FaRedo,
  FaUserTie,
  FaLaptopCode
} from 'react-icons/fa';

const featuresData = [
  {
    icon: <FaChalkboardTeacher />,
    title: "Live Instructor-Led Classes",
    description: "Learn from industry practitioners with 10+ years experience in live interactive sessions — not just recorded videos."
  },
  {
    icon: <FaProjectDiagram />,
    title: "Real Industry Projects",
    description: "Work on 10-15 industry-grade projects per course using real datasets and scenarios from top companies."
  },
  {
    icon: <FaCertificate />,
    title: "Industry Certifications",
    description: "Earn certificates recognized by 200+ employers. Prep included for AWS, Google, CEH & other certifications."
  },
  {
    icon: <FaLaptopCode />,
    title: "Hands-On Lab Access",
    description: "24/7 access to cloud labs, coding environments, and sandboxes for practice — no setup required."
  },
  {
    icon: <FaHeadset />,
    title: "24/7 Learning Support",
    description: "Get help anytime with dedicated mentors, doubt resolution sessions, and an active learner community."
  },
  {
    icon: <FaRedo />,
    title: "Lifetime Free Re-access",
    description: "Attend unlimited batches for free. Course content is updated regularly to match industry demands."
  },
  {
    icon: <FaUserTie />,
    title: "1-on-1 Career Mentoring",
    description: "Personal career mentors for resume building, LinkedIn optimization, mock interviews & salary negotiation."
  }
];

const Features = () => {
  return (
    <section className="features" id="features">
      <div className="section-header">
        <span className="section-badge">Why TrainingProtec</span>
        <h2 className="section-title">
          The TrainingProtec <span>Advantage</span>
        </h2>
        <p className="section-description">
          We don't just teach — we transform careers with placement-focused training, live classes, and real-world projects.
        </p>
      </div>

      <div className="features-grid">
        {featuresData.map((feature, index) => (
          <div className={`feature-card ${feature.highlight ? 'feature-highlight' : ''}`} key={index}>
            <div className="feature-icon">
              {feature.icon}
            </div>
            <h3>{feature.title}</h3>
            <p>{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Features;
