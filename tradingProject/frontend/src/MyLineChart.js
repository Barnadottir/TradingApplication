import { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";
import {
    Chart as ChartJS,
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement
} from "chart.js";

ChartJS.register(
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement
);

const MyLineChart = (props) => {
    const [chartData, setChartData] = useState(null);

    useEffect(() => {
        fetch('/api/BTCData/')
            .then(response => response.json())
            .then(data => {
                // Get an array of timestamps (keys) and prices (values)
                console.log("data:",data.Open);
                let timestamps = Object.keys(data.Open);
                let prices = Object.values(data.Open);
                
                // Convert timestamps to dates and prices to numbers
                let labels = timestamps.map(t => new Date(Number(t)).toLocaleDateString());
                let dataset = prices.map(Number);

                setChartData({
                    labels: labels,
                    datasets: [{
                        label: 'BTC Historic Data',
                        data: dataset,
                        borderColor: 'red',
                        fill : true,
                        tension: 0.4
                    }]
                });
            });
    }, []);

    const options = {
        plugins: {
            legend: true
        },
        scales : {
            y: {}
        }
    }

    return (
        <div>
            <h1>BTC Historic data:</h1>
            <button onClick = {(evt) => console.log("making trade!")}>
                Press me to make trade!
            </button>
            <button onClick = {(evt) => console.log("Sell positions!")}>
                Press me to sell!
            </button>
            {chartData && 
                <Line
                    data = {chartData}
                    options = {options}
                />
            }
        </div>
    );
};

export default MyLineChart;
