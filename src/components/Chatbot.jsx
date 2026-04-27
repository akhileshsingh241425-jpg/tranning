import React, { useState, useRef, useEffect } from 'react';
import { FaCommentDots, FaTimes, FaPaperPlane, FaRobot, FaUser, FaGraduationCap, FaEnvelope } from 'react-icons/fa';

const quickReplies = [
  "Tell me about courses",
  "Course fees & EMI options",
  "Placement assistance details",
  "Talk to a counsellor",
  "Certification details",
  "Free demo class"
];

const botResponses = {
  greeting: "Hi there! 👋 Welcome to TrainingProtec — Your Global Professional Certification Training Platform. I'm your learning assistant. How can I help you today?",
  courses: "We offer 150+ certification training programs:\n\n🔹 **Data Science & AI**\n🔹 **Cloud Computing & DevOps**\n🔹 **Cyber Security**\n🔹 **Full Stack Web Dev**\n🔹 **Digital Marketing**\n🔹 **Business Analytics**\n🔹 **UI/UX Design**\n🔹 **Project Management** & more\n\nAll courses include live classes, hands-on projects & certification support. Which domain interests you?",
  fees: "💰 **Flexible Payment Options:**\n\n✅ One-time payment with attractive discounts\n✅ EMI options available\n✅ No-cost EMI on select courses\n✅ Corporate group discounts available\n✅ Customized training packages\n\nWant me to connect you with a counsellor for the best offer?",
  placement: "🎯 **Career Support Program:**\n\n✅ Certification Exam Preparation\n✅ Resume Building & LinkedIn Optimization\n✅ Mock Interviews with Industry Experts\n✅ 1-on-1 Career Mentoring\n✅ Job Interview Preparation\n✅ Live Project Support\n\nOur team supports you throughout your learning journey! 🚀",
  counsellor: "📧 **Connect with a Career Counsellor:**\n\n🔹 **Email:** contact@trainingprotec.com\n🔹 **Response Time:** Within 24 hours (Mon-Sat)\n\nOr fill out the Contact form on our website and we'll get back to you promptly!",
  certification: "📜 **Globally Recognized Certifications:**\n\n✅ TrainingProtec Course Completion Certificate\n✅ Prep for AWS, Google, CEH, PMP & more\n✅ Globally recognized credentials\n✅ Shareable on LinkedIn\n✅ Lifetime validity\n\nOur certification programs are designed to help you stand out in the global job market!",
  demo: "🎓 **Book a Free Demo Class:**\n\nExperience our teaching methodology firsthand!\n\n✅ 1-hour live session with industry expert\n✅ Hands-on project walkthrough\n✅ Career path guidance\n✅ Q&A with the instructor\n\nFill out the Contact form or email us at **contact@trainingprotec.com** to book your free class today!",
  default: "I'd be happy to help! Here are some things I can assist with:\n\n🔹 Course information & curriculum\n🔹 Fees, EMI & scholarship details\n🔹 Placement assistance info\n🔹 Free demo class booking\n🔹 Connecting you with a counsellor\n\nJust ask me anything or choose from the quick options below! 😊"
};

const getResponse = (input) => {
  const lower = input.toLowerCase();
  if (lower.includes('course') || lower.includes('program') || lower.includes('learn') || lower.includes('train')) {
    return botResponses.courses;
  }
  if (lower.includes('fee') || lower.includes('price') || lower.includes('cost') || lower.includes('emi') || lower.includes('pay') || lower.includes('discount')) {
    return botResponses.fees;
  }
  if (lower.includes('place') || lower.includes('job') || lower.includes('hire') || lower.includes('career') || lower.includes('salary')) {
    return botResponses.placement;
  }
  if (lower.includes('call') || lower.includes('counsell') || lower.includes('talk') || lower.includes('phone') || lower.includes('contact')) {
    return botResponses.counsellor;
  }
  if (lower.includes('certif') || lower.includes('certificate')) {
    return botResponses.certification;
  }
  if (lower.includes('demo') || lower.includes('free') || lower.includes('trial') || lower.includes('class')) {
    return botResponses.demo;
  }
  if (lower.includes('hi') || lower.includes('hello') || lower.includes('hey') || lower.includes('namaste')) {
    return botResponses.greeting;
  }
  return botResponses.default;
};

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { type: 'bot', text: botResponses.greeting, time: new Date() }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, isTyping]);

  useEffect(() => {
    if (isOpen && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isOpen]);

  const sendMessage = (text) => {
    if (!text.trim()) return;

    const userMsg = { type: 'user', text: text.trim(), time: new Date() };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsTyping(true);

    setTimeout(() => {
      const response = getResponse(text);
      setMessages(prev => [...prev, { type: 'bot', text: response, time: new Date() }]);
      setIsTyping(false);
    }, 800 + Math.random() * 700);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    sendMessage(input);
  };

  const handleQuickReply = (reply) => {
    sendMessage(reply);
  };

  const formatTime = (date) => {
    return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
  };

  const formatMessage = (text) => {
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n/g, '<br />');
  };

  return (
    <div className="chatbot-wrapper">
      {/* Floating Button */}
      <button 
        className={`chatbot-toggle ${isOpen ? 'open' : ''}`}
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle chat"
      >
        {isOpen ? <FaTimes /> : <FaCommentDots />}
        {!isOpen && <span className="chatbot-badge">1</span>}
      </button>

      {/* Chat Window */}
      {isOpen && (
        <div className="chatbot-window">
          {/* Header */}
          <div className="chatbot-header">
            <div className="chatbot-header-info">
              <div className="chatbot-avatar">
                <FaGraduationCap />
              </div>
              <div>
                <h4>TrainingProtec Assistant</h4>
                <span className="chatbot-status">
                  <span className="status-dot"></span> Online — Replies instantly
                </span>
              </div>
            </div>
            <div className="chatbot-header-actions">
              <a href="mailto:contact@trainingprotec.com" className="chatbot-action-btn email" title="Email us">
                <FaEnvelope />
              </a>
              <button className="chatbot-close" onClick={() => setIsOpen(false)}>
                <FaTimes />
              </button>
            </div>
          </div>

          {/* Messages */}
          <div className="chatbot-messages">
            {messages.map((msg, index) => (
              <div key={index} className={`chatbot-msg ${msg.type}`}>
                <div className="msg-avatar">
                  {msg.type === 'bot' ? <FaRobot /> : <FaUser />}
                </div>
                <div className="msg-content">
                  <div 
                    className="msg-bubble"
                    dangerouslySetInnerHTML={{ __html: formatMessage(msg.text) }}
                  />
                  <span className="msg-time">{formatTime(msg.time)}</span>
                </div>
              </div>
            ))}
            {isTyping && (
              <div className="chatbot-msg bot">
                <div className="msg-avatar"><FaRobot /></div>
                <div className="msg-content">
                  <div className="msg-bubble typing">
                    <span className="typing-dot"></span>
                    <span className="typing-dot"></span>
                    <span className="typing-dot"></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Quick Replies */}
          <div className="chatbot-quick-replies">
            {quickReplies.map((reply, i) => (
              <button key={i} onClick={() => handleQuickReply(reply)} className="quick-reply-btn">
                {reply}
              </button>
            ))}
          </div>

          {/* Input */}
          <form className="chatbot-input" onSubmit={handleSubmit}>
            <input
              ref={inputRef}
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your question..."
              maxLength={500}
            />
            <button type="submit" disabled={!input.trim()}>
              <FaPaperPlane />
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default Chatbot;
