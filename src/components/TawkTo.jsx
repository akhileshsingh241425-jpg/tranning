import { useEffect } from 'react';

const TawkTo = () => {
  useEffect(() => {
    const propertyId = process.env.REACT_APP_TAWK_ID;
    if (!propertyId) return;

    const s1 = document.createElement('script');
    const s0 = document.getElementsByTagName('script')[0];
    s1.async = true;
    s1.src = `https://embed.tawk.to/${propertyId}`;
    s1.charset = 'UTF-8';
    s1.setAttribute('crossorigin', '*');
    s0.parentNode.insertBefore(s1, s0);
  }, []);

  return null;
};

export default TawkTo;
