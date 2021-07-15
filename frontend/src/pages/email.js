import React from "react";
import { SidebarLeft } from "../components/sidebarLeft";
import { SidebarRight } from "../components/sidebarRight";
import { Register } from "../components/register";

export const Email = ({email, setEmail, onSubmit}) => {
    return (
        <div className="home">
            <SidebarLeft />
            <div className="content-single content">
                    <h1 className="single-title title">Register an email address</h1>
                    <Register email={email} setEmail={setEmail} onSubmit={onSubmit}/>
            </div>
            <SidebarRight />
        </div>
    );
}