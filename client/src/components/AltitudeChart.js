import React from "react";
import {
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Area,
  AreaChart,
} from "recharts";

const DataChart = (params) => {
  return (
    <AreaChart
      width={730}
      height={250}
      data={params.data}
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
  );
};

export default DataChart;
