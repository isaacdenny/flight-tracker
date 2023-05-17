import React, { useEffect, useState } from "react";
import {
  AreaChart,
  YAxis,
  XAxis,
  Tooltip,
  Area,
} from "recharts";

const Homepage = () => {
  const [data, setData] = useState([]);

  const fetchFlightInfo = async () => {
    const time_req = await fetch((`http://localhost:8000/inflight/`))
    const time_res = await time_req.json()
    const position_req = await fetch((`http://localhost:8000/position/`))
    const position_res = await position_req.json()
    setData([...data, { 'time': time_res['total_time'], 'altitude': position_res['alt'] }]);
  }

  useEffect(() => {
    fetchFlightInfo();
  }, []);

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
            <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8} />
              <stop offset="95%" stopColor="#8884d8" stopOpacity={0} />
            </linearGradient>
          </defs>
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Area
            type="monotone"
            dataKey="altitude"
            stroke="#8884d8"
            fillOpacity={1}
            fill="url(#colorUv)"
          />
        </AreaChart>
        <button onClick={fetchFlightInfo}>Add to chart</button>
      </header>
    </div>
  );
};

export default Homepage;
