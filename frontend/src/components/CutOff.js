import React, { useState } from 'react';

const CutOff = ({ cutOffNum, updateCutOffNum }) => {

    return (
        <div>
            <div className="cut-off">
                <label htmlFor="cut-off">Select Cutoff (Minutes):</label>
                <span className="cutoff-input">
                    <input type="number" min={1} max={60} step={1} value={cutOffNum} onChange={e => updateCutOffNum(e.target.value)} />
                </span>
            </div>
        </div>
    );
}

export default CutOff;