import './App.css';
import { useState } from 'react';


function App() {
  const [selected, setSelected] = useState("zoom")
  return (
    <div className="App">
      <div className="header">
        <h2>
          OMAS
        </h2>
      </div>

      <div className="meeting-type">
        <form>
          <label htmlFor="meet-type">Select Meeting Service:</label>
          <select value={selected} onChange={(e) => setSelected(e.target.value)}>
            <option value="zoom">Zoom</option>
            <option value="teams">Teams</option>
            <option value="webex">Webex</option>
          </select>
        </form>
      </div>
    </div>
  );
}

export default App;
