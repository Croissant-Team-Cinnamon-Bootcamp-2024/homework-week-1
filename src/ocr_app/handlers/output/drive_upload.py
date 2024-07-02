import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

client_secrets_file = r'secrets\client_secrets.json'

google_auth = GoogleAuth()
google_auth.settings['client_config_file'] = client_secrets_file
drive_app = GoogleDrive(google_auth)


def get_files_from_results():
    results_dir = 'results'
    return [
        os.path.join(results_dir, f)
        for f in os.listdir(results_dir)
        if os.path.isfile(os.path.join(results_dir, f))
    ]


def upload_file(env_folder_id):
    file_path_list = get_files_from_results()
    print(env_folder_id)
    for file in file_path_list:
        file_name = os.path.basename(file)
        upfile = drive_app.CreateFile(
            {'title': file_name, 'parents': [{'id': env_folder_id}]}
        )
        upfile.SetContentFile(file)
        upfile.Upload()
        print(f"Uploaded file: {file_name}")


def file_exists_in_folder(folder_id, file_name):
    query = f"'{folder_id}' in parents and trashed=false and title='{file_name}'"
    file_list = drive_app.ListFile({'q': query}).GetList()
    return len(file_list) > 0


if __name__ == '__main__':
    upload_file()
