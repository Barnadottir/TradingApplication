import React, { useState } from 'react';
import MyLineChart from './MyLineChart';

const TradingSection = () => {
  const [showTradingData, setShowTradingData] = useState(false);
  const [selectedOption, setSelectedOption] = useState('');

  const handleButtonClick = () => {
    setShowTradingData(!showTradingData);
  };

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <MyLineChart />
      <button onClick={handleButtonClick}>
        {showTradingData ? 'Hide Trading Data' : 'Show Trading Data'}
      </button>
      <form>
        <label htmlFor="select-option">Select an option:</label>
        <select
          id="select-option"
          name="select-option"
          value={selectedOption}
          onChange={handleOptionChange}
        >
          <option value="option1">Option 1</option>
          <option value="option2">Option 2</option>
          <option value="option3">Option 3</option>
        </select>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default TradingSection;