import React, { useState } from 'react';

const MeetingType = () => {

      const [selected, setSelected] = useState("zoom")

      return (
            <div>
                  <div className="meeting-type">
                        <form>
                              <label htmlFor="meet-type">Select Meeting Service:</label>
                              <select value={selected} onChange={(e) => setSelected(e.target.value)}>
                                    <option value="zoom">Zoom</option>
                                    <option value="teams">Teams</option>
                                    <option value="webex">Webex</option>
                              </select>
                        </form>
                  </div>
            </div>
      );
}

export default MeetingType;
