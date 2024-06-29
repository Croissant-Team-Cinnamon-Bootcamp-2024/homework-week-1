from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

google_auth = GoogleAuth()
drive_app = GoogleDrive(google_auth)

folder_id = '1dGRj7HaiKj2YZNcYZA3MB55ZhrcoXaYM'

def get_files_from_results():
    results_dir = 'results'
    return [os.path.join(results_dir, f) for f in os.listdir(results_dir) if os.path.isfile(os.path.join(results_dir, f))]


upload_files = get_files_from_results()

# Function to delete all files in a folder
def delete_files_in_folder(folder_id):
    file_list = drive_app.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    for file in file_list:
        print(f"Deleting file: {file['title']}")
        file.Delete()


def upload_file(file_path_list = upload_files):
    for file in file_path_list:
        upfile =  drive_app.CreateFile({'title':file[5:],'parents':[{'id':folder_id}]})
        upfile.SetContentFile(file)
        upfile.Upload()

