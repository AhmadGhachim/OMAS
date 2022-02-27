import './App.css';
import { useState } from 'react';
import MeetingType from './components/MeetingType';
import File from './components/File';


function App() {



  return (
    <div className="App">
      <div className="header">
        <h2>
          OMAS
        </h2>
      </div>

      <MeetingType />

      <div className="meeting-documents">
        <File title="Meeting Service File" />
        <button>Ready!</button>
        <File title="Student Database File" />
      </div>

    </div>
  );
}

export default App;
