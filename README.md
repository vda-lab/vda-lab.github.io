I0U19A - Management of Large Omics Datasets
===========================================
This repository holds slides and exercises for the course I0U19A of Master of Bioinformatics at KU Leuven, Belgium.

Lecturer: Jan Aerts
Teaching Assistants: Toni Verbeiren, Ryo Sakai, Raf Winand, Thomas Moerman

To convert markdown files to html:
  `pandoc -f markdown -t html my_file.md > my_file.html`

For new presentations (see https://github.com/hakimel/reveal.js#installation):

* in lectures folder: `git clone https://github.com/hakimel/reveal.js.git`
* `mv reveal.js my_new_presentation`
* `cd my_new_presentation`
* `npm install`
* `grunt serve`
* create new file index.md
* `pandoc -f markdown -t revealjs index.md > index.html`
