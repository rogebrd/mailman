import React from "react";
import { SidebarLeft } from "../components/sidebarLeft";
import { SidebarRightConfirmation } from "../components/sidebarRight-confirmation";

export const Confirmation = () => {
    const copyToClipboard = (str) => {
        const el = document.createElement('textarea');
        el.value = str;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
      };

    return (
        <div className="home">
            <SidebarLeft />
            <div className="content-single content">
                <svg width="94" height="94" viewBox="0 0 94 94" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M81.947 12.053C73.95 4.055 62.192 0 47 0C31.808 0 20.05 4.055 12.053 12.053C4.056 20.051 0 31.809 0 47C0 62.191 4.055 73.949 12.053 81.947C20.051 89.945 31.808 94 47 94C62.192 94 73.95 89.945 81.947 81.947C89.944 73.949 94 62.191 94 47C94 31.809 89.945 20.051 81.947 12.053ZM47 88C19.794 88 6 74.206 6 47C6 19.794 19.794 6 47 6C74.206 6 88 19.794 88 47C88 74.206 74.206 88 47 88Z" fill="#F7F5F2"/>
                    <path d="M40.8782 67.1213L72.8782 35.1213L68.6355 30.8787L40.8784 58.6358L25.1213 42.8787L20.8787 47.1213L40.8782 67.1213Z" fill="#F7F5F2"/>
                </svg>
                <h1 className="no-padding single-title title">Begin forwarding your email to Dropbox</h1>
                <p className="single-title page-subtitle">Forward any email to save it and any attachments</p>
                <div className="email-input-wrapper">
                    <svg className="email-input-logo" width="18" height="14" viewBox="0 0 18 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M0 0.25V11.5C0.000694729 12.0965 0.237971 12.6684 0.659777 13.0902C1.08158 13.512 1.65348 13.7493 2.25 13.75H15.75C16.3465 13.7493 16.9184 13.512 17.3402 13.0902C17.762 12.6684 17.9993 12.0965 18 11.5V0.25H0ZM15.4395 1.75L9 8.18913L2.5605 1.75H15.4395ZM15.75 12.25H2.25C2.05109 12.25 1.86032 12.171 1.71967 12.0303C1.57902 11.8897 1.5 11.6989 1.5 11.5V2.8105L9 10.3105L16.5 2.8105V11.5C16.5 11.6989 16.421 11.8897 16.2803 12.0303C16.1397 12.171 15.9489 12.25 15.75 12.25Z" fill="#524A3E" fill-opacity="0.78"/>
                    </svg>
                    <p className="copy email-input">dropbox.mailman@gmail.com</p>
                    <button className="copy email-input-button" onClick={() => copyToClipboard("dropbox.mailman@gmail.com")}>Copy</button>
        </div>
            </div>
            <SidebarRightConfirmation />
        </div>
    );
}