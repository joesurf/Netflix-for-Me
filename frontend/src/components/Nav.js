import React, { useEffect, useState } from 'react';
import "./Nav.css";
import netflix_logo from '../assets/Netflix_logo.svg';
import netflix_default_profile from '../assets/netflix_default_profile.jpg'


function Nav() {
    const [show, handleShow] = useState(false);

    useEffect(() => {
        window.addEventListener("scroll", () => {
            if (window.scrollY > 100) {
                handleShow(true);
            } else {
                handleShow(false);
            }
        });
        return () => {
            window.removeEventListener("scroll", () => {});
        };
    }, []);

    return (
        <div className={`nav ${show && "nav__black"}`}>
            <img 
                className='nav__logo'
                src={netflix_logo}
                alt="Netflix Logo"
            />

            <img 
                className='nav__avatar'
                src={netflix_default_profile}
                alt="Avator Profile"
            />
        </div>
    )
}

export default Nav