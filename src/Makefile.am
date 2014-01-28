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