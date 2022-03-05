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
                              <div className="heading-item name-column">
                                    Name
                              </div>
                              <div className="heading-item duration-column">
                                    In-Meeting Duration
                              </div>
                              <div className="heading-item attended-column">
                                    Absent/Present
                              </div>
                        </div>

                        <div className="content">
                              <div className="content-item name-column">Posi Adeyemi</div>
                              <div className="content-item duration-column">37:01</div>
                              <div className="content-item attended-column">present</div>
                        </div>

                        <div className="content">
                              <div className="content-item name-column">Ahmad Ghachim</div>
                              <div className="content-item duration-column">37:01</div>
                              <div className="content-item attended-column">present</div>
                        </div>
                  </div>

            </div>
      )
}

export default DisplayedData