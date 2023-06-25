import { useState } from 'react';
import { getCookie} from "./utilities/utils"
const MakeTrade = () => {
    const [symbol, setSymbol] = useState('');
    const [shares, setShares] = useState(1);
    const [side, setSide] = useState('buy');

    const makeTrade = (event) => {
        event.preventDefault();  // Prevent the form from refreshing the page
        const csrftoken = getCookie('csrftoken'); // Get CSRF token
    
        fetch('/api/makeTrade/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken, // Include CSRF token in headers
            },
            body: JSON.stringify({ symbol, shares, side }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    };

    return (
        <form onSubmit={makeTrade}>
            <input type="text" value={symbol} onChange={e => setSymbol(e.target.value)} placeholder="Symbol" />
            <input type="number" value={shares} onChange={e => setShares(e.target.value)} placeholder="Shares" min="1" />
            <select value={side} onChange={e => setSide(e.target.value)}>
                <option value="buy">Buy</option>
                <option value="sell">Sell</option>
            </select>
            <button type="submit">Submit Trade</button>
            <button onClick= {evt => console.log("submit Data!")}>Submit med!!</button>
        </form>
    );
};

export default MakeTrade;
