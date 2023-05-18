import React, { useEffect, useState } from "react";
import AltitudeChart from "../components/AltitudeChart";
import MapChart from "../components/MapChart";

const LiveViewPage = () => {
  const [altData, setAltData] = useState([]);
  const [posData, setPosData] = useState({});

  const fetchFlightInfo = async () => {
    try {
      const inflight_req = await fetch(`http://localhost:8000/inflight/`);
      const inflight_res = await inflight_req.json();
      const position_req = await fetch(`http://localhost:8000/position/`);
      const position_res = await position_req.json();

      if (inflight_res["in_flight"]) {
        const total_time = (
          Math.round(inflight_res["total_time"] * 100) / 100
        ).toFixed(2);
        const newAltData = {
          time: total_time,
          altitude: position_res["alt"],
        };
        const newPosData = {
          time: total_time,
          lat: position_res["lat"],
          lon: position_res["lon"]
        };
        let tempData = [...altData];
        tempData.push(newAltData);
        if (tempData.length > 20) {
          tempData.shift();
        }
        setAltData(tempData);
        setPosData(newPosData)
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
        <h1>LiveViewPage</h1>
        <AltitudeChart data={altData} />
        <MapChart data={posData} />
      </header>
    </div>
  );
};

export default LiveViewPage;
