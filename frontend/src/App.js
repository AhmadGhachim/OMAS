import './App.css';
import { useState, useEffect, useRef } from 'react';
import MeetingType from './components/MeetingType';
import File from './components/File';
import CutOff from "./components/CutOff";
import DisplayedData from './components/DisplayedData';


function App() {

  const [num, setNum] = useState(0);

  // state to determine if the Process button should be disabled or not. (boolean value)
  const [isReady, setIsReady] = useState(true);

  // state to determine if the data has been processed and returned from the backend.(boolen value)
  const [isProcessed, setIsProcessed] = useState(false);

  // state to store the returned data from the backend. (Array of objects of students)
  const [outputData, setOutputData] = useState([
    {
      name: "Posi Adeyemi",
      duration: "37:01",
      attended: "present",
    },

    {
      name: "Ahmad Ghachim",
      duration: "37:01",
      attended: "present",
    },
  ])

  const processBtnRef = useRef(null);

  const updateCutOffNum = (num) => {
    setNum(num)
  }

  // placeholder function to allow the Process button to switch between disabled and non-disabled states.
  useEffect(() => {
    if (isReady) {
      processBtnRef.current.className = "ready"
      processBtnRef.current.disabled = false;
      // processBtnRef.current.onClick = () => handleSubmit();
    }
    else {
      processBtnRef.current.className = ""
      processBtnRef.current.disabled = true;
    }
  }, [isReady])


  // placeholder function to handle the onclick for the Process button
  const handleSubmit = (e) => {
    setIsProcessed(isProcessed => !isProcessed);
  }

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
      <CutOff cutOffNum={num} updateCutOffNum={updateCutOffNum} />

      <div className="meeting-documents">
        <File title="Meeting Service File" />
        <File title="Student Database File" />
      </div>

      <div className="Process_button">
        <button onClick={handleSubmit} ref={processBtnRef}>{isProcessed ? "Processed" : "Process"}</button>
      </div>

      {isProcessed && <DisplayedData outputData={outputData} />}

    </div>
  );
}

export default App;
