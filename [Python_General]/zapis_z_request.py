import requests 
import os
 
 
def save_url_file(url, dir, file):
       
    print(msg.format(file))
    
    r = requests.get(url, stream = True) 
    file_path = os.path.join(dir, file)
      
    with open(file_path, "wb") as f: 
        f.write(r.content)


url = 'http://mobilo24.eu/spis'
dir = 'd:/temp/'
file = 'spis.html'
save_url_file(url, dir, file)
 
url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'd:/temp/'
file = 'logo.png'
save_url_file(url, dir, file)
