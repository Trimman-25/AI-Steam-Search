import React from 'react';

const SearchBar = ({ query, setQuery, handleSearch }) => {
  return (
    <div className="search-container">
      <form onSubmit={handleSearch}>
        <input
          type="text"
          className="search-input"
          placeholder="e.g. escaping a terrifying monster in space"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit" className="search-button">
          Search
        </button>
      </form>
    </div>
  );
};

export default SearchBar;
