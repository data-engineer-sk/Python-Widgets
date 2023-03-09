# The below YouTube Video downloader works on 27 Feb 2023
# However, the quality is not really good, should be fixed later
# By Samuel Ko

import pytube
from pytube import YouTube

""" Go to stackoverflow.com, search for 
Error in pytube <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] 
certificate verify failed: unable to get local issuer certificate 
(_ssl.c:997)>
"""
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context
link = input('Enter The Youtube Video URL: ')
dn = pytube.YouTube(link)
# dn.streams.first().download() # original script
dn.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print('Your Video Has Been Downloaded', link)


