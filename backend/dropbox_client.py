from dropbox import Dropbox, files

class MailmanDropboxClient():
    def __init__(self):
        self.dbx = Dropbox(
            oauth2_access_token="temp_token"
        )

    def upload_file_to_dropbox(self, email_contents, path, desired_file_name, access_token):
        content_in_bytes = self.convert_email_content_to_bytes(email_contents)
        path = "%s/%s" % (path, desired_file_name)

        self.reset_tokens(access_token)
        self.dbx.files_upload(
            content_in_bytes, 
            path, 
            mode=files.WriteMode.overwrite,  # when saving over a previous email/thread, overrides the file
            strict_conflict=False
        )
        

    def convert_email_content_to_bytes(self, email_contents):
        return email_contents.encode('ascii')

    def reset_tokens(self, access_token):
        dbx = self.dbx
        dbx._oauth2_access_token = access_token
        dbx._oauth2_refresh_token = None
        dbx._oauth2_access_token_expiration = None
