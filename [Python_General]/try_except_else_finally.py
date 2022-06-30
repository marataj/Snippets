import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
     
url = 'http://www.mobilo24.eu/spis/'
dir = 'd:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'
 
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)


try:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
        print("Removing file: {}".format(tmpfile_path))
    save_url_to_file(url,tmpfile_path)
    shutil.copyfile(tmpfile_path,file_path)
    
except Exception as e:
    print("Error: {}".format(e))
else:
    print("Computing completed successfully")
finally:
     if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
        print("Removing file: {}".format(tmpfile_path))
