import React from "react";
import { Home } from "./pages/home";
import { Email } from "./pages/email";
import { Dropbox } from "./pages/dropbox";
import { Confirmation } from "./pages/confirmation";
import { DropboxAuth } from "dropbox";

export const Mailman = () => {
    // States are HOME, EMAIL, DROPBOX, CONFIRMATION, ERROR
    const [registerStep, setRegisterStep] = React.useState("HOME");
    const [email, setEmail] = React.useState("");
    const [dropboxAuth, setDropboxAuth] = React.useState(null);
    const [authPopup, setAuthPopup] = React.useState(null);

    const onSubmitEmail = () => {
        if(email !== ""){
            setRegisterStep("DROPBOX");
        }
    }

    const onSubmitAuthenticate = () => {
        const auth = new DropboxAuth({
            clientId: 'a04f1ghft6a45rn'
        });
        setDropboxAuth(auth);
        auth.getAuthenticationUrl('https://rogebrd.github.io/mailman/', '', 'code', 'legacy', null, 'none', true).then((authUrl) => {
            const windowOptions = {
                toolbar: 'no',
                menubar: 'no',
                width: 600,
                height: 800,
                top: 100,
                left: 100,
            };
            const popup = window.open(authUrl, "Mailman Authentication", windowOptions);
            setAuthPopup(popup);
        }).catch((error) => {
            console.error(error);
        });
    }

    React.useEffect(() => {
        if (authPopup) {
            return;
        }

        const currentUrl = window.location.href;
          if (!currentUrl) {
            return;
          }
          const searchParams = new URL(currentUrl).searchParams;
          const code = searchParams.get('code');
          if (code) {
            window.opener.postMessage({
                'code': code,
                'sender': 'Dropbox Authentication Popup'
            });
            window.close();
          }

    }, [authPopup]);

    const onMessageReceivedFromPopup = React.useCallback((event) => {
        if(!dropboxAuth){
            return;
        }
        const contents = event.data;
        if(contents.sender && contents.sender === 'Dropbox Authentication Popup'){
            dropboxAuth.getAccessTokenFromCode('https://rogebrd.github.io/mailman/', contents.code).then((response) => {
                const { result } = response;
                const fetchOptions = {
                    method: 'POST'
                }
                const baseApiUrl = "https://duv3a4ynni.execute-api.us-west-2.amazonaws.com";
                const registrationUrl = `${baseApiUrl}/prod/api?email=${email}&dropbox_oauth_token=${result.access_token}`;
                fetch(registrationUrl, fetchOptions)
                    .then((res) => {
                        setRegisterStep("CONFIRMATION");
                    })
                    .catch((error) => {
                        console.error(error);
                    })
                
            })
            .catch((error) => {
            console.error(error);
            })
        }
    }, [dropboxAuth, email]
    );

    React.useEffect(() => {
        window.addEventListener("message", onMessageReceivedFromPopup);
        return () =>
          window.removeEventListener("message", onMessageReceivedFromPopup);
      }, [onMessageReceivedFromPopup]);

    const getPage = () => {
        switch(registerStep) {
            case "HOME":
                return (<Home email={email} setEmail={setEmail} onSubmit={onSubmitEmail} navigate={setRegisterStep}/>)
            case "EMAIL":
                return (<Email email={email} setEmail={setEmail} onSubmit={onSubmitEmail}/>)
            case "DROPBOX":
                return (<Dropbox onSubmit={onSubmitAuthenticate} />)
            case "CONFIRMATION":
                return (<Confirmation />)
            case "ERROR":
            default:
                return (<Home />)
        }
    }

    return (
        <>
        {
            (getPage())
        }
        </>
    );
}