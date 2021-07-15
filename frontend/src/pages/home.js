import React from "react";
import { SidebarLeft } from "../components/sidebarLeft";
import { SidebarRight } from "../components/sidebarRight";
import { Register } from "../components/register";

export const Home = ({email, setEmail, onSubmit, navigate}) => {
    return (
        <div className="home">
            <SidebarLeft />
            <div className="content">
                <div className="content-top">
                    <h1 className="title">Save email and attachments to Dropbox</h1>
                    <p className="page-subtitle">Forward and save. It's that simple. <button onClick={() => navigate("EMAIL")} className="try-link">Try it now</button></p>
                </div>
                <div className="content-bottom">
                    <Register email={email} setEmail={setEmail} onSubmit={onSubmit}/>
                </div>
            </div>
            <SidebarRight />
        </div>
    );
}