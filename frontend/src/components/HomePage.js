import React, { useRef, useEffect } from 'react'
import MeetingType from './MeetingType'
import CutOff from './CutOff'
import File from './File'
import DisplayedData from './DisplayedData'

function HomePage({ num, updateCutOffNum, handleProcessSubmit, isProcessed, outputData, isReady, meetingType, updateMeetingType }) {

      const processBtnRef = useRef(null);

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

                  <MeetingType meetingType={meetingType} updateMeetingType={updateMeetingType} />
                  <CutOff cutOffNum={num} updateCutOffNum={updateCutOffNum} />

                  <div className="meeting-documents">
                        <File title="Meeting Service File" />
                        <File title="Student Database File" />
                  </div>

                  <div className="Process_button">
                        <button onClick={handleProcessSubmit} ref={processBtnRef}>{isProcessed ? "Processed" : "Process"}</button>
                  </div>

                  {isProcessed && <DisplayedData outputData={outputData} />}

            </div>
      )
}

export default HomePage