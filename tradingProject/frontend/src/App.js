import React, { useState, useEffect } from 'react';
import "./styles.css";
import TradingData from "./TradingData";
import AccountData from './AccountData';
import MyLineChart from './MyLineChart';
const App = () => {
    const [posts, setPosts] = useState([]);
    const [showTradingData, setShowTradingData] = useState(false);
    const dates = ['2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04'];
    const prices = [35.78, 36.01, 35.98, 36.23];
    useEffect(() => {
        fetch('/api/posts/')
            .then(res => res.json())
            .then(data => setPosts(data));
        //console.log("we are trying to fetch data!");
    }, []);

    const handleButtonClick = () => {
        setShowTradingData(!showTradingData);
    }

    const submitData = (evt) => {
        evt.preventDefault();
        //console.log("data we want:", evt.target.value);
    }
    return (
        <div className="App">
          <MyLineChart dates={dates} prices={prices} />
            <AccountData />
            <button onClick={handleButtonClick}>
                {showTradingData ? 'Hide Trading Data' : 'Show Trading Data'}
            </button>
            <header className="header">
                <h1 className="title">Welcome to Oskar and Philip's Trading Website!</h1>
            </header>
            <form onSubmit={(evt) => submitData(evt)}>
                <label htmlFor="select-option">Select an option:</label>
                <select id="select-option" name="select-option">
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                    <option value="option3">Option 3</option>
                </select>
                <input type="submit" value="Submit" />
            </form>
            <div className="content">
                {posts.map(post => (
                    <div className="post" key={post.id}>
                        <h2 className="post-title">{post.title}</h2>
                        <p className="post-content">{post.content}</p>
                    </div>
                ))}
            </div>
            {showTradingData && <TradingData />}
        </div>
    );
}

export default App;
