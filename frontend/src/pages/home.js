import React from "react";
import { SidebarLeft } from "../components/sidebarLeft";
import { SidebarRight } from "../components/sidebarRight";
import { Register } from "../components/register";

export const Home = () => {
    return (
        <div className="home">
            <SidebarLeft />
            <div className="content">
                <div className="content-top">
                    <h1 className="page-title">Save email and attachments to Dropbox</h1>
                    <p className="page-subtitle">Forward and save. It's that simple. <a className="try-link">Try it now</a></p>
                </div>
                <div className="content-bottom">
                    <Register />
                </div>
            </div>
            <SidebarRight />
        </div>
    );
}