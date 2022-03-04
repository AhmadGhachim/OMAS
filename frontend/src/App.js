import './App.css';
import { useState } from 'react';
import MeetingType from './components/MeetingType';
import File from './components/File';
import CutOff from "./components/CutOff";


function App() {



  return (
    <div className="App">
      <div className="header">
        <h2>
          OMAS
        </h2>
          <h3>
              An attendance system for online meeting platforms (Zoom, Teams etc.) which uses meeting reports generated
              by these services and automatically organises it in a database for the user.
          </h3>
      </div>
          <div className="steps">
              <ol className="inside-steps" >
                  <li>Select a meeting service that matches your platform.</li>
                  <li>
                      Select cutoff (Time required to be in meeting to be marked as present).
                  </li>
                  <li>
                      Upload the meeting service file provided by the platform.
                  </li>
                  <li>
                      Upload a file containing the student database.
                  </li>
                  <li>
                      Click the process button when steps 1 to 4 are done!
                  </li>
              </ol>

          </div>

        <MeetingType />
        <CutOff />

      <div className="meeting-documents">
        <File title="Meeting Service File" />
        <File title="Student Database File" />
      </div>

      <div className="Process_button">
          <button>Process</button>
      </div>




    </div>
  );
}

export default App;
