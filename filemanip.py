#!/usr/bin/python
import os, errno
import sys, subprocess
from distutils.dir_util import mkpath
import shutil

def mkdirp(directory):
    """ Creates an empty directory. """

    if not os.path.isdir(directory):
        mkpath(directory)

def touch(fname):
    """ Creates an empty file """

    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, 'w').close()


def mkdirs(projectname, modulename):
    """ Creates Directory Structure for Make. """
    
    mkdirp(projectname)
    mkdirp(projectname + '/src')
    mkdirp(projectname + '/src' + '/' + modulename)
    touch(projectname + '/' + 'Makefile.am')
    touch(projectname + '/' + 'configure.ac')
    touch(projectname + '/src' + '/' + projectname + '.in')
    touch(projectname + '/src' + '/' + 'Makefile.am')    
    touch(projectname + '/src' + '/' + modulename + '/' + modulename + '.py')
    touch(projectname + '/src' + '/' + modulename + '/' + '__init__.py')
    touch(projectname + '/src' + '/' + modulename + '/' + 'Makefile.am')
    touch(projectname + '/AUTHORS')
    touch(projectname + '/ChangeLog')
    touch(projectname + '/NEWS')
    touch(projectname + '/README')
    

def writetofiles(projectname, modulename):
    """"Creates files. """

    with open(projectname + '/' + 'configure.ac', 'w') as config:
        config.write('AC_INIT([' + projectname + '], [0.1])\n')
        config.write('AM_INIT_AUTOMAKE\n')
        config.write('AM_PATH_PYTHON([2.7])\n')
        config.write('AC_CONFIG_FILES([Makefile src/Makefile src/' + modulename + '/Makefile])\n')
        config.write('AC_OUTPUT')
        
    with open(projectname + '/Makefile.am', 'w') as mkfile:
        mkfile.write('SUBDIRS = src')
        
    with open(projectname + '/src/Makefile.am', 'w') as mkfile:
        mkfile.write('SUBDIRS = ' + modulename + '\n\n')
        mkfile.write('bin_SCRIPTS = ' + projectname + '\n')
        mkfile.write('CLEANFILES = $(bin_SCRIPTS)\n')
        mkfile.write('EXTRA_DIST = ' + projectname + '.in\n\n')
        mkfile.write('do_substitution = sed -e "s,[@]pythondir[@],$(pythondir),g"\ \n')
        mkfile.write('	-e "s,[@]PACKAGE[@],$(PACKAGE),g" \ \n')
        mkfile.write('	-e "s,[@]VERSION[@],$(VERSION),g" \n\n')
        mkfile.write(projectname + ': ' + projectname + '.in Makefile\n')
        mkfile.write('	$(do_substitution) < $(srcdir)/' + projectname + '.in > ' + projectname + '\n')
        mkfile.write('	chmod +x ' + projectname)

    with open(projectname + '/src/' + modulename + '/Makefile.am', 'w') as mkfile:
        mkfile.write(modulename + '_PYTHON = \ \n')
        mkfile.write('	' + modulename + '.py \ \n')
        mkfile.write('	__init__.py \n\n')
        mkfile.write(modulename + 'dir = $(pythondir)/' + modulename + '\n')




if __name__ == "__main__":
  
    projectname = str(sys.argv[1])
    modulename = str(sys.argv[2])
    mkdirs(projectname, modulename)
    writetofiles(projectname, modulename)
    os.system('cd ' + projectname + '&& sudo aclocal')
    os.system('cd ' + projectname + '&& sudo autoconf')
    os.system('cd ' + projectname + '&& sudo automake --add-missing')
    os.system('cd ' + projectname + '&& sudo ./configure')
    os.system('cd ' + projectname + '&& sudo make')
    os.system('cd ' + projectname + '&& sudo make install')
    os.system('cd ' + projectname + '&& sudo make dist')

