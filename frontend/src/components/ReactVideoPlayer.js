import React from 'react';
import { DefaultPlayer } from 'react-html5video';
import 'react-html5video/dist/styles.css';



const ReactVideoPlayer = () => {
    return (
        <DefaultPlayer autoPlay loop>


            <source src={ "https://www.sgunchained.com/gamingTestVideo.mp4" } type="video/webm" />
        </DefaultPlayer>
    );
};

export default ReactVideoPlayer;