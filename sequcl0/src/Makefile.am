SUBDIRS = sequ

bin_SCRIPTS = sequcl0
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = sequcl0.in

do_substitution = sed -e "s,[@]pythondir[@],$(pythondir),g"\ 
	-e "s,[@]PACKAGE[@],$(PACKAGE),g" \ 
	-e "s,[@]VERSION[@],$(VERSION),g" 

sequcl0: sequcl0.in Makefile
	$(do_substitution) < $(srcdir)/sequcl0.in > sequcl0
	chmod +x sequcl0