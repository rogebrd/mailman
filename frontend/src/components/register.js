import React from "react";

export const Register = () => {
    const [email, setEmail] = React.useState("");

    const registerEmail = () => {
        //make call to lambda to register new email
    }

    return (
        <div>
            <h2>Register new email</h2>
            <input type="text" value={email} onChange={(change) => setEmail(change.target.value)}></input>
            <button onClick={registerEmail}>Register</button>
        </div>
    );
}