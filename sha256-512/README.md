**SHA256-512.V1**

This tool provides decoding-encoding with SHA256-512.

**WARNING:** You need to download word lists for decrypt method!

  ```usage: sha256-512.py [-h] [-hs HASHOBJECT] [-p FILEPATH] [-e | -d]
     -h, --help            show this help message and exit
     -hs HASHOBJECT, --hashobject HASHOBJECT use as : -hs [string] or --hashobject [string]
     -p FILEPATH, --filepath FILEPATH use as : -p [filepath] or --filepath [filepath]
     -e, --encode          use as:-hs [object] -e
     -d, --decode          use as: -hs [object] -p [path] -d

    Example:
   
      CommandLine ~$ python3 sha256-512.py -hs [hash object here] -e

      CommandLine ~$ python3 sha256-512.py -hs [hashed object here] -p [word list path here] -d

      CommandLine ~$ python3 sha256-512.py -hs cyber -e

      ENCODED OBJECT (SHA256):  b4bf5d7e5fcf89ef8adb64ec9c624db850d10f2afef020ed9ef23892df0833af
	  
	  ENCODED OBJECT (SHA512):  ff5bb17dfe26eba3c6ac9641a70a96d92b1e7f219899ec58141b643c67d8d6fc21dd5f731d095d0f07eefd771be1bab459a4e7e8bb95d9768e6498b106c9f923

      CommandLine ~$ python3 sha256-512.py -hs b4bf5d7e5fcf89ef8adb64ec9c624db850d10f2afef020ed9ef23892df0833af -p C:\Users\user1 -d

      DECODED OBJECT (SHA256):  b4bf5d7e5fcf89ef8adb64ec9c624db850d10f2afef020ed9ef23892df0833af RESULT: cyber
	  
	  CommandLine ~$ python3 sha256-512.py -hs ff5bb17dfe26eba3c6ac9641a70a96d92b1e7f219899ec58141b643c67d8d6fc21dd5f731d095d0f07eefd771be1bab459a4e7e8bb95d9768e6498b106c9f923 -p C:\Users\user1 -d
	  
	  DECODED OBJECT (SHA512):  ff5bb17dfe26eba3c6ac9641a70a96d92b1e7f219899ec58141b643c67d8d6fc21dd5f731d095d0f07eefd771be1bab459a4e7e8bb95d9768e6498b106c9f923 RESULT: cyber
	```
Attention:Only Educational Purposes.