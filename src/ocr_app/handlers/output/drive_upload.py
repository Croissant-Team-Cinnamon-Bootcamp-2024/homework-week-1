import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def get_files_from_results(results_dir):
    """
    Collects all file paths from the specified directory.

    Args:
        results_dir (str): The directory to scan for files.

    Returns:
        list: A list of full paths to the files in the specified directory.
    """
    return [
        os.path.join(results_dir, f)
        for f in os.listdir(results_dir)
        if os.path.isfile(os.path.join(results_dir, f))
    ]


def get_drive_app(secrets_dir):
    """
    Initializes and returns a GoogleDrive object using a specified client secrets file.

    Args:
        secrets_dir (str): Directory containing the 'client_secrets.json' file.

    Returns:
        GoogleDrive: An authenticated GoogleDrive object.
    """
    client_secrets_file = os.path.join(secrets_dir, 'client_secrets.json')
    google_auth = GoogleAuth()
    google_auth.settings['client_config_file'] = client_secrets_file
    return GoogleDrive(google_auth)


def upload_file(env_folder_id, secrets_dir, results_dir):
    """
    Uploads all files from a local directory to a specified Google Drive folder.

    Args:
        env_folder_id (str): The Google Drive folder ID where the files will be uploaded.
        secrets_dir (str): The directory containing the Google API client secrets.
        results_dir (str): The directory from which files will be uploaded.

    Prints the paths of uploaded files and relevant directory info.
    """
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
    """
    Checks if a specific file exists in a Google Drive folder.

    Args:
        folder_id (str): The Google Drive folder ID to search within.
        file_name (str): The name of the file to search for.
        secrets_dir (str): Directory containing the Google API client secrets.

    Returns:
        bool: True if the file exists in the folder, False otherwise.
    """
    drive_app = get_drive_app(secrets_dir)
    query = f"'{folder_id}' in parents and trashed=false and title='{file_name}'"
    file_list = drive_app.ListFile({'q': query}).GetList()
    return len(file_list) > 0
