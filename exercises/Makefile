# themes. blood is dark, smoot font. beige is lighter

DOC0=0.\ BigData\ Course
DOC1=1.\ Visualization

TEMPLATE=stylesheets/doc-template.css

all: 
	make $(DOC0).html
	make $(DOC1).html

$(DOC0).html : $(DOC0).md
	pandoc $(DOC0).md -t html5 -o $(DOC0).html  --highlight-style=tango --css $(TEMPLATE) --self-contained

$(DOC1).html : $(DOC1).md
	pandoc $(DOC1).md -t html5 -o $(DOC1).html  --highlight-style=tango --css $(TEMPLATE) --self-contained

