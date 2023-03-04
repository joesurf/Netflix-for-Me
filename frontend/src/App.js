import React, { Fragment } from 'react';

import {
  Route,
  Routes,
  BrowserRouter,
} from "react-router-dom";

import HomePage from './pages/HomePage';
import VideoPage from './pages/VideoPage';

function App() {
  return (
    <Fragment>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/videos/:id" element={<VideoPage />} />

        </Routes>
      </BrowserRouter>
    </Fragment>
  )
}

export default App