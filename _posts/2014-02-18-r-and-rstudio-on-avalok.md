---
layout: post
title:  "R and RStudio on Avalok"
date:   2014-02-18 08:34
author: Raf Winand
categories: R avalok
published: false
tags:
- R
- avalok
---
The version of R that is installed on Avalok is 2.13 while 3.0.2 is the latest version and is required by a number of packages. There is a way to install both RStudio and a personal version of R on Avalok and still work through sge.

First you have to download the RStudio binaries from http://www.rstudio.com/ide/download/desktop. On Avalok you can use the Debian 6+/Ubuntu 10.04+ binary packages because compiling them from source doesn't work. You can just unpack them in your personal directory

```
tar -zxvf rstudio-0.98.501-amd64-debian.tar.gz
```

Next, you have to compile R from source which you can get from http://cran.freestatistics.org/ Unpack the content in your home folder: `tar -zxvf R-3.0.2.tar.gz`

Run configure but make sure you add the flag that will build R as a shared library because RStudio needs the files that are created by this installation. If you don't do this you will get an error when starting RStudio. Also specify the directory you want R to install to because the default directory is not accessible: `./configure --enable-R-shlib --prefix=<yourDir>/R`

Finally install R by running the following commands.

```
make
make check
make install
```

Because RStudio will look for the default installation of R it will not use this installation of R. To have RStudio use this version of R you have to set an environment variable using `export RSTUDIO_WHICH_R=<yourDir>/R/bin/R`.

Now to run RStudio through sge you just open a terminal window in your VNC session, type *sge* and run RStudio from the command line that opens. Make sure you exported the environment variable first because otherwise RStudio will just use the default version of R. Now you can also install all packages to your personal version of R through RStudio.
