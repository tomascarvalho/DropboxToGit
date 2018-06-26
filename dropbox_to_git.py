import requests, zipfile, io, subprocess, os, sys
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ZIP_FILE_URL = os.getenv('ZIP_FILE_URL')
if not ZIP_FILE_URL:
    sys.exit('Error getting zip file url from env')

try:
    r = requests.get(ZIP_FILE_URL)
except:
    sys.exit('Error getting file from dropbox. Make sure that ZIP_FILE_URL is a valid download URL')

z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(path='Report')
commit_message = 'thesis backup: ' + datetime.now().isoformat()
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", commit_message])
subprocess.call(["git", "push"])
