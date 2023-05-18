import React, { useEffect, useState } from "react";
import { XAxis, YAxis, CartesianGrid, Tooltip, Area, AreaChart } from "recharts";

const Homepage = () => {
  const [data, setData] = useState([]);

  const fetchFlightInfo = async () => {
    try {
      const inflight_req = await fetch(`http://localhost:8000/inflight/`);
      const inflight_res = await inflight_req.json();
      const position_req = await fetch(`http://localhost:8000/position/`);
      const position_res = await position_req.json();

      if (inflight_res["in_flight"]) {
        const newData = {
          time: (Math.round(inflight_res["total_time"] * 100) / 100).toFixed(2),
          altitude: position_res["alt"],
        };
        let tempData = [...data];
        tempData.push(newData);
        if (tempData.length > 20) {
          tempData.shift();
        }
        setData(tempData);
      }
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    const intervalId = setInterval(() => {
      fetchFlightInfo();
    }, 5000);
    return () => clearInterval(intervalId);
  }, [fetchFlightInfo]);

  return (
    <div className="App">
      <header className="App-header">
        <AreaChart
          width={730}
          height={250}
          data={data}
          margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
        >
          <defs>
            <linearGradient id="colorAlt" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8} />
              <stop offset="95%" stopColor="#8884d8" stopOpacity={0} />
            </linearGradient>
          </defs>
          <XAxis dataKey="time" />
          <YAxis />
          <CartesianGrid strokeDasharray="3 3" />
          <Tooltip />
          <Area
            type="monotone"
            dataKey="altitude"
            stroke="#8884d8"
            fillOpacity={1}
            fill="url(#colorAlt)"
          />
        </AreaChart>
      </header>
    </div>
  );
};

export default Homepage;
