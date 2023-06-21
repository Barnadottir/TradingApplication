import { useState, useEffect } from "react";
import "./styles.css"

const TradingData = (props) => {
    const [tradingData, setTradingData] = useState(null);

    useEffect(() => {
        fetch('/api/stockdata/')
            .then(res => res.json())
            .then(data => {
                //console.log(data);  // should log {company: 'Apple Inc.', ticker: 'AAPL', price: '150.00 USD'}
                setTradingData(data);
            });
    }, []);

    const renderValue = (value) => {
        if (typeof value === 'object') {
            return (
                <ul className="nested-list">
                    {Object.entries(value).map(([key, nestedValue]) => (
                        <li key={key}>
                            <span className="nested-key">{key}:</span> {nestedValue.toString()}
                        </li>
                    ))}
                </ul>
            );
        }
        return value.toString();
    };

    const printAllData = () => {
        if (tradingData) {
            return Object.entries(tradingData).map(([key, value]) => (
                <li key={key}>
                    <span className="data-key">{key}:</span> {renderValue(value)}
                </li>
            ));
        }
        return null;
    };

    return (
        <div className="App">
            <h1 className="header">Trading Data</h1>
            <ul className="trading-list">{printAllData()}</ul>
        </div>
    );
};

export default TradingData;
