import React from 'react'

function DisplayedData({ outputData }) {
      return (
            <div className="displayed-data">
                  <div className="download-btn">
                        <button>
                              Download file
                        </button>
                  </div>

                  <div className="output-container">
                        <div className="heading">
                              <div className="heading-item">
                                    Name
                              </div>
                              <div className="heading-item">
                                    In-Meeting Duration
                              </div>
                              <div className="heading-item">
                                    Absent/Present
                              </div>
                        </div>

                        {outputData.map(each => (
                              <div className="content">
                                    <div className="content-item">{each.name}</div>
                                    <div className="content-item">{each.duration}</div>
                                    <div className="content-item">{each.attended}</div>
                              </div>
                        ))}
                  </div>

            </div>
      )
}

export default DisplayedData