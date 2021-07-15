import React from "react";

export const SidebarRightConfirmation = () => {
    return (
        <div className="sidebar-right">
            <img className="sidebar-right-image-confirmation" src={process.env.PUBLIC_URL + '/email-folder.png'} alt="Dropbox Folder"></img>
            <p className="sidebar-right-confirmation-text">Psst... your emails will be stored in the new <a className="email-folder-link">Emails folder</a> in Files</p>
        </div>
    );
}