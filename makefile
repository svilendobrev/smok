# svilendobrev.com

TARGET ?= /usr/src/python3.2-3.2/


#configure , patch , pgen
now: pgen
all: now
	$(MAKE) -C $(TARGET) GRAMMAR_INPUT=$(GRAMMAR_INPUT)

pgen: patch	grammar #make pgen then make grammar
	rm -f $(TARGET)/Parser/pgen.stamp
	export genUSELOCALE=1; $(MAKE) -C $(TARGET) GRAMMAR_INPUT=$(GRAMMAR_INPUT)  Parser/pgen.stamp

configure=$(TARGET)/Makefile

patch: patch.ok
patch.ok: $(configure)
	- cat diffs/*.diff | patch -p 1 -d $(TARGET)
	touch $@


BGPY = PYTHONPATH=~/src/bin/util/ python3 bg.py

$(configure):
	cd $(TARGET); ./configure

orgGRAMMAR_INPUT= $(TARGET)/Grammar/Grammar
GRAMMAR_INPUT   = $(TARGET)/Grammar/bgGrammar

grammar: $(GRAMMAR_INPUT)
$(GRAMMAR_INPUT): $(orgGRAMMAR_INPUT) bg.py
	$(BGPY)  --grammar < $< > $@


PGEN = Parser/pgen
GRAMMAR_H= Include/graminit.h
GRAMMAR_C= Python/graminit.c

grammargen:
	$(PGEN) $(GRAMMAR_INPUT) $(GRAMMAR_H) $(GRAMMAR_C)

vim: bg3py.vim
bg3py.vim: bg.py
	$(BGPY) --vim < /usr/share/vim/vim73/syntax/python.vim > $@
	cat $@

diff:
	diff -Naur $(TARGET)/$(DIFF) ./$(DIFF)

opit:
	$(TARGET)/python opit.py
# vim:ts=4:sw=4:noexpandtab
