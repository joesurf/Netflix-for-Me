import React, { useEffect, useState } from 'react'
// import axios from '../axios';
import './Row.css'

import ReactVideoPlayer from './ReactVideoPlayer';

const base_url = "https://www.sgunchained.com/";

function PersonalRow({ title, fetchUrl, isLargeRow }) {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        function fetchData() {
            const movies = [
                {
                    "s3_video_source": "gamingTestVideo.mp4",
                    "title": "Gaming"
                },
                {
                    "s3_video_source": "dirtyTestVideo.mp4",
                    "title": "Test"
                }
            ]
            setMovies(movies);
        }
        fetchData();
    }, [fetchUrl]);

    return (
        <div className="row">
            <h2>{"Personal"}</h2>

            <div className="row__posters">
                
                {movies.map(movie => (
                    <div className={`row__posterLarge ${isLargeRow && "row__posterLarge"}`}
                    >
                        <ReactVideoPlayer 
                            key={movie.id} 
                            src={`${base_url}${movie.s3_video_source}`} 
                            alt={movie.title} 
                        />
                    </div>
   
                ))}
            </div>
        </div>
    )
}

export default PersonalRow