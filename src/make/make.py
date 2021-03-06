#!/usr/bin/python
#Copyright (c) 2013 James Beedy

import os, errno
import sys, subprocess
from distutils.dir_util import mkpath
import shutil

def mkdirp(directory):
    """Creates an empty directory. Python implementation of mkdir. """
    if not os.path.isdir(directory):
        mkpath(directory)

def touch(fname):
    """Creates an empty file. Python implementation of touch. """
    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, 'w').close()

class Make(object):
    """Class to be instantiated with object that contains projectname and modulename. """
    def __init__(self, args):
        self.projectname = str(args.projectname)
        self.modulename = str(args.modulename)

    def mkdirs(self):
        """Creates Directory Structure for Make. """
        mkdirp(self.projectname)
        mkdirp(self.projectname + '/src')
        mkdirp(self.projectname + '/requirements')
        mkdirp(self.projectname + '/src' + '/' + self.modulename)
        touch(self.projectname + '/requirements/requirements.txt')
        touch(self.projectname + '/Makefile.am')
        touch(self.projectname + '/configure.ac')
        touch(self.projectname + '/src/' + self.projectname + '.in')
        touch(self.projectname + '/src/' + 'Makefile.am')    
        touch(self.projectname + '/src/' + self.modulename + '/' + self.modulename + '.py')
        touch(self.projectname + '/src/' + self.modulename + '/__init__.py')
        touch(self.projectname + '/src/' + self.modulename + '/Makefile.am')
        touch(self.projectname + '/AUTHORS')
        touch(self.projectname + '/ChangeLog')
        touch(self.projectname + '/NEWS')
        touch(self.projectname + '/README')
    
    def writetofiles(self):
        """"Creates files. """
        with open(self.projectname + '/' + 'configure.ac', 'w') as config:
            config.write('AC_INIT([' + self.projectname + '], [0.1])\n')
            config.write('AM_INIT_AUTOMAKE\n')
            config.write('AM_PATH_PYTHON([2.7])\n')
            config.write('AC_CONFIG_FILES([Makefile src/Makefile src/' + self.modulename + '/Makefile])\n')
            config.write('AC_OUTPUT')
        with open(self.projectname + '/Makefile.am', 'w') as mkfile:
            mkfile.write('SUBDIRS = src')
        with open(self.projectname + '/src/Makefile.am', 'w') as mkfile:
            mkfile.write('SUBDIRS = ' + self.modulename + '\n\n')
            mkfile.write('bin_SCRIPTS = ' + self.projectname + '\n')
            mkfile.write('CLEANFILES = $(bin_SCRIPTS)\n')
            mkfile.write('EXTRA_DIST = ' + self.projectname + '.in\n\n')
            mkfile.write('do_substitution = sed -e "s,[@]pythondir[@],$(pythondir),g"\ \n')
            mkfile.write('	-e "s,[@]PACKAGE[@],$(PACKAGE),g" \ \n')
            mkfile.write('	-e "s,[@]VERSION[@],$(VERSION),g" \n\n')
            mkfile.write(self.projectname + ': ' + self.projectname + '.in Makefile\n')
            mkfile.write('	$(do_substitution) < $(srcdir)/' + self.projectname + '.in > ' + self.projectname + '\n')
            mkfile.write('	chmod +x ' + self.projectname)
        with open(self.projectname + '/src/' + self.modulename + '/Makefile.am', 'w') as mkfile:
            mkfile.write(self.modulename + '_PYTHON = \ \n')
            mkfile.write('	' + self.modulename + '.py \ \n')
            mkfile.write('	__init__.py \n\n')
            mkfile.write(self.modulename + 'dir = $(pythondir)/' + self.modulename + '\n')

    def deps(self):
        os.system('cd ' + self.projectname + '/requirements')
        os.system('pip freeze > freeezeout.txt')    
        
        

                
