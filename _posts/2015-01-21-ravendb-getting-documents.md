---
layout: post
title:  "RavenDB - Getting documents"
date:   2015-01-21 08:57
author: Raf Winand
categories: main
tags:
- ravendb
- nosql
- python
---
With ravendb-py you can't load all documents or documents of a certain type, you can only select them through the document id or through an index. As you may not be able to create an index or have the document ids at hand, it would be useful if you could use another function of the HTTP API. The following python code will retrieve all objects that have a key that starts with a given string.

This block has to be added to *loader.py*:

{% highlight python %}
def loadAll(self, startsWith, exclude = '', matches = '', start = 0, pageSize = 25, metadata = "false"):
        headers = {"Content-Type": "application/json", "Accept": "text/plain"}
        request = requests.get(
            '{0}/databases/{1}/docs?startsWith={2}&pageSize={3}&metadata-only={4}&start={5}&exclude={6}&matches={7}'.format(
                self._client.url,
                self._client.database,
                startsWith,
                pageSize,
                metadata,
                start,
                exclude,
                matches
            ),
            headers=headers
        )

        if request.status_code == 200:
            results = []

            for value in request.json():
                results.append(b.buncher(value).bunch())

            return results
        else:
            raise Exception(
                'Error getting document Http :{0}'.format(
                    request.status_code
                )
            )
{% endhighlight %}

To call this function, the following code has to be added to *ravendb.py*:

{% highlight python %}
def loadAll(self, startsWith, **kwargs):
  return self.queries.loadAll(startsWith, **kwargs)
{% endhighlight %}

And this code to *queries.py*:

{% highlight python %}
def loadAll(self, startsWith, **kwargs):
  return l.loader(self._client).loadAll(startsWith, **kwargs)
{% endhighlight %}

Now, just run the setup.py that was included with the original ravendb-py and install the module. Then, to use the code, first you have to create a session:

{% highlight python %}
from ravendb import *
client = store(url='http://my_database.org:8080', database='my_database')
session = client.createSession()
{% endhighlight %}

And then you can query the data with the following line:

{% highlight python %}
employees = session.loadAll("Employees")
{% endhighlight %}

This will return an array with all documents that have a key that starts with *Employees*.

As could be seen from the first block of code, there are several arguments that can be passed to this function. I will go over all of them and explain why they can be useful.

1. **startsWith:** key prefix for which the documents should be returned and this is the only value that is required. Keep in mind that when using e.g. "Employees", this will return documents with keys that start with "Employees" as well as documents with a key called "EmployeesOrders".
1. **pageSize:** this specifies how many results should be returned. By default Ravendb only returns 25 results without giving you any notice that these are not all results in case there are more than 25. You can fill in almost any number here but Ravendb will only return up to 1024 results anyway, even if you specify a higher number here. Default = 25
1. **metadata-only:** gives you the option of only returning the metadata for the requested documents. Default = False
1. **start:** specifies how many results should be skipped before returning the documents. This way you can get more documents if you are over the 1024 limit by first querying 1024 documents and then specifying start=1024 which will give you results 1025-2048. Default = 0
1. **exclude:** pipe (\| or %7C) separated values that specify which characters should not be matched in the document keys after the given prefix. You can also use '?' for any single character or '*' for any character. If you would want all Employees documents but none that start with a 1, you can exclude "1*". Default = ""
1. **matches:** pipe (\| or %7C) separated values that specify which characters should be matched in the document keys after the given prefix. You can also use '?' for any single character or '*' for any character. If you would want all Employees documents but not the EmployeesOrders documents, you can match the "/" in the document id by matching "%2F*". This way, you will only get keys that start with "Employees/" which will only be Employees documents. Default = ""
