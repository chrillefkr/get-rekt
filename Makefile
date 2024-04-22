CFLAGS=-O2 -pipe -s
CC=gcc
prefix = /usr
exec_prefix = $(prefix)
sbindir = $(exec_prefix)/sbin
INSTALL=install
DESTDIR=

get-rekt: main.c
	$(CC) $(CFLAGS) main.c -o get-rekt

.PHONY: install
install: get-rekt
	mkdir -p $(DESTDIR)$(sbindir)
	$(INSTALL) get-rekt $(DESTDIR)$(sbindir)/get-rekt
