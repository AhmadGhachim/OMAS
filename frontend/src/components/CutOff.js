import React, { useState } from 'react';
import InputNumber from 'react-input-number';

const CutOff = () => {

    const [num, setNum] = useState(1);
    return (
        <div>
            <div className="cut-off">
                <label htmlFor="cut-off">Select Cutoff (Minutes):</label>
                <span className="cutoff-input">
                <input type="number" min={0} max={60} step={1} value={num} onChange={e => setNum(e.target.value)} />
            </span>
            </div>
        </div>
    );
}

export default CutOff;