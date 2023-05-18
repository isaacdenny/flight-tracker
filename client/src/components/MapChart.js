import React from "react";
import {
  ComposableMap,
  Geographies,
  Geography,
  Marker
} from "react-simple-maps";

const geoUrl =
  "https://raw.githubusercontent.com/deldersveld/topojson/master/continents/north-america.json";

const MapChart = (params) => {
  return (
    <ComposableMap projection="geoAlbers">
      <Geographies geography={geoUrl}>
        {({ geographies }) =>
          geographies.map((geo) => (
            <Geography
              key={geo.rsmKey}
              geography={geo}
              fill="#DDD"
              stroke="#FFF"
            />
          ))
        }
      </Geographies>
      <Marker coordinates={[params.data['lon'], params.data['lat']]}>
        <circle r={8} fill="#F53" />
      </Marker>
    </ComposableMap>
  );
};

export default MapChart;