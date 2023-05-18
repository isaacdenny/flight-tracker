import React from "react";
import { Map, Marker } from "pigeon-maps";
import { stamenToner } from "pigeon-maps/providers";

const MapChart = (params) => {
  return (
    <Map
      provider={stamenToner}
      dprs={[1, 2]}
      width={730}
      height={250}
      defaultCenter={[params.data["lat"], params.data["lon"]]}
      defaultZoom={12}
    >
      <Marker width={50} anchor={[params.data["lat"], params.data["lon"]]} />
    </Map>
  );
};

export default MapChart;
