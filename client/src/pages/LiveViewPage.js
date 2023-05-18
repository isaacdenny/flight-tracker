import React, { useEffect, useState } from "react";
import AltitudeChart from "../components/AltitudeChart";
import MapChart from "../components/MapChart";

const LiveViewPage = () => {
  const [isActive, setIsActive] = useState(false);
  const [altData, setAltData] = useState([]);
  const [posData, setPosData] = useState({});
  const [deviceCode, setDeviceCode] = useState("AE45980");

  const handleStartFlight = async () => {
    const res = (
      await fetch(`http://localhost:8000/live/${deviceCode}`, {
        method: "POST"
      })
    ).json();
    setIsActive(true);
  };

  const fetchFlightInfo = async () => {
    try {
      const flight_req = await fetch(
        `http://localhost:8000/live/${deviceCode}`
      );
      const flight_res = await flight_req.json();

      if (flight_res.is_active) {
        const total_time = (
          Math.round(flight_res.total_time * 100) / 100
        ).toFixed(2);
        const newAltData = {
          time: total_time,
          altitude: flight_res.position.alt,
        };
        const newPosData = {
          time: total_time,
          lat: flight_res.position.lat,
          lon: flight_res.position.lon,
        };
        let tempData = [...altData];
        tempData.push(newAltData);
        if (tempData.length > 20) {
          tempData.shift();
        }
        setAltData(tempData);
        setPosData(newPosData);
      }
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    if (!isActive) {
      return
    }
    const intervalId = setInterval(() => {
      fetchFlightInfo();
    }, 5000);
    return () => clearInterval(intervalId);
  }, [fetchFlightInfo]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>LiveViewPage</h1>
        <p>View Flight Stats Live</p>
        {isActive ? (
          <>
            <AltitudeChart data={altData} />
            <MapChart data={posData} />
          </>
        ) : (
          <>
            <input
              value={deviceCode}
              onChange={(e) => setDeviceCode(e.target.value)}
            />
            <button onClick={handleStartFlight}>Start Flight</button>
          </>
        )}
      </header>
    </div>
  );
};

export default LiveViewPage;
