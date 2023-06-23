import React from 'react';

const Header = ({ navigate }) => {
  return (
    <header className="header">
      <div className="container">
        <h1 className="title">Welcome to Oskar and Philip's Trading Website!</h1>
        <nav>
          <ul className="navigation">
            <li>
              <button onClick={() => navigate('home')}>Home</button>
            </li>
            <li>
              <button onClick={() => navigate('trading')}>Trading</button>
            </li>
            <li>
              <button onClick={() => navigate('data')}>Data</button>
            </li>
            <li>
              <button onClick={() => navigate('trader')}>Make a Trade</button>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;