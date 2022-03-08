import React, { useRef, useState } from 'react'

function File({ title }) {

      const [filename, setFilename] = useState("");

      const hiddenFileInput = useRef(null);

      const handleClick = (e) => {
            e.preventDefault();
            hiddenFileInput.current.click();
      }

      const handleDelete = (e) => {
            e.preventDefault();
            e.target.files = null;
            setFilename("");
            alert("File deleted")
      }

      const handleFileInputChange = (e) => {
            const uploadedFile = e.target.files[0];
            setFilename(uploadedFile.name);
      }

      return (
            <div className="file">
                  <form>
                        <label htmlFor="service-file">{title}</label>

                        <div className="file-input-btn" onClick={handleClick}>
                              {
                                    filename !== "" &&
                                    <div className="file-info">
                                          <p>{filename}</p>
                                          <button className="cancel-btn" onClick={handleDelete}>X</button>
                                    </div>
                              }

                              <p>Click to Upload</p>
                        </div>

                        <input ref={hiddenFileInput} type="file" id="service-file" accept=".text/csv, xlsx" style={{ display: "none" }} onChange={handleFileInputChange} />
                  </form>
            </div>
      )
}

export default File