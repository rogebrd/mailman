from dropbox import Dropbox, files

class MailmanDropboxClient():
    def __init__(self):
        self.dbx = Dropbox(
            oauth2_access_token="temp_token"
        )

    def upload_file_to_dropbox(self, file_contents, path, file_name, access_token):
        if not type(file_contents) is bytes:
            file_contents = self.convert_file_content_to_bytes(file_contents)
        self.reset_tokens(access_token)
        path = "%s/%s" % (path, file_name)
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

    def upload_email(self, formatted_email, path, access_token):
        attachments = formatted_email.msg.attachments
        if attachments:
            attachments_path = "%s/Attachments" % path
            for attachment in attachments:
                file_name = attachment.filename
                file_contents = attachment.payload
                self.upload_file_to_dropbox(file_contents, attachments_path, file_name, access_token)
        file_name = "%s.txt" % formatted_email.formatted_subject
        file_contents = formatted_email.formatted_text
        self.upload_file_to_dropbox(file_contents, path, file_name, access_token)
