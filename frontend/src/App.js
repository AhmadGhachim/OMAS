import './App.css';
import { useState } from 'react';
import HomePage from './components/HomePage';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

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


  const updateCutOffNum = (num) => {
    setNum(num)
  }

  // placeholder function to handle the onclick for the Process button
  const handleProcessSubmit = (e) => {
    setIsProcessed(isProcessed => !isProcessed);
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
            />
          }
        />

      </Routes>

    </Router>

  );
}

export default App;
