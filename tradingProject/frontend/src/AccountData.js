import { useState, useEffect } from "react";
import "./styles.css";

const AccountData = (props) => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchAccountData = () => {
            fetch("/api/accountData/")
                .then(response => response.json())
                .then(data => setData(data));
        };
        
        fetchAccountData();  // Fetch once immediately when the component mounts

        //const intervalId = setInterval(fetchAccountData, 5000);  // Then start to fetch every 5 seconds
        
        //return () => clearInterval(intervalId);  // Clear the interval when the component unmounts
    }, []);

    //if(data) console.log("NEW DATA!!", data);

    const renderData = () => {
        if (!data) return null;
        return (
            <div>
                <h2>Account id: {data.id}</h2>
                <p>Equity: {data.equity}</p>
                <p>Currency: {data.currency}</p>
                {/* Add more fields as necessary */}
            </div>
        );
    }

    return (
        <div className="account-data">
            <h1 className="account-data-header">
                Account Data Page
            </h1>
            {renderData()}
        </div>
    );
}

export default AccountData;
