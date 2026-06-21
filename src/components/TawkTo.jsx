import { useEffect } from 'react';

const TawkTo = () => {
  useEffect(() => {
    const s1 = document.createElement('script');
    const s0 = document.getElementsByTagName('script')[0];
    s1.async = true;
    s1.src = 'https://embed.tawk.to/5f2c0161ed9d9d262708b09a';
    s1.charset = 'UTF-8';
    s1.setAttribute('crossorigin', '*');
    s0.parentNode.insertBefore(s1, s0);
  }, []);

  return null;
};

export default TawkTo;
