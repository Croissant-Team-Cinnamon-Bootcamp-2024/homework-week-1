import os
import sys
sys.path.append('../src')

from data_process import drive_upload
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

google_auth = GoogleAuth()
drive_app = GoogleDrive(google_auth)


def test_delete_files_in_folder():
    drive_upload.delete_files_in_folder('1dGRj7HaiKj2YZNcYZA3MB55ZhrcoXaYM')

    def is_folder_empty(folder_id):
        file_list = drive_app.ListFile(
            {'q': f"'{drive_upload.folder_id}' in parents and trashed=false"}
        ).GetList()
        return len(file_list) == 0

    if is_folder_empty(drive_upload.folder_id):
        print("The folder is empty.")
    else:
        print("The folder is not empty.")


def test_upload_files():
    file_paths = drive_upload.get_files_from_results()
    drive_upload.upload_file(file_paths)

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        if drive_upload.file_exists_in_folder(drive_upload.folder_id, file_name):
            print(f"The file '{file_name}' exists in the folder.")
        else:
            print(f"The file '{file_name}' does not exist in the folder.")


# if __name__ == "__main__":
#     test_delete_files_in_folder()
#     test_upload_files()
