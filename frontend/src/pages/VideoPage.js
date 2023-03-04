import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import ReactVideoPlayer from '../components/ReactVideoPlayer';

import axios from 'axios';

function VideoPage() {
    const { id } = useParams();
    let [movie, setMovie] = useState({});

    useEffect(() => {
        getMovie(id);
    }, [id])

    async function getMovie(id) {
        // Only for testing purposes

        try {
            const response = await axios.get(`http://54.90.184.160/videos/${id}`);
            setMovie(response.data);
        } catch (error) { 
            console.log(error);
        }
    }

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