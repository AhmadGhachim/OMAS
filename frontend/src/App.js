import './App.css';
import { useEffect, useState } from 'react';
import HomePage from './components/HomePage';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CutOff from './components/CutOff';

function App() {

  const [meetingType, setMeetingType] = useState("zoom")

  const [num, setNum] = useState(0);

  const [serviceFile, setServiceFile] = useState(null);

  const [databaseFile, setDatabaseFile] = useState(null)

  // state to determine if the Process button should be disabled or not. (boolean value)
  const [isReady, setIsReady] = useState(false);

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
  const handleProcessSubmit = async (e) => {
    const uploadData = new FormData()
    uploadData.append("meetingType", meetingType)
    uploadData.append("cutOffNum", num)
    uploadData.append("serviceFile", serviceFile, serviceFile.name)
    uploadData.append("databaseFile", databaseFile, databaseFile.name)

    try {
      const res = await fetch("http://127.0.0.1:8000/api/processData", {
        method: "POST",
        body: uploadData
      })

      console.log(res)
      setIsProcessed(isProcessed => !isProcessed);
    }
    catch (error) {
      console.log(error)
    }

  }


  const handleFileStateUpdate = (title, data) => {
    console.log(data)
    if (title === "Meeting Service File") {
      setServiceFile(data)
    }
    else {
      setDatabaseFile(data)
    }
  }

  useEffect(() => {
    if (serviceFile != null && databaseFile != null) {
      setIsReady(true)
    }
    else {
      if (isReady) {
        setIsReady(false)
      }
    }
  }, [serviceFile, databaseFile])


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
              handleFileStateUpdate={handleFileStateUpdate}
            />
          }
        />

      </Routes>

    </Router>

  );
}

export default App;
