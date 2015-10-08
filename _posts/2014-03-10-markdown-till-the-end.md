---
layout: post
title:  "Markdown till the end"
date:   2014-03-10 09:47
author: Toni Verbeiren
categories: markdown howto
tags:
- markdown
- howto
---
It's [nothing](/2014/01/proper-syntax-highlighting-in-revealjs-using-pandoc) [new](http://www.data-intuitive.com/2013/06/writing-workflow-markdown-pandoc-latex-and-the-likes/) that I am a big fan of [Markdown](http://daringfireball.net/projects/markdown/) and [Pandoc](http://johnmacfarlane.net/pandoc/) for everything related to writing and publishing. For the last conference paper I wrote, I wanted to go all the way: write exclusively in Markdown and let Pandoc/LaTeX do the conversion and typesetting. I'm not going to show the actual example because the review process is double-blind...

# Body text
Usually, LaTeX style files are provided for sending in journal or conference papers. The traditional approach would be to start from a provided template and use LaTeX syntax to type the text. I did something else. I replaced the *body* (the part between `\begin{document}` and `\end{document}`) of the provided template tex file with the following:

```
$body$
```

This file is now the template, let's call it `template.tex`. We now create a markdown file in which we put some content using Markdown syntax: `paper.md`. The markdown file can be converted into a PDF using the following Pandoc instruction:

```
pandoc paper.md -o paper.pdf --template template.tex
```

That's it! All style information is covered in the template (the provided style file) and the content is provided by the Markdown file. You might have guessed that Pandoc uses `$body$` as a placeholder for pasting the content from the Markdown file (after converting it to LaTeX format).

Well, actually, we're not finished yet. We don't yet have a title, an author, an abstract, references, graphics, ...

# Title, Author, Date
Adding the title, an author and/or the date is similarly easy as the body of the text. Pandoc has since long supported this by means of a special syntax in the beginning of the Markdown file:

{% highlight tex %}
% A title for the paper
% T Verbeiren
% 2/4/2014
{% endhighlight %}

This is automatically converted into variables that can be used in the template as such:

{% highlight tex %}
<pre class="lang:tex decode:true">\title{$title$}
\author{$author$}
\date{$date$}
{% endhighlight %}

Later, in the body of the document a `\maketitle` line should be present in order to print the title.

This is just the basics. Have multiple authors? Check the documentation or the template that is provided by Pandoc itself.

# Abstract
Pandoc does not have a default way of handling abstracts. But since Pandoc v. 1.12.2, YAML blocks can be added to the beginning of a Markdown file and Pandoc knows how to deal with them. This allows for custom parsing of variables like an abstract. In our `paper.md` file, we put the following YAML block:
{% highlight yaml %}
---
abstract: |
  This is the abstract.
  Multiple lines are not problem.
  They are all included.
...
{% endhighlight %}

In the `template.tex` file, the following is sufficient to add the abstract to the title:
{% highlight tex %}
\begin{abstract}
$abstract$
\end{abstract}
{% endhighlight %}

# Citations and References
Pandoc has [support for citations](http://johnmacfarlane.net/pandoc/README.html#citations) in different styles, but unfortunately the one I needed to use was not there. If you find it in [the list of available styles](https://github.com/citation-style-language/styles), use this method. I reverted to using plain old LaTeX syntax in the Markdown file. Pandoc makes sure it passes the LaTeX command along.

In the same vein, I used LaTeX references (`\label{foo}` and `\ref{foo}`) for referring to floating figures.

# Figures
Adding figures is simply a matter of providing the template with the correct snippet. I derived mine from the template that is provided by Pandoc:

{% highlight tex %}
$if(graphics)$
  \usepackage[pdftex]{graphicx}
  \pdfcompresslevel=9
  \makeatletter
  \def\maxwidth{\ifdim\Gin@nat@width&gt;\linewidth\linewidth
    \else\Gin@nat@width\fi}
    \makeatother
    \let\Oldincludegraphics\includegraphics
    \renewcommand{\includegraphics}[1]{\Oldincludegraphics[width=.8\linewidth]{#1}}
$endif$
{% endhighlight %}

Add this to the preamble of the template file and in the Markdown file you can use the usual syntax to refer to a figure:

```
![This is where the caption goes.\label{foo}](foo.png)
```

That's it!

Additional tuning can be done, extra packages can be loaded. Also, by using the YAML code blocks, one can add affiliations, keywords, acknowledgments and other information to the Markdown document that depending on the template is used to generate the PDF/HTML/... output.
