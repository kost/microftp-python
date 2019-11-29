#!/usr/bin/env python

import microftp

ftp = microftp.microFTP("127.0.0.1")
ftp.set_pasv(True)
ftp.login()
ftp.set_debuglevel(9999)
ftp.cwd(args.dir)
print(ftp.raw_retrlines('LIST'))
ftp.quit()


