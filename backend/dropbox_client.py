from dropbox import Dropbox, files
import string

class MailmanClient():
    def __init__(self):
        self.dbx = Dropbox(
            oauth2_access_token="temp_token"
        )

    def upload_file_to_dropbox(self, file_contents, path, file_name, access_token):
        if not type(file_contents) is bytes:
            file_contents = self.convert_file_content_to_bytes(file_contents)
        path = "%s/%s" % (path, file_name)

        self.reset_tokens(access_token)
        self.dbx.files_upload(
            file_contents, 
            path, 
            mode=files.WriteMode.overwrite,  # when saving over a previous email/thread, overrides the file
            strict_conflict=False
            )
        

    def convert_file_content_to_bytes(self, file_contents):
        return file_contents.encode('ascii')

    def reset_tokens(self, access_token):
        dbx = self.dbx
        dbx._oauth2_access_token = access_token
        dbx._oauth2_refresh_token = None
        dbx._oauth2_access_token_expiration = None

    def upload_email(self, message_obj, path, access_token):
        if message_obj.attachments:
            attachments_path = "%s/attachments" % path
            for attachment in message_obj.attachments:
                file_name = attachments.filename
                file_contents = attachments.payload
                self.upload_file_to_dropbox(file_contents, attachments_path, file_name, access_token)

        self.upload_file_to_dropbox(message_obj.text, path, message_obj.subject, access_token)
