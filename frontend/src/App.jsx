import { useState } from 'react'
import SearchBar from './components/SearchBar'
import GameCard from './components/GameCard'
import Loader from './components/Loader'
import './App.css'

function App() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [hasSearched, setHasSearched] = useState(false)

  const handleSearch = async (e) => {
    e.preventDefault()
    if (!query.trim()) return

    setIsLoading(true)
    setError(null)
    setHasSearched(true)
    setResults([]) // Clear previous results

    try {
      const response = await fetch(`http://localhost:8000/search?q=${encodeURIComponent(query)}&top_k=9`)
      
      if (!response.ok) {
        throw new Error('Failed to connect to the AI Engine. Is the backend running?')
      }

      const data = await response.json()
      setResults(data.results || [])
    } catch (err) {
      setError(err.message)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <>
      <h1 className="title">Steam AI Search</h1>
      <p className="subtitle">Search 27,000+ games by passing pure vibes, not just keywords.</p>
      
      <SearchBar 
        query={query} 
        setQuery={setQuery} 
        handleSearch={handleSearch} 
      />

      {isLoading && <Loader message={`Searching for "${query}"...`} />}

      {error && (
        <div className="error-state">
          <h3>Connection Error</h3>
          <p>{error}</p>
        </div>
      )}

      {!isLoading && !error && hasSearched && results.length === 0 && (
        <div className="empty-state">
          <div className="empty-icon">🎮</div>
          <p>No matches found. Try another prompt!</p>
        </div>
      )}

      {!isLoading && !error && !hasSearched && (
        <div className="empty-state">
          <div className="empty-icon">✨</div>
          <p>Describe your ideal game to begin.</p>
        </div>
      )}

      {results.length > 0 && (
        <div className="results-grid">
          {results.map((game, index) => (
            <GameCard key={game.appid} game={game} index={index} />
          ))}
        </div>
      )}
    </>
  )
}

export default App
