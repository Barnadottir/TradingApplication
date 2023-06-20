import React, { useState, useEffect } from 'react';
import "./styles.css"
import TradingData from "./TradingData";


//OBS make TraindData component as route instead!!

const App = () => {
  const [posts, setPosts] = useState([]);
  const [showTradingData, setShowTradingData] = useState(false); 
  
  useEffect(() => {
    fetch('/api/posts/')
      .then(res => res.json())
      .then(data => setPosts(data));
      console.log("we are trying to fetch data!");
  }, []);

  const handleButtonClick = () => {
    setShowTradingData(!showTradingData);
  }

  return (
    <div className="App">
      <button onClick={handleButtonClick}>
        {showTradingData ? 'Hide Trading Data' : 'Show Trading Data'}
      </button>
      <header className="header">
        <h1 className="title">Welcome to Oskar and Philip's Trading Website!</h1>
      </header>
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
