from Google import Create_Service
import mimetypes
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload

CLIENT_SECRET_FILE = 'oauth-credentials.json'
API_NAME='drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1OfpvoyDUfRjSqDjxH45tEjMD0TmElWSq'

file_names = ['test.txt']
file_type = ['text/plain']

for file_name, mime_type in zip(file_names, file_type):
    file_metadata = {
        'name' : file_name,
        'parents' : [folder_id]
    }

    media = MediaFileUpload('{0}'.format(file_name),mimetype=mime_type)

    service.files().create(
        body = file_metadata,
        media_body = media,
        fields = 'id'
    ).execute()

file_ids = []
file_names = []


"""
@deconstructible
class GoogleDriveStorage(Storage):
    def __init__(self):
        pass

    def _open(self, name, mode='rb'):
        file_data = self._check_file_exists(name)
        request = self._drive_service.files().get_media(
            fileId=file_data['id'])
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            _, done = downloader.next_chunk()
        fh.seek(0)
        return File(fh, name)

    def _save(self, name, content):
        name = os.path.join(settings.GOOGLE_DRIVE_STORAGE_MEDIA_ROOT, name)
        folder_path = os.path.sep.join(self._split_path(name)[:-1])
        folder_data = self._get_or_create_folder(folder_path)
        parent_id = None if folder_data is None else folder_data['id']
        # Now we had created (or obtained) folder on GDrive
        # Upload the file
        mime_type, _ = mimetypes.guess_type(name)
        if mime_type is None:
            mime_type = self._UNKNOWN_MIMETYPE_
        media_body = MediaIoBaseUpload(
            content.file, mime_type, resumable=True, chunksize=1024 * 512)
        body = {
            'name': self._split_path(name)[-1],
            'mimeType': mime_type
        }
        # Set the parent folder.
        if parent_id:
            body['parents'] = [parent_id]
        file_data = self._drive_service.files().create(
            body=body,
            media_body=media_body).execute()

        # Setting up permissions
        for p in self._permissions:
            self._drive_service.permissions().create(
                fileId=file_data['id'], body={**p.raw}).execute()

        return file_data.get('originalFilename', file_data.get('name'))

    def delete(self, name):
        file_data = self._check_file_exists(name)
        if file_data is not None:
            self._drive_service.files().delete(
                fileId=file_data['id']).execute()

    def exists(self, name):
        return self._check_file_exists(name) is not None

    def url(self, name):
        file_data = self._check_file_exists(name)
        if file_data is None:
            return None
        return file_data['webContentLink']
"""