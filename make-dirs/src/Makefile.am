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