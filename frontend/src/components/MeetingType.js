import React, { useState } from 'react';

const MeetingType = ({ meetingType, updateMeetingType }) => {


      return (
            <div>
                  <div className="meeting-type">
                        <form>
                              <label htmlFor="meet-type">Select Meeting Service:</label>
                              <span className="select-container">
                                    <select value={meetingType} onChange={(e) => updateMeetingType(e.target.value)}>
                                          <option value="zoom">Zoom</option>
                                          <option value="teams">Teams</option>
                                          <option value="webex">Webex</option>
                                          <option value="skype">Skype</option>
                                    </select>
                              </span>

                        </form>
                  </div>
            </div>
      );
}

export default MeetingType;
