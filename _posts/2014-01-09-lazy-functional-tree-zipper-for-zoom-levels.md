---
layout: post
title:  "A lazy functional tree zipper for zoom levels"
date:   2014-01-09 18:46:00
author: Toni Verbeiren
categories: spark locustree scala
tags:
- spark
- locustree
- scala
---
*... This must be the best blog post title around ...*

Based on the [Locustree concept](http://saaientist.blogspot.be/2009/04/locustree-searching-genomic-loci.html) by [Jan Aerts](http://homes.esat.kuleuven.be/~bioiuser/person.php?persid=473), I have been working on a tree representation for storing zoom and pan/shift information. This post aims to describe the context, a possible implementation in Scala and its use in visualisation.

Let's assume for a while that we have a large amount of data that can be mapped onto one dimension. One possible use-case is genome data, but all sorts of problems can be rephrased like this. The idea is to represent the data on a screen for visual analysis. In other words, one dimension defines the scale and on top of that we have information: gene expressions, transcription factor binding, amino acids, ...

Please note that a *multi-dimensional* version of the locustree is in the making, stay tuned.

## Locustree
The concept of a locustree stems from the fact that it does not make sense for us to represent the full (remember 1D) dataset on a screen, it is simply too small for that. And even if we would draw all the points, we would not be able to notice any remarkable aspects of our data. In other words, it makes sense for us to look at the data at different zoom levels. At the highest zoom level we see individual data points, the lowest zoom level gives an aggregate idea of the full dataset and different zoom levels can exist in-between. A tree representation with a storage backend as a binary file representation has been created by Jan Aerts (see [here](https://github.com/jandot/locustree) for the source) where every level in the tree represents a zoom level. At all but the largest zoom level, we are interested in aggregate information about the underlying data. In his version, Jan did not have the computational power to render the genome data from the raw data on-the-fly. This meant he had to *pre-process* the data for the different resolutions and store this intermediate data on disk. We are investigating whether it is possible to avoid this intermediate step and immediately start from the raw data.

## Functional programming
Another requirement we have put forward is to employ a [functional approach](http://en.wikipedia.org/wiki/Functional_programming) to programming whenever possible. The primary reason being that [functional programming](http://www.defmacro.org/ramblings/fp.html) (see [here](http://fsharpforfunandprofit.com/posts/ten-reasons-not-to-use-a-functional-programming-language/) for a fun way to learn about FP) leads to immutable data structures which in turn leads to easier distribution and clustering of the algorithms and data. And less headaches while developing...

But wait... if data structures are immutable, how can my program do something useful? Take a look at the Spark examples (they are actually Scala examples) in [a previous post](/2014/01/spark-for-genomic-data). Did you notice that the variables (or actual *values*) do not change? Since these are only pointers to the data anyway, no computational or memory overhead is generated.

## Zippers
It turns out that creating a (locus)tree in a functional way is not all that hard. But in order for the tree to have some awareness of where the *active* node is, is a different story especially when we want to avoid copying memory blocks all the time. The name that is usually used for a functional datastructure that is aware of location is a [zipper](http://en.wikipedia.org/wiki/Zipper_(data_structure)). We're almost there... one more concept needs to be introduced...

## Lazy evaluation
One concept we still need to introduce is [lazy evaluation](http://en.wikipedia.org/wiki/Lazy_evaluation). For us humans, it may as much as: calculate or evaluate only when necessary. The most obvious example is when generating an infinite sequence of numbers or events. In a lazy sense, this is possible. Only when traversing the sequence will there be an evaluation of the entries.

We need something similar for our tree. Only when we access a certain node in the tree do we want to calculate or generate the data for that node.

## Building a simple binary zipper

Pasting the following code in a Scala worksheet does the trick:

{% highlight scala %}
trait Tree
object Empty extends Tree
case class Node(value:Int,left:Tree, right:Tree) extends Tree

trait Location
  case class goRight(value:Int, leftTree:Tree) extends Location
  case class goLeft(value:Int,rightTree:Tree) extends Location

  case class Zipper(tree:Tree, location:List[Location]) {
    def right:Option[Zipper] = tree match {
      case Node(value,left,Empty) =&gt; None
      case Node(value,left,right) =&gt; Some(Zipper(right,goRight(value,left)::location))
    }
    def left:Option[Zipper] = tree match {
      case Node(value,Empty,right) =&gt; None  // oeps!
      case Node(value,left,right) =&gt; Some(Zipper(left,goLeft(value,right)::location))
    }
    def up:Option[Zipper] = location match {
      case List() =&gt; None
      case head::tail =&gt; head match {
      case goLeft(value,rightTree) =&gt; Some(Zipper(Node(value,tree,rightTree),tail))
      case goRight(value,leftTree) =&gt; Some(Zipper(Node(value,leftTree,tree),tail))
    }
  }
}
{% endhighlight %}

This implementation is not perfect, there could be some sealing and other things, but it gets the message across.

The first part takes care of constructing the tree. The location is a way to denote a spot in the tree by means of a path to the spot from the root node (in reverse order). Basically, it can be seen as a trace of the path to the current (active) node.

The zipper is then simply the combination of the current node/tree and the path to it.

Initialisation is can easily be done:

{% highlight scala %}
val test = Node(2,Node(3,Empty,Empty),Node(4,Empty,Node(5,Empty,Empty)))
val zipper = Zipper(test,List())
{% endhighlight %}

The *history* for the root node (and the full tree) is the zero list. Starting from `root` and selecting the left child is easy:

{% highlight scala %}
val goDown = zipper left
{% endhighlight %}

Can you appreciate the coolness of this? In principle, we should write `zipper.left()`, but Scala allows us to write in human readable text...

This is not all, however. The result, given the class definitions above results in an encapsulated result of type `Option[Zipper]`. We could have omitted the `Option` collection, but we would have to carefully handle exceptions like taking the parent of the root node or taking the child of an empty node. `Option` allows us to the deal with these exceptions in a graceful way.

In order to extract the value from an Option, we can simply use the `get` method:

{% highlight scala %}
<pre class="lang:scala decode:true">val goUp = godown.get up
{% endhighlight %}

Again, this yields an `Option[Zipper]` which can be extracted using `get`. Many other possibilities exist to cope with option types, in fact they behave as a [Monad](http://en.wikipedia.org/wiki/Monad). Please [see here](http://danielwestheide.com/blog/2012/12/19/the-neophytes-guide-to-scala-part-5-the-option-type.html) fore more information.

## Conclusion for now
To wrap up: we have introduced the different concepts that are necessary to understand the concept of a *lazy functional tree zipper*. Additionally, we have presented a very simple (binary) implementation in Scala.
