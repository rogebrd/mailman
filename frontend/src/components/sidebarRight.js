import React from "react";

export const SidebarRight = () => {
    return (
        <div className="sidebar-right">
            <img className="sidebar-right-image" src={process.env.PUBLIC_URL + '/sidebar-right.png'} alt="Dropbox Working"></img>
        </div>
    );
}