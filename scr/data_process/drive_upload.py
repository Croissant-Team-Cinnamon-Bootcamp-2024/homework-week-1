from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

folder_id = '1dGRj7HaiKj2YZNcYZA3MB55ZhrcoXaYM'
current_dir = os.path.dirname(os.path.abspath(__file__))
client_secrets_file = os.path.join(current_dir, 'client_secrets.json')

google_auth = GoogleAuth()
google_auth.settings['client_config_file'] = client_secrets_file
drive_app = GoogleDrive(google_auth)

def get_files_from_results():
    results_dir = 'results'
    return [os.path.join(results_dir, f) for f in os.listdir(results_dir) if os.path.isfile(os.path.join(results_dir, f))]


upload_files = get_files_from_results()

# Function to delete all files in a folder
def delete_files_in_folder(folder_id = folder_id):
    file_list = drive_app.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    for file in file_list:
        print(f"Deleting file: {file['title']}")
        file.Delete()


# def upload_file(file_path_list = upload_files):
#     for file in file_path_list:
#         upfile =  drive_app.CreateFile({'title':file[8:],'parents':[{'id':folder_id}]})
#         upfile.SetContentFile(file)
#         upfile.Upload()

def upload_file(file_path_list=upload_files):
    for file in file_path_list:
        file_name = os.path.basename(file)
        upfile = drive_app.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
        upfile.SetContentFile(file)
        upfile.Upload()
        print(f"Uploaded file: {file_name}")

def file_exists_in_folder(folder_id, file_name):
    query = f"'{folder_id}' in parents and trashed=false and title='{file_name}'"
    file_list = drive_app.ListFile({'q': query}).GetList()
    return len(file_list) > 0

if __name__ == '__main__':
    upload_file()
    # delete_files_in_folder()