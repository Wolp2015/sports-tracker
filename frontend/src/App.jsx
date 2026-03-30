import { useState } from 'react'

function App() {
  const [teamName, setTeamName] = useState("")
  const [team, setTeam] = useState(null)

  const [playerName, setPlayerName] = useState("")
  const [player, setPlayer] = useState(null)
  
  async function searchTeam() {
    const response = await fetch(`http://localhost:5000/api/team/${teamName}`)
    const data = await response.json()
    setTeam(data)
}

  async function searchPlayer() {
    const response = await fetch(`http://localhost:5000/api/player/${playerName}`)
    const data = await response.json()
    setPlayer(data)
}

  return (
    <div>
      <h1> Sports Tracker</h1>
      <input value={teamName} onChange={(e) => setTeamName(e.target.value)} />
      <button onClick={searchTeam}>Search Team</button>
      {team && (
      <div>       
          <h2>{team.name}</h2>
          <p>{team.league}</p>
          <p>{team.stadium}</p>
          <p>{team.location}</p>
          <p>{team.formed_year}</p>
      </div>
    )}

      <input value={playerName} onChange={(e) => setPlayerName(e.target.value)} />
      <button onClick={searchPlayer}>Search Player</button>
      {player && (
      <div>       
          <h2>{player.name}</h2>
          <p>{player.team}</p>
          <p>{player.nationality}</p>
          <p>{player.born}</p>
          <p>{player.status}</p>
          <p>{player.position}</p>
      </div>
    )}  
    </div>
  );
}

export default App