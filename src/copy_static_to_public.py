import os
import shutil

def copy_static_to_public(public_folder, static_folder, delete_public=True):
   
    if delete_public == True:
        shutil.rmtree(public_folder,ignore_errors=True)
        os.mkdir(public_folder)

    folder_contents = os.listdir(static_folder)

    for item in folder_contents:
        src = os.path.join(static_folder, item)
        dest = os.path.join(public_folder, item)

        if os.path.isfile(src):
            shutil.copy(src, dest)
        else:
            os.mkdir(dest)
            copy_static_to_public(dest, src, delete_public=False )
    

    
