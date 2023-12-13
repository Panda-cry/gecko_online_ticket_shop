// src/store/actions.js
import { createSlice, configureStore } from "@reduxjs/toolkit";

const initialState = {
  chart: [],
};
const chartSlice = createSlice({
  name: "chart",
  initialState,
  reducers: {
    add(state, action) {
      state.chart.push(action.payload);
    },
    remove(state) {
      state.chart.pop();
    },
  },
});

// src/store/index.js

const store = configureStore({
  reducer: {
    chart: chartSlice.reducer,
  },
});

export const chartActions = chartSlice.actions;
export default store;
