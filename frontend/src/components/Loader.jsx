import React from 'react';

const Loader = ({ message }) => {
  return (
    <div className="loader-container">
      <div className="glow-spinner"></div>
      <div className="loader-text">{message || "Searching the cosmos..."}</div>
    </div>
  );
};

export default Loader;
