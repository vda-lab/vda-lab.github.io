slides : slides.md
	pandoc -t revealjs slides.md -o slides.html --slide-level=1 --variable revealjs-url=reveal.js -s --variable transition=fade --no-highlight --variable hlss=zenburn --template "reveal-template.html" --slide-level 1 --variable theme=course

doc : slides.md
	cat slides.md | grep -v -e '- - -' -e '\\ ' | pandoc -t html5 -o slides-doc.html  --highlight-style=tango --css css/doc-template.css --self-contained
