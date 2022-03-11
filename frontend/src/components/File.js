import React, { useEffect, useRef, useState } from 'react'

function File({ title, file, handleFileStateUpdate }) {

      const hiddenFileInput = useRef(null);

      const handleClick = (e) => {
            e.preventDefault();
            hiddenFileInput.current.click();
      }

      const handleDelete = (e) => {
            e.preventDefault();
            hiddenFileInput.current.value = "";
            handleFileStateUpdate(title, null);
            alert("File deleted");
      }

      const handleFileInputChange = async (e) => {
            const uploadedFile = e.target.files[0];
            handleFileStateUpdate(title, uploadedFile);
      }

      useEffect(() => {
            if (file) {
                  hiddenFileInput.current.disabled = true;
            }
            else {
                  hiddenFileInput.current.disabled = false;
            }
      })
      return (
            <div className="file">
                  <form>
                        <label htmlFor="service-file">{title}</label>

                        <div className="file-input-btn" onClick={handleClick}>
                              {
                                    file &&
                                    <div className="file-info">
                                          <p>{file.name}</p>
                                          <button className="cancel-btn" onClick={handleDelete}>X</button>
                                    </div>
                              }

                              <p>Click to Upload</p>
                        </div>

                        <input ref={hiddenFileInput} type="file" id="service-file" accept=".txt,.xlsx,.csv" style={{ display: "none" }} onChange={handleFileInputChange} />
                  </form>
            </div>
      )
}

export default File