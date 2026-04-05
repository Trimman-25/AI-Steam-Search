import React from 'react';

const GameCard = ({ game, index }) => {
  // Staggered animation delay
  const style = {
    animationDelay: `${index * 0.1}s`
  };

  // Convert genres string (e.g. "Action, RPG") to array for mapping
  const genresList = game.genres ? game.genres.split(',').map(g => g.trim()) : [];

  return (
    <a 
      href={`https://store.steampowered.com/app/${game.appid}`} 
      target="_blank" 
      rel="noopener noreferrer" 
      className="game-card"
      style={style}
    >
      <div className="card-score">
        {(game.score).toFixed(2)} Match
      </div>
      
      <div className="card-content">
        <h3 className="card-title">{game.title}</h3>
        
        <div className="card-genres">
          {genresList.slice(0, 3).map((genre, i) => (
            <span key={i} className="genre-tag">{genre}</span>
          ))}
          {genresList.length > 3 && <span className="genre-tag">+{genresList.length - 3}</span>}
        </div>
        
        <p className="card-desc">{game.description}</p>
      </div>
    </a>
  );
};

export default GameCard;
