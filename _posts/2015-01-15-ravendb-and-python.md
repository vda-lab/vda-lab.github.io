---
layout: post
title:  "RavenDB and python"
date:   2015-01-15 16:56
author: Raf Winand
categories: main
tags:
- ravendb
- nosql
- python
---
Although RavenDB is designed to be used with C# and HTTP, a Python client also exists. This client is developed by Patrick McEvoy aka '*firegrass*' and can be found at https://github.com/firegrass/ravendb-py. Installation is very straightforward and can be done by downloading the zip file with the source code, unzipping that to a directory and executing the following command: `python setup.py install`.

Working with this client can be a bit tricky as the documentation is minimal and the readme is not always completely correct. So next I will describe the steps that you can take to create a connection and get some data from the server.

First you have to import the ravendb-py module:

```
from ravendb import *
```

This way you can just use the plain *name* instead of typing ravendb.*name*

Next you have to create a connection to the database:

{% highlight python %}
client = store(url='http://my.database.net:8080', database='my_database')
session = client.createSession()
{% endhighlight %}

If you know the documentIDs of the documents that you want to retrieve, you can use the following code. Make sure to pass the documentIDs as an array or otherwise you will get an HTTP error (500). With this code you can use a '/' in the ID but when using indexes, this doesn't work anymore (cfr. infra).

{% highlight python %}
results = session.load(["Employees/1234512345"])
{% endhighlight %}

This will return an array of the retrieved documents and each document is a 'bunch'. Bunch is another python module that provides a dictionary that supports attribute-style access (like JavaScript). For instance you can retrieve the following object by executing the previous code:

{% highlight python %}
Bunch(@metadata={u'Raven-Last-Modified': u'2015-01-14T15:29:55.3827050', u'Raven-Clr-Type': u'My_database.Core.Employees.Employee, My_database.Core', u'Non-Authoritative-Information': False, u'Last-Modified': u'2015-01-14T15:29:55.3827050Z', u'@etag': u'01000000-0000-000B-0000-000000000146', u'Raven-Entity-Name': u'Employees', u'@id': u'Employees/1234512345'}, DoesNotWantEmails=False, Email=u'anon@anon.anon', Feed={}, FeedCounter=0, EmployeesDataId=u'EmployeesData/10528', HasOpenedFeed=False, MailsReceived=[], Paid=False, RegistrationCode=u'XXXXXX2015', RegistrationDate=u'2015-01-13T09:13:13.2143562', Password={u'Salt': u'sfdsfsfd', u'Hash': u'sfsfsfsfsfsf', u'Iterations': 1000})
{% endhighlight %}

If you now want to access a field, e.g. the email address you just type: results[0].Email. This will give you: u'anon@anon.anon'. As you can see there is a *u* prefix when you look at the results in a python interpreter. This just means that the following string is Unicode string. Printing the variable to screen will not display the *u* and comparing the string in python to the same string without the *u* will also yield True. This only happens in python 2.x as in python 3.x every string is assumed to be Unicode while in python 2.x it is assumed to be an 8-bit string.

Another way to get documents is by using the available indexes. The command seems straightforward but this is only true if you use indexes that don't contain a '/'. For instance, the following code will give you a result if you have a index called *documentsByState* and searched for deleted documents.

{% highlight python %}
results = session.query('documentsByState', {
    'deleted': True
})
{% endhighlight %}

If, however, your index contains a '/', like e.g. *Companies/ByCodeAndName*, the client will report an HTTP 500 error. This is because when creating the http request, the '/' still remains there and therefore the server doesn't find the appropriate index. The key here is to replace the '/' with '%2F'. So the following code gives an error:

{% highlight python %}
results = session.query('Companies/ByCodeAndName', {'Name': 'MyCompany'})
{% endhighlight %}

While the following code will give you a result:

{% highlight python %}
results = session.query('Companies%2FByCodeAndName', {'Name': 'MyCompany'})

Bunch(IsStale=False, documents=[Bunch(@metadata={u'Raven-Last-Modified': u'2015-01-14T13:21:04.2097228', u'Raven-Clr-Type': u'My_database.Core.Companies.Company, My_database.Core', u'Non-Authoritative-Information': False, u'Last-Modified': u'2015-01-14T13:21:04.2097228Z', u'@etag': u'01000000-0000-0001-0000-0000000007FD', u'Temp-Index-Score': 3.48490644, u'Raven-Entity-Name': u'Companies', u'@id': u'companies/194'}, Code=u'MYCOMPANY2015', RegisteredUsers=0, MaxUsers=3000, Name=u'MyCompany')])
{% endhighlight %}

As you can see, the returned resultset is a bunch itself. The collected documents are also placed in an array. So if you would want to get the first document you would have to run the code:

{% highlight python %}
first_result = results.documents[0]
{% endhighlight %}

As the python client actually just sends http requests to the server, it is possible to extend the code to allow for more complex or other queries should that be necessary.
