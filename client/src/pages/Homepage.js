import React, { useEffect, useState } from "react";
import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";

const Homepage = () => {
  const [options, setOptions] = useState({
    chart: {
      width: 800,
    },
    xAxis: {
      labels: {
        format: '{value:.1f}',
      },
      tickamount: "8",
    },
    title: {
      text: `Altitude for flight: id here`,
    },
    series: [{ type: "area", name: "altitude", data: [] }],
  });

  const fetchFlightInfo = async () => {
    try {
      const inflight_req = await fetch(`http://localhost:8000/inflight/`);
      const inflight_res = await inflight_req.json();
      const position_req = await fetch(`http://localhost:8000/position/`);
      const position_res = await position_req.json();

      if (inflight_res["in_flight"]) {
        let updatedSeries = options.series;
        updatedSeries[0].data.push([
          inflight_res["total_time"],
          position_res["alt"],
        ]);
        if (updatedSeries[0].data.length > 25) {
          updatedSeries[0].data = updatedSeries[0].data.slice(1);
        }
        setOptions({
          xAxis: {
            labels: {
              format: '{value:.1f}',
            },
            tickamount: "8",
          },
          title: {
            text: `Altitude for flight: id here`,
          },
          series: updatedSeries,
        });
      }
    } catch (e) {
      console.log(e);
    } finally {
      setTimeout(fetchFlightInfo, 3000);
    }
  };

  useEffect(() => {
    fetchFlightInfo();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <HighchartsReact highcharts={Highcharts} options={options} />
      </header>
    </div>
  );
};

export default Homepage;
