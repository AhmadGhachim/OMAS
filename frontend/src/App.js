import './App.css';
import { useState } from 'react';
import MeetingType from './components/MeetingType';
import MeetingServiceFile from './components/MeetingServiceFile';


function App() {



  return (
    <div className="App">
      <div className="header">
        <h2>
          OMAS
        </h2>
      </div>

      <MeetingType />



    </div>
  );
}

export default App;
