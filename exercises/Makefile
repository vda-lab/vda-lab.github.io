# themes. blood is dark, smoot font. beige is lighter

DOC0=datasets
DOC1=visualization
DOC2=index

TEMPLATE=stylesheets/doc-template.css

all: 
	make $(DOC0).html
	make $(DOC1).html
	make $(DOC2).html

$(DOC0).html : $(DOC0).md
	pandoc $(DOC0).md -t html5 -o $(DOC0).html  --highlight-style=tango --css $(TEMPLATE) --self-contained

$(DOC1).html : $(DOC1).md
	pandoc $(DOC1).md -t html5 -o $(DOC1).html  --highlight-style=tango --css $(TEMPLATE) --self-contained

$(DOC2).html : $(DOC2).md
	pandoc $(DOC2).md -t html5 -o $(DOC2).html  --highlight-style=tango --css $(TEMPLATE) --self-contained

clean:
	rm $(DOC0).html
	rm $(DOC1).html
	rm $(DOC2).html


