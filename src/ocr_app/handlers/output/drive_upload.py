import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def get_files_from_results(results_dir):
    return [
        os.path.join(results_dir, f)
        for f in os.listdir(results_dir)
        if os.path.isfile(os.path.join(results_dir, f))
    ]


def get_drive_app(secrets_dir):
    client_secrets_file = os.path.join(secrets_dir, 'client_secrets.json')
    google_auth = GoogleAuth()
    google_auth.settings['client_config_file'] = client_secrets_file
    return GoogleDrive(google_auth)


def upload_file(env_folder_id, secrets_dir, results_dir):
    drive_app = get_drive_app(secrets_dir)
    file_path_list = get_files_from_results(results_dir)
    print(f"Folder ID: {env_folder_id}")
    print(
        f"Client secrets file path: {os.path.join(secrets_dir, 'client_secrets.json')}"
    )
    print(f"Results directory: {results_dir}")

    for file in file_path_list:
        file_name = os.path.basename(file)
        upfile = drive_app.CreateFile(
            {'title': file_name, 'parents': [{'id': env_folder_id}]}
        )
        upfile.SetContentFile(file)
        upfile.Upload()
        print(f"Uploaded file: {file_name}")


def file_exists_in_folder(folder_id, file_name, secrets_dir):
    drive_app = get_drive_app(secrets_dir)
    query = f"'{folder_id}' in parents and trashed=false and title='{file_name}'"
    file_list = drive_app.ListFile({'q': query}).GetList()
    return len(file_list) > 0
