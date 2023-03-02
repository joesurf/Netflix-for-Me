import React from 'react';
import './App.css';

import Row from './components/Row';
import Banner from './components/Banner';
import requests from './requests';
import Nav from './components/Nav';

// import ReactVideoPlayer from './components/ReactVideoPlayer';

import PersonalRow from './components/PersonalRow'


function App() {
  return (
    <div className="app">
      <Nav></Nav>
      
      <Banner></Banner>

      <Row title="NETFLIX ORIGINALS" fetchUrl={requests.fetchNetflixOriginals} isLargeRow />
      
      <Row title="Trending Now" fetchUrl={requests.fetchTrending} />
      <Row title="Top Rated" fetchUrl={requests.fetchTopRated} />
      <Row title="Action Movies" fetchUrl={requests.fetchActionMovies} />
      <Row title="Comedy Movies" fetchUrl={requests.fetchComedyMovies} />
      <Row title="Horror Movies" fetchUrl={requests.fetchHorrorMovies} />
      <Row title="Romance Movies" fetchUrl={requests.fetchRomanceMovies} />
      <Row title="Documentaries" fetchUrl={requests.fetchDocumantaries} />
      {/* <Row title="Personal" fetchUrl={} /> */}
      <PersonalRow></PersonalRow>

      {/* <ReactVideoPlayer></ReactVideoPlayer> */}
    </div>
  );
}

export default App;
