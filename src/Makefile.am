<<<<<<< HEAD
SUBDIRS = plot

bin_SCRIPTS = plotting
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = plotting.in

do_substitution = sed -e "s,[@]pythondir[@],$(pythondir),g"\ 
        -e "s,[@]PACKAGE[@],$(PACKAGE),g" \ 
        -e "s,[@]VERSION[@],$(VERSION),g" 

plotting: plotting.in Makefile
        $(do_substitution) < $(srcdir)/plotting.in > plotting
        chmod +x plotting
=======
SUBDIRS = make

bin_SCRIPTS = make-dirs
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = make-dirs.in

do_substitution = sed -e "s,[@]pythondir[@],$(pythondir),g"\ 
	-e "s,[@]PACKAGE[@],$(PACKAGE),g" \ 
	-e "s,[@]VERSION[@],$(VERSION),g" 

make-dirs: make-dirs.in Makefile
	$(do_substitution) < $(srcdir)/make-dirs.in > make-dirs
	chmod +x make-dirs
>>>>>>> b012543cf0f93baf4f3d170cc7f7f4fcde842adc
