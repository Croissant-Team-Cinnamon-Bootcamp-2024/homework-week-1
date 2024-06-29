import drive_upload
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

google_auth = GoogleAuth()
drive_app = GoogleDrive(google_auth)

def test_delete_files_in_folder():
    drive_upload.delete_files_in_folder('1dGRj7HaiKj2YZNcYZA3MB55ZhrcoXaYM')
    def is_folder_empty(folder_id):
        file_list = drive_app.ListFile({'q': f"'{drive_upload.folder_id}' in parents and trashed=false"}).GetList()
        return len(file_list) == 0
    if is_folder_empty(drive_upload.folder_id):
        print("The folder is empty.")
    else:
        print("The folder is not empty.")

def test_upload_files():
    file_names = drive_upload.get_files_from_results()
    drive_upload.upload_file(file_names)   
    def file_exists_in_folder(folder_id, file_name):
        query = f"'{folder_id}' in parents and trashed=false and title='{file_name}'"
        file_list = drive_app.ListFile({'q': query}).GetList()
        return len(file_list) > 0
    for file_name in file_names:
        if file_exists_in_folder(drive_upload.folder_id, file_name):
            print(f"The file '{file_name}' already exists in the folder.")
        else:
            print(f"The file '{file_name}' does not exist in the folder.")
            return
test_delete_files_in_folder()
# test_upload_files()
