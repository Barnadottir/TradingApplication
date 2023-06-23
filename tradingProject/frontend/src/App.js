import React, { useState } from 'react';
import "./styles.css";
import TradingSection from './TradingSection';
import TradingData from "./TradingData";
import Header from "./Header";
import AccountData from "./AccountData";
import Footer from "./Footer";
import MakeTrade from "./MakeTrade";

const App = () => {
  const [route, setRoute] = useState('home');

  const renderComponent = () => {
    switch (route) {
      case 'home':
        return <Home />;
      case 'trading':
        return <TradingSection />;
      case 'data':
        return <TradingData />;
      case 'trader':
        return <MakeTrade />;
      default:
        return null;
    }
  };

  const navigate = (route) => {
    setRoute(route);
  };

  return (
    <div className="App">
      <Header navigate={navigate} />
      <div className="content">
        <div className="left-panel">
          <AccountData />
        </div>
        <div className="right-panel">
          {renderComponent()}
        </div>
      </div>
      <Footer /> 
    </div>
  );
};

const Home = () => {
  return (
    <div>
      <h2>Welcome to the Homepage</h2>
      {/* Add your homepage content here */}
    </div>
  );
};

export default App;