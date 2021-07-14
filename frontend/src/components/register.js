import React from "react";

export const Register = () => {
    const [email, setEmail] = React.useState("");

    const registerEmail = () => {
        //make call to lambda to register new email
    }

    return (
        <div className="email-input-wrapper">
            <svg className="email-input-logo" width="18" height="14" viewBox="0 0 18 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M0 0.25V11.5C0.000694729 12.0965 0.237971 12.6684 0.659777 13.0902C1.08158 13.512 1.65348 13.7493 2.25 13.75H15.75C16.3465 13.7493 16.9184 13.512 17.3402 13.0902C17.762 12.6684 17.9993 12.0965 18 11.5V0.25H0ZM15.4395 1.75L9 8.18913L2.5605 1.75H15.4395ZM15.75 12.25H2.25C2.05109 12.25 1.86032 12.171 1.71967 12.0303C1.57902 11.8897 1.5 11.6989 1.5 11.5V2.8105L9 10.3105L16.5 2.8105V11.5C16.5 11.6989 16.421 11.8897 16.2803 12.0303C16.1397 12.171 15.9489 12.25 15.75 12.25Z" fill="#524A3E" fill-opacity="0.78"/>
            </svg>

            <input className="email-input" type="text" placeholder="Email Address"></input>
            <button className="email-input-button">Sign up</button>
        </div>
        
    );
}