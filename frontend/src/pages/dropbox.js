import React from "react";
import { SidebarLeft } from "../components/sidebarLeft";
import { SidebarRight } from "../components/sidebarRight";

export const Dropbox = () => {
    return (
        <div className="home">
            <SidebarLeft />
            <div className="content-single content">
                    <h1 className="single-title title">Authenticate with Dropbox</h1>
                    <button className="dropbox-button">Sign in</button>
            </div>
            <SidebarRight />
        </div>
    );
}