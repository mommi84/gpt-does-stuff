**Goal:** perform a Google search
```
root@7f74ae263cb7:/# apt-get update && apt-get install -y google-chrome-stable
```
> _GPT:_ This command updates the package list and installs the stable version of Google Chrome
```
[...]  lists... 65%Reading package lists... 66%Reading package lists... 66%Reading package lists... 77%Reading package lists... 77%Reading package lists... 77%Reading package lists... 77%Reading package lists... 84%Reading package lists... 84%Reading package lists... 84%Reading package lists... 84%Reading package lists... 84%Reading package lists... 84%Reading package lists... 85%Reading package lists... 85%Reading package lists... 94%Reading package lists... 94%Reading package lists... 94%Reading package lists... 94%Reading package lists... 99%Reading package lists... 99%Reading package lists... 99%Reading package lists... 99%Reading package lists... Done
Reading package lists... 0%Reading package lists... 0%Reading package lists... 0%Reading package lists... 6%Reading package lists... 6%Reading package lists... 6%Reading package lists... 6%Reading package lists... 65%Reading package lists... 65%Reading package lists... 66%Reading package lists... 66%Reading package lists... 77%Reading package lists... 77%Reading package lists... 77%Reading package lists... 77%Reading package lists... 84%Reading package lists... 84%Reading package lists... 84%Reading package lists... 84%Reading package lists... 84%Reading package lists... 84%Reading package lists... 85%Reading package lists... 85%Reading package lists... 94%Reading package lists... 94%Reading package lists... 94%Reading package lists... 94%Reading package lists... 99%Reading package lists... 99%Reading package lists... 99%Reading package lists... 99%Reading package lists... Done
Building dependency tree... 0%Building dependency tree... 0%Building dependency tree... 50%Building dependency tree... 50%Building dependency tree       
Reading state information... 0%Reading state information... 0%Reading state information... Done
E: Unable to locate package google-chrome-stable
root@7f74ae263cb7:/# [Kwget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
> _GPT:_ This command downloads the Google Chrome .deb package from the official website
```
bash: wget: command not found
root@7f74ae263cb7:/# [Kapt-get update && apt-get install -y wget
```
> _GPT:_ This command installs the wget package which is required to download files from the internet
```
[...]  program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/aarch64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/aarch64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/aarch64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/aarch64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Setting up openssl (1.1.1f-1ubuntu2.17) ...
Setting up publicsuffix (20200303.0012-1) ...
Setting up wget (1.20.3-1ubuntu2) ...
Setting up ca-certificates (20211016ubuntu0.20.04.1) ...
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/aarch64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/aarch64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/aarch64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/aarch64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Updating certificates in /etc/ssl/certs...
124 added, 0 removed; done.
Processing triggers for libc-bin (2.31-0ubuntu9.9) ...
Processing triggers for ca-certificates (20211016ubuntu0.20.04.1) ...
Updating certificates in /etc/ssl/certs...
0 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
root@7f74ae263cb7:/# [Kwget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
> _GPT:_ Now that wget is installed, this command downloads the Google Chrome .deb package from the official website
```
[...] gle-chrome-stable_current_amd64.deb
Resolving dl.google.com (dl.google.com)... 142.250.200.14, 2a00:1450:4009:822::200e
Connecting to dl.google.com (dl.google.com)|142.250.200.14|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 93863956 (90M) [application/x-debian-package]
Saving to: 'google-chrome-stable_current_amd64.deb'

          google-ch   0%[                    ]       0  --.-KB/s                        google-chr   2%[                    ]   2.63M  13.0MB/s                       google-chro   7%[>                   ]   7.04M  17.5MB/s                      google-chrom  13%[=>                  ]  12.04M  19.9MB/s                     google-chrome  19%[==>                 ]  17.29M  21.4MB/s                    google-chrome-  25%[====>               ]  22.54M  22.4MB/s                   google-chrome-s  31%[=====>              ]  27.79M  23.0MB/s                  google-chrome-st  36%[======>             ]  33.01M  23.4MB/s                 google-chrome-sta  42%[=======>            ]  38.24M  23.8MB/s                google-chrome-stab  48%[========>           ]  43.51M  24.0MB/s               google-chrome-stabl  54%[=========>          ]  48.79M  24.3MB/s               oogle-chrome-stable  60%[===========>        ]  54.05M  24.4MB/s               ogle-chrome-stable_  66%[============>       ]  59.27M  24.6MB/s               gle-chrome-stable_c  72%[=============>      ]  64.48M  24.7MB/s               le-chrome-stable_cu  77%[==============>     ]  69.69M  24.8MB/s               e-chrome-stable_cur  83%[===============>    ]  74.96M  24.9MB/s    eta 1s     -chrome-stable_curr  89%[================>   ]  80.18M  25.7MB/s    eta 1s     chrome-stable_curre  95%[==================> ]  85.43M  26.0MB/s    eta 1s     google-chrome-stabl 100%[===================>]  89.52M  26.1MB/s    in 3.6s    

2023-03-30 20:18:47 (25.1 MB/s) - 'google-chrome-stable_current_amd64.deb' saved [93863956/93863956]

root@7f74ae263cb7:/# [Kdpkg -i google-chrome-stable_current_amd64.deb
```
> _GPT:_ This command installs the Google Chrome package that was downloaded in the previous step
```
dpkg: error processing archive google-chrome-stable_current_amd64.deb (--install):
 package architecture (amd64) does not match system (arm64)
Errors were encountered while processing:
 google-chrome-stable_current_amd64.deb
root@7f74ae263cb7:/# [Kapt-get install -yq gdebi-core
```
> _GPT:_ This command installs the gdebi-core package which is required to install .deb packages on Ubuntu
```
[...] /man1/xzmore.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzless.1.gz because associated file /usr/share/man/man1/xzless.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzdiff.1.gz because associated file /usr/share/man/man1/xzdiff.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzcmp.1.gz because associated file /usr/share/man/man1/xzcmp.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzgrep.1.gz because associated file /usr/share/man/man1/xzgrep.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzegrep.1.gz because associated file /usr/share/man/man1/xzegrep.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzfgrep.1.gz because associated file /usr/share/man/man1/xzfgrep.1.gz (of link group lzma) doesn't exist
Setting up python-apt-common (2.0.1ubuntu0.20.04.1) ...
Setting up libmpdec2:arm64 (2.4.2-3) ...
Setting up readline-common (8.0-4) ...
Setting up iso-codes (4.4-1) ...
Setting up libreadline8:arm64 (8.0-4) ...
Setting up libpython3.8-stdlib:arm64 (3.8.10-0ubuntu1~20.04.7) ...
Setting up python3.8 (3.8.10-0ubuntu1~20.04.7) ...
Setting up libpython3-stdlib:arm64 (3.8.2-0ubuntu2) ...
Setting up python3 (3.8.2-0ubuntu2) ...
running python rtupdate hooks for python3.8...
running python post-rtupdate hooks for python3.8...
Setting up python3-six (1.14.0-2) ...
Setting up lsb-release (11.1.0ubuntu2) ...
Setting up python3-pkg-resources (45.2.0-1ubuntu0.1) ...
Setting up python3-apt (2.0.1ubuntu0.20.04.1) ...
Setting up python3-chardet (3.0.4-4build1) ...
Setting up python3-debian (0.1.36ubuntu1) ...
Setting up gdebi-core (0.9.5.7+nmu3) ...
Processing triggers for libc-bin (2.31-0ubuntu9.9) ...
root@7f74ae263cb7:/# [Kapt-get install -yq python3-pip
```
> _GPT:_ This command installs the Python package manager (pip) for Python 3 on Ubuntu
```
[...]  up gpg-wks-server (2.2.19-3ubuntu2.2) ...
Setting up cpp-9 (9.4.0-1ubuntu1~20.04.1) ...
Setting up libperl5.30:arm64 (5.30.0-9ubuntu0.3) ...
Setting up libc6-dev:arm64 (2.31-0ubuntu9.9) ...
Setting up libhx509-5-heimdal:arm64 (7.7.0+dfsg-1ubuntu1.4) ...
Setting up libgcc-9-dev:arm64 (9.4.0-1ubuntu1~20.04.1) ...
Setting up perl (5.30.0-9ubuntu0.3) ...
Setting up libexpat1-dev:arm64 (2.2.9-1ubuntu0.6) ...
Setting up libpython3.8-dev:arm64 (3.8.10-0ubuntu1~20.04.7) ...
Setting up libdpkg-perl (1.19.7ubuntu3.2) ...
Setting up zlib1g-dev:arm64 (1:1.2.11.dfsg-2ubuntu1.5) ...
Setting up cpp (4:9.3.0-1ubuntu2) ...
Setting up libkrb5-26-heimdal:arm64 (7.7.0+dfsg-1ubuntu1.4) ...
Setting up gcc-9 (9.4.0-1ubuntu1~20.04.1) ...
Setting up libpython3-dev:arm64 (3.8.2-0ubuntu2) ...
Setting up libstdc++-9-dev:arm64 (9.4.0-1ubuntu1~20.04.1) ...
Setting up libfile-fcntllock-perl (0.22-3build4) ...
Setting up libalgorithm-diff-perl (1.19.03-2) ...
Setting up libheimntlm0-heimdal:arm64 (7.7.0+dfsg-1ubuntu1.4) ...
Setting up gcc (4:9.3.0-1ubuntu2) ...
Setting up dpkg-dev (1.19.7ubuntu3.2) ...
Setting up libgssapi3-heimdal:arm64 (7.7.0+dfsg-1ubuntu1.4) ...
Setting up g++-9 (9.4.0-1ubuntu1~20.04.1) ...
Setting up python3.8-dev (3.8.10-0ubuntu1~20.04.7) ...
Setting up g++ (4:9.3.0-1ubuntu2) ...
update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
update-alternatives: warning: skip creation of /usr/share/man/man1/c++.1.gz because associated file /usr/share/man/man1/g++.1.gz (of link group c++) doesn't exist
Setting up build-essential (12.8ubuntu1.1) ...
Setting up libalgorithm-diff-xs-perl (0.04-6) ...
Setting up libalgorithm-merge-perl (0.08-3) ...
Setting up libldap-2.4-2:arm64 (2.4.49+dfsg-2ubuntu1.9) ...
Setting up dirmngr (2.2.19-3ubuntu2.2) ...
Setting up python3-dev (3.8.2-0ubuntu2) ...
Setting up gpg-wks-client (2.2.19-3ubuntu2.2) ...
Setting up gnupg (2.2.19-3ubuntu2.2) ...
Processing triggers for libc-bin (2.31-0ubuntu9.9) ...
root@7f74ae263cb7:/# [Kpip3 install google
```
> _GPT:_ This command installs the Google package for Python using pip3
```
Collecting google
  Downloading google-3.0.0-py2.py3-none-any.whl (45 kB)
     |███████▎                        | 10 kB 7.9 MB/s eta 0:00:01     |██████████████▌                 | 20 kB 4.9 MB/s eta 0:00:01     |█████████████████████▊          | 30 kB 3.6 MB/s eta 0:00:01     |█████████████████████████████   | 40 kB 2.2 MB/s eta 0:00:01     |████████████████████████████████| 45 kB 2.0 MB/s 
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.12.0-py3-none-any.whl (132 kB)
     |██▌                             | 10 kB 2.6 MB/s eta 0:00:01     |█████                           | 20 kB 2.8 MB/s eta 0:00:01     |███████▍                        | 30 kB 4.2 MB/s eta 0:00:01     |██████████                      | 40 kB 4.9 MB/s eta 0:00:01     |████████████▍                   | 51 kB 5.3 MB/s eta 0:00:01     |██████████████▉                 | 61 kB 6.3 MB/s eta 0:00:01     |█████████████████▍              | 71 kB 3.5 MB/s eta 0:00:01     |███████████████████▉            | 81 kB 4.0 MB/s eta 0:00:01     |██████████████████████▎         | 92 kB 4.5 MB/s eta 0:00:01     |████████████████████████▉       | 102 kB 4.1 MB/s eta 0:00:01     |███████████████████████████▎    | 112 kB 4.1 MB/s eta 0:00:01     |█████████████████████████████▊  | 122 kB 4.1 MB/s eta 0:00:01     |████████████████████████████████| 132 kB 4.1 MB/s 
Collecting soupsieve>1.2
  Downloading soupsieve-2.4-py3-none-any.whl (37 kB)
Installing collected packages: soupsieve, beautifulsoup4, google
Successfully installed beautifulsoup4-4.12.0 google-3.0.0 soupsieve-2.4
root@7f74ae263cb7:/# python3
```
> _GPT:_ This command opens the Python 3 interpreter
```
Python 3.8.10 (default, Mar 13 2023, 10:26:41) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import googlesearch
```
> _GPT:_ This command imports the googlesearch module in Python
```

>>> import googlesearch
```
> _GPT:_ This command imports the googlesearch module in Python
```

>>> from googlesearch import search
```
> _GPT:_ This command imports the search function from the googlesearch module
```

>>> query = 'best pizza in new york'
```
> _GPT:_ This command sets the query variable to 'best pizza in new york'
```

>>> for j in search(query, num_results=5): print(j)
```
> _GPT:_ This command performs a Google search for the query and prints the top 5 results
```

... 
```