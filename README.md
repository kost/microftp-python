[![Build Status](https://travis-ci.org/kost/microftp-python.png)](https://travis-ci.org/kost/microftp-python)

microftp
======
Python module to handle FTP protocol (client side only). It is modified original ftplib to handle broken FTP servers in embedded world.

Requirements
============

It should work with both python2 and python3 with simple pip commands:
```
pip install microftp
```

microftpcmd examples
========

Few microftpcmd examples:
```
microftpcmd --host 192.168.4.1 ls
microftpcmd --host 192.168.4.1 -d -v ls
microftpcmd --host 192.168.4.1 put local.txt remote.txt
microftpcmd --host 192.168.4.1 put local.txt remote.txt
microftpcmd --host 192.168.4.1 get remote-file.txt local-file.txt
microftpcmd --host 192.168.4.1 rm file-to-delete.txt
```

Note that you can also specify basic parameters using environment variables:
```
export MICROFTP_HOST=127.0.0.1
export MICROFTP_USER=user
export MICROFTP_PASSWORD=password
export MICROFTP_DIR=/something
```

and then you can just specify command:
```
microftpcmd ls
```

All options are listed using --help:

```
microftpcmd --help
```

Requirements
============

It should work with both python2 and python3 with simple pip commands:
```
sudo apt-get update
sudo apt-get install -y python3 python3-pip
sudo pip3 install microftp
```

Examples
========

Simple example to get devices and its current status:

```
import microftp

ftp = microftp.microFTP("127.0.0.1")
ftp.set_pasv(True)
ftp.login()
ftp.set_debuglevel(9999)
ftp.cwd(args.dir)
print(ftp.raw_retrlines('LIST'))
ftp.quit()
```

Manual
======

```
usage: microftpcmd [-h] [--host HOST] [--port PORT] [--delay DELAY]
                   [--block BLOCK] [--verbose] [--debug] [--user USER]
                   [--password PASSWORD] [--site SITE] [--siteafter SITEAFTER]
                   [--dir DIR]
                   CMD [CMD ...]

microftp - connect to broken or embedded FTP servers

positional arguments:
  CMD                   commands for ftp

optional arguments:
  -h, --help            show this help message and exit
  --host HOST, -i HOST  Host to connect to
  --port PORT, -P PORT  Port to connect to
  --delay DELAY         Introduce delay between blocks
  --block BLOCK         Size of block
  --verbose, -v         Enable verbose messages
  --debug, -d           Enable debugging messages
  --user USER, -u USER  Specify FTP user
  --password PASSWORD, -p PASSWORD
                        Specify FTP password
  --site SITE, -S SITE  Specify site command (executed before transfer)
  --siteafter SITEAFTER, -A SITEAFTER
                        Specify site command (executed after transfer)
  --dir DIR, -D DIR     Specify FTP dir to change before transfer

microftpcmd --host 192.168.4.1 ls
microftpcmd --host 192.168.4.1 get remote-file.txt local-file.txt
microftpcmd --host 192.168.4.1 put local-file.txt remote-file.txt
microftpcmd --host 192.168.4.1 -S mount -D sd -A umount ls
microftpcmd --host 192.168.4.1 -S mount -D sd -A site /sd/blink.bit -A umount put blink.bit blink.bit
```

ulx3s
=====

Some specific ulx3s examples:
```
microftpcmd --host 192.168.5.7 --delay 0.3 --block 32 -v -d --user root put ~/wget /root/wget
microftpcmd --host 192.168.4.1 -S mount -D sd -A umount ls
microftpcmd --host 192.168.4.1 -S mount -D sd -A site /sd/blink.bit -A umount put blink.bit blink.bit
```

