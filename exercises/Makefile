DOC0=datasets
DOC1=visualization
DOC2=index
DOC3=rdbms
DOC4=data-processing
DOC5=data-processing-ex
DOC6=nosql
DOC7=nosql-ex

TEMPLATE=stylesheets/doc-template.css

all: 
	make $(DOC0).html
	make $(DOC1).html
	make $(DOC2).html
	make $(DOC3).html
	make $(DOC4).html
	make $(DOC5).html
	make $(DOC6).html
	make $(DOC7).html

$(DOC0).html : $(DOC0).md
	pandoc $(DOC0).md -t html5 -o $(DOC0).html  --highlight-style=tango --css $(TEMPLATE) --self-contained

$(DOC1).html : $(DOC1).md
	pandoc $(DOC1).md -t html5 -o $(DOC1).html  --highlight-style=tango --css $(TEMPLATE) --self-contained

$(DOC2).html : $(DOC2).md
	pandoc $(DOC2).md -t html5 -o $(DOC2).html  --highlight-style=tango --css $(TEMPLATE) --self-contained

$(DOC3).html : $(DOC3).md
	pandoc $(DOC3).md -t html5 -o $(DOC3).html  --highlight-style=tango --css $(TEMPLATE) --self-contained	

$(DOC4).html : $(DOC4).md
	pandoc $(DOC4).md -t html5 -o $(DOC4).html  --highlight-style=tango --css $(TEMPLATE) --self-contained	

$(DOC5).html : $(DOC5).md
	pandoc $(DOC5).md -t html5 -o $(DOC5).html  --highlight-style=tango --css $(TEMPLATE) --self-contained	

$(DOC6).html : $(DOC6).md
	pandoc $(DOC6).md -t html5 -o $(DOC6).html  --highlight-style=tango --css $(TEMPLATE) --self-contained	

$(DOC7).html : $(DOC7).md
	pandoc $(DOC7).md -t html5 -o $(DOC7).html  --highlight-style=tango --css $(TEMPLATE) --self-contained	

