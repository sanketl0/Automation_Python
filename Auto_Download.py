
from sys import *
from os import *
import requests
from urllib.parse import urlparse

def is_downloadable(url):
    h = requests.head(url,allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)

def pc_Download(url):
    allowed = is_downloadable(url)
    if allowed:
        try:
            res = requests.get(url,allow_redirects=True)
            filename=get_filename_from_cd(url)
            fd = open(filename,"wb")
            
            for buffer in res.iter_content(1024):
                fd.write(buffer)
            fd.close()
            return True
        except Exception as E:
            return False

    else:
        return False
def main():

    print("Application  name:",argv[0])
    if(len(argv) == 2):
        if((argv[1]=="-h") or (argv[1]=="-H")):
            print("Help : This script is used to download file_")
            exit()

        if((argv[1]=="-u") or (argv[1]=="-U")):
            print("usages : ApplicationName")
            exit()

    url = 'https://www.google.com/favicon.ico'
    
    result = pc_Download(url)
    
    if result:
        print("File Download successfully")
    else:
        print("Filed to Download")

if __name__ == "__main__":
    main()