import React, { useState } from 'react';

const WorkbookInitializer = () => {
    const [classname, setClassname] = useState("");
    const [startMonth, setStartMonth] = useState("");
    const [endMonth, setEndMonth] = useState("");
    const [filename, setFilename] = useState("");


    const handlesubmit = () => {
        console.log(classname + startMonth+ endMonth);
    
        
      }

      const handleDelete = (e) => {
        // e.preventDefault();
        e.target.files = null;
        setFilename("");
        alert("File deleted")
  }

    return (
        <div className='workbook'>
            <h1>Workbook Initializer</h1>
            <div className="cut-off">
                <label htmlFor="cut-off">Class: </label>
                <span className="cutoff-input">
                    <input type="text" placeholder="classname" onChange={(e=>{
            setClassname(e.target.value);
                    })}/>
                    <span className="select-container" placeholder="start month">
                                    <select value={startMonth} onChange={(e) => setStartMonth(e.target.value)}>
                                          <option value="January">January</option>
                                          <option value="February">February</option>
                                          <option value="March">March</option>
                                          <option value="April">April</option>
                                          <option value="May">May</option>
                                          <option value="June">June</option>
                                          <option value="July">July</option>
                                          <option value="August">August</option>
                                          <option value="September">September</option>
                                          <option value="October">October</option>
                                          <option value="November">November</option>
                                          <option value="December">December</option>
                                    </select>
                              </span>
                              <span className="select-container" placeholder="end month">
                                    <select value={endMonth} onChange={(e) => setEndMonth(e.target.value)}>
                                    <option value="January">January</option>
                                          <option value="February">February</option>
                                          <option value="March">March</option>
                                          <option value="April">April</option>
                                          <option value="May">May</option>
                                          <option value="June">June</option>
                                          <option value="July">July</option>
                                          <option value="August">August</option>
                                          <option value="September">September</option>
                                          <option value="October">October</option>
                                          <option value="November">November</option>
                                          <option value="December">December</option>
                                    </select>

                                    {classname}
                                    {startMonth}
                                    {endMonth}
                              </span>
                              <input type="file" id="service-file" accept=".text/csv,.xlsx" onChange={(e) => setFilename(e.target.files[0].name)} />
                              <button className="cancel-btn" onClick={handleDelete}>Delete file</button>
                {/* <button className="Process_button" onClick={final_cutoff}>Final cutoff</button> */}
            </span>
            </div>
            <div className='addClass'>
            <button>Add Another Class</button>
            </div>
            <button onClick={handlesubmit}>INITIALIZE</button>
        </div>
    );
}

export default WorkbookInitializer;
