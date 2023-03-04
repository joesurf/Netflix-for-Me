import React, { useEffect, useState } from 'react'
import axios from '../axios';
import './Row.css'
import Card from './Card';



function Row({ title, fetchUrl, isLargeRow }) {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const request = await axios.get(fetchUrl);
            setMovies(request.data.results);
            return request;
        }
        fetchData();
    }, [fetchUrl]);

    return (
        <div className="row">
            <h2>{title}</h2>

            <div className="row__posters">
                {movies.map(movie => (
                    <Card key={movie.id} movie={movie} isLargeRow={isLargeRow} />
                ))}
            </div>
        </div>
    )
}

export default Row