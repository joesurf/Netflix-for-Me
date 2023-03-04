import React from 'react';
import { DefaultPlayer } from 'react-html5video';
import 'react-html5video/dist/styles.css';



const ReactVideoPlayer = ({ src, alt}) => {
    console.log(src);

    return (
        <DefaultPlayer autoPlay loop>
            <source src={ src } type="video/webm" />
        </DefaultPlayer>
    );
};

export default ReactVideoPlayer;