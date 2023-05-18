import React from "react";
import { Map, Marker } from 'pigeon-maps'
import { stamenToner } from 'pigeon-maps/providers'

const MapChart = (params) => {
  let position = [params.data['lat'], params.data['lon']]
  return (
    <Map provider={stamenToner} dprs={[1, 2]} height={300} defaultCenter={position} defaultZoom={12}>
      <Marker width={50} anchor={position} />
    </Map>
  );
};

export default MapChart;