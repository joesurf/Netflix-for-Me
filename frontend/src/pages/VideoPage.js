import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import ReactVideoPlayer from '../components/ReactVideoPlayer';

import axios from 'axios';

const base_url = "https://www.sgunchained.com/";

function VideoPage({ }) {
    const { id } = useParams();
    let [movie, setMovie] = useState({});

    useEffect(() => {
        getMovie(id);
    }, [])

    async function getMovie(id) {
        // Only for testing purposes
        id = "The Demi-Gods and Semi-Devils E1.mp4";

        try {
            const response = await axios.get(`http://localhost:8000/videos/${id}`);
            setMovie(response.data);
            // console.log(response.data['s3_video_source']);
        } catch (error) { 
            console.log(error);
        }
    }

    console.log("MOVIE");
    console.log(movie);
    if (Object.keys(movie).length === 0) {
        return <h1>Still loading...</h1>
    }

    return (
        <div>
            <ReactVideoPlayer 
                key={movie.id} 
                src={movie.s3_video_source}
                alt={movie.title} 
            />
        </div>
    )
}

export default VideoPage;