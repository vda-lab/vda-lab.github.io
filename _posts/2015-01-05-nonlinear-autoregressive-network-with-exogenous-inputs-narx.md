---
layout: post
title:  "Nonlinear autoregressive network with exogenous inputs (NARX)"
date:   2015-01-05 10:02
author: Raf Winand
categories: network
published: false
---
A nonlinear autoregressive network with exogenous inputs (NARX) is a recurrent dynamic network with feedback connections enclosing several layers of the network. This is a kind of neural network that is suited for the analysis of time-series data. While ANN models are usually used to predict values one step in the future NARX models enter the predicted output value back into the model's input in order to predict several steps ahead (= multi-step-ahead) A NARX network is defined as:

```
y(t+1) = f(y(t), y(t-1), ..., y(t-n_y), u(t), u(t-1), ..., u(t-n_u))
```

From this equation you can see that the next value of *y* that you want to predict depends on previous values of (= already predicted outputs of) *y* and an independent, exogenous input *u*.

A NARX network can be schematically represented as:

![NARX](/assets/narx.gif)

* TDL = Tapped delay line
* LW = Layer weight matrix
* IW = Input weight matrix
* b = bias vector

Training of a NARX network can be done in two different ways:

1. **Series-parallel mode (SP) or open loop**: In this case the output is only based on actual input values.
  ![NARX 1](/assets/ugtsnarxfeedback.png)
1. **Parellel mode (P) or closed loop**: In this case the predicted output values are sent back to the input of the model.
  ![NARX 2](/assets/ugtsnarxfeedback_2.png)

When you are training the model, all actual input values are available so the series-parallel mode is used. When training of the model is done the loop can be closed and the network can be used for multi-step-ahead predictions.

An example of a NARX network is included in Matlab and tries to predict the position of a permanent magnet in a magnetic levitation system. In the following graphs, the top graph show the position of the permanent magnet while the bottom one show the voltage applied to the electromagnet.

![dynamic maglev](/assets/dynamic_maglev.gif)

The first step is to load the data:

{% highlight sh %}
load magdata
y = con2seq(y);
u = con2seq(u);
{% endhighlight %}

This will load two 1x4001 matrices containing the voltage (*u*) and position (*y*).

Next the NARX network has to be created:
{% highlight sh %}
d1 = [1:2];
d2 = [1:2];
narx_net = narxnet(d1,d2,10);
narx_net.divideFcn = '';
narx_net.trainParam.min_grad = 1e-10;
[p,Pi,Ai,t] = preparets(narx_net,u,{},y);
{% endhighlight %}

This code does the following:

**narxnet(inputDelays,feedbackDelays,hiddenSizes,trainFcn):**

Create the NARX network with the specified parameters. d1 and d2 are 2 row vectors with d1 as the input delay and d2 as the feedback delay. By default they are 1:2 but the ideal values have to be defined by using nncorr. The number 10 specifies the number of neurons in the hidden layer which has to be set to the optimal small value (H <= (N-1)/3) by trial and error. It is also possible to add a training function but in this case the default 'trainlm' works fine.

**divideFcn:**

Specifies how to divide the data. In this case, dividing the data in a training, validation and test set is not necessary but for other models you can specify either:

* dividerand: Divide the data randomly
* divideblock: Divide the data into contiguous blocks
* divideint: Divide the data using an interleaved selection, i.e. as in dealing a deck of cards
* divideind: Divide the data by index. The indices for the three subsets are defined by the division parameters net.divideParam.trainInd, net.divideParam.valInd and net.divideParam.testInd. The default assignment for these indices is the null array, so you must set the indices when using this option.

Of these, divideblock is the best one using the default percentages (0.7, 0.15, 0.15) in case you want to split the data.

**trainParam.min_grad:**

Defines the minimum performance gradient. As the training reaches a minimum, the gradient will become smaller. When it falls below this threshold the training is stopped.

**[Xs,Xi,Ai,Ts,EWs,shift] = preparets(net,Xnf,Tnf,Tf,EW)**

This prepares the data so that the network can be trained.

* Xs = Shifted inputs (p)
* Xi = Initial input delay states (Pi)
* Ai = Initial layer delay states (Ai)
* Ts = Shifted targets (t)
* EWs = Shifted error weights
* shift = The number of timesteps truncated from the front of X and T in order to properly fill Xi and Ai.

* net = Neural network (narx_net)
* Xnf = Non-feedback inputs (u)
* Tnf = Non-feedback targets ({})
* Tf = Feedback targets (y)
* EW = Error weights (default = {1})

Here you can already see that *y* is an input that is also an output (target). Later on when the network is closed, the output will be connected to the input. The next step is to train the model:

{% highlight sh %}
narx_net = train(narx_net,p,t,Pi);
{% endhighlight %}

After training the model the original data can be simulated and the error between the actual data and the model can be plotted:

{% highlight sh %}
<pre class="lang:default decode:true " >yp = sim(narx_net,p,Pi);
e = cell2mat(yp)-cell2mat(t);
plot(e)
{% endhighlight %}

This will give the following graph:

![Error plot](/assets/error_plot.png)

Because the network was still open when training, the error here is the error on a one-step-ahead prediction. But we want to predict the position many steps ahead so the network has to be closed. This can be done by:

```
narx_net_closed = closeloop(narx_net);
```

It is now possible to use the closed network to predict a number of steps into the future. In this case we will calculate 900 steps. Again you can use the preparets function to prepare the data.

{% highlight sh %}
y1 = y(1700:2600);
u1 = u(1700:2600);
[p1,Pi1,Ai1,t1] = preparets(narx_net_closed,u1,{},y1);
yp1 = narx_net_closed(p1,Pi1,Ai1);
TS = size(t1,2);
plot(1:TS,cell2mat(t1),'b',1:TS,cell2mat(yp1),'r')
{% endhighlight %}

This will now predict 900 steps and plot the predicted positions (blue) together with the original data (red).

![NARX prediction](/assets/narx_prediction.png)

In order for the parallel response (iterated prediction) to be accurate, it is important that the network be trained so that the errors in the series-parallel configuration (one-step-ahead prediction) are very small.
