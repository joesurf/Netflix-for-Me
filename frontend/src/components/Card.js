import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Card.css';

const base_url = "https://image.tmdb.org/t/p/original/";


function Card({ movie, isLargeRow }) {
    const navigate = useNavigate();


    function watchVideo() {
        const id = 1;
        navigate(`/videos/${id}`);
    }

    return (
        <img 
            key={movie.id} 
            className={`row__poster ${isLargeRow && "row__posterLarge"}`}
            src={`${base_url}${isLargeRow ? movie.poster_path : movie.backdrop_path}`} 
            alt={movie.name} 

            onClick={watchVideo}
        />
    )
}

export default Card