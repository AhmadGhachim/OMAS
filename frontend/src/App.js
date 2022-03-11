import './App.css';
import { useEffect, useState } from 'react';
import HomePage from './components/HomePage';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {

  const [meetingType, setMeetingType] = useState("zoom")

  const [num, setNum] = useState(0);

  const [serviceFile, setServiceFile] = useState(null);

  const [databaseFile, setDatabaseFile] = useState(null)

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


  const updateCutOffNum = (num) => {
    setNum(num)
  }

  const updateMeetingType = (newMeetingType) => {
    setMeetingType(newMeetingType);
  }

  // placeholder function to handle the onclick for the Process button
  const handleProcessSubmit = (e) => {
    setIsProcessed(isProcessed => !isProcessed);
  }

  // const handleFileInputChange = (e, title) => {
  //   // e.preventDefault();
  //   // const reader = new FileReader();
  //   // reader.onload = () => {
  //   //   console.log(reader.result)
  //   //   var blocks = reader.result.split(";");
  //   //   console.log(blocks)
  //   //   const realData = blocks[1].split(",")[1];
  //   //   console.log(realData)
  //   //   handleFileStateUpdate(title, realData);
  //   // }
  //   // reader.onerror = (error) => console.error(error);
  //   // reader.readAsDataURL(e.target.files[0]);

  //   e.preventDefault();
  //   console.log(e.target.files[0])
  //   handleFileStateUpdate(title, e.target.files[0])
  // }

  const handleFileStateUpdate = (title, data) => {
    console.log(data)
    if (title === "Meeting Service File") {
      setServiceFile(data)
    }
    else {
      setDatabaseFile(data)
    }
  }


  return (
    <Router>

      <Routes>
        <Route path="/"
          element={
            <HomePage num={num}
              updateCutOffNum={updateCutOffNum}
              handleProcessSubmit={handleProcessSubmit}
              isProcessed={isProcessed}
              outputData={outputData}
              isReady={isReady}
              meetingType={meetingType}
              updateMeetingType={updateMeetingType}
              serviceFile={serviceFile}
              databaseFile={databaseFile}
              // handleFileInputChange={handleFileInputChange}
              handleFileStateUpdate={handleFileStateUpdate}
            />
          }
        />

      </Routes>

    </Router>

  );
}

export default App;
