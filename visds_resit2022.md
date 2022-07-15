---
layout: page
title: Data Visualisation in Data Science - instructions August 2022
permalink: visds_resit2022.html
---
## Overview
For the July/August term, we ask you to create designs on a yelp dataset, as well as implement two visuals using svelte. The exercises done during the course will _not_ be part of this exam period. Thirty percent of the grade will be based on the designs; 70% on the implementation.

Please submit your contributions **before August 22**.

**Getting help** - The teaching assistants will be available to support you again. Please **do not wait until the last week before the deadline** to ask them your questions. Any open office moments will be announced on Blackboard/Toledo. Not all teaching assistants are available throughout the entire July/August term. Include all three in your correspondence for the best chance of a timely reply.

- Jelmer Bot: not available until July 25th, and from August 15th
- Jannes Peeters: not available in last 2 weeks of August
- Dries Heylen: varying availability 

## Design
We ask you to go through a diverge and emerge phase for a yelp dataset. Yelp (http://www.yelp.com) is an online directory of businesses and services that includes reviews by customers. The data consists of information on businesses, users, and reviews. You can create sketches for these independently (i.e. businesses), or combined (e.g. businesses vs users); that is up to you.

We refer you to the teaching material (slides and video) on methods to explore design space in the diverge and emerge stages.

### The data
Imagine having tens of thousands of records for each datatype, but we only show one below to give you an idea of the information each holds.

**Businesses**
{% highlight json %}
{
  "business_id": "Pns2l4eNsfO8kk83dixA6A",
  "name": "Abby Rappoport, LAC, CMQ",
  "address": "1616 Chapala St, Ste 2",
  "city": "Santa Barbara",
  "state": "CA",
  "postal_code": "93101",
  "latitude": 34.4266787,
  "longitude": -119.7111968,
  "stars": 5,
  "review_count": 7,
  "is_open": 0,
  "attributes": {
    "ByAppointmentOnly": "True"
  },
  "categories": "Doctors, Traditional Chinese Medicine, Naturopathic/Holistic, Acupuncture, Health & Medical, Nutritionists",
  "hours": null
}
{% endhighlight %}

**Users**
{% highlight json %}
{
  "user_id": "qVc8ODYU5SZjKXVBgXdI7w",
  "name": "Walker",
  "review_count": 585,
  "yelping_since": "2007-01-25 16:47:26",
  "useful": 7217,
  "funny": 1259,
  "cool": 5994,
  "elite": "2007",
  "friends": "NSCy54eWehBJyZdG2iE84w, pe42u7DcCH2QmI81NX-8qA",
  "fans": 267,
  "average_stars": 3.91,
  "compliment_hot": 250,
  "compliment_more": 65,
  "compliment_profile": 55,
  "compliment_cute": 56,
  "compliment_list": 18,
  "compliment_note": 232,
  "compliment_plain": 844,
  "compliment_cool": 467,
  "compliment_funny": 467,
  "compliment_writer": 239,
  "compliment_photos": 180
}
{% endhighlight %}

**Reviews**
{% highlight json %}
{
  "review_id": "KU_O5udG6zpxOg-VcAEodg",
  "user_id": "mh_-eMZ6K5RLWhZyISBhwA",
  "business_id": "XQfwVwDr-v0ZS3_CbbE5Xw",
  "stars": 3,
  "useful": 0,
  "funny": 0,
  "cool": 0,
  "text": "If you decide to eat here, just be aware it is going to take about 2 hours from beginning to end. We have tried it multiple times, because I want to like it! I have been to it's other locations in NJ and never had a bad experience. \n\nThe food is good, but it takes a very long time to come out. The waitstaff is very young, but usually pleasant. We have just had too many experiences where we spent way too long waiting. We usually opt for another diner or restaurant on the weekends, in order to be done quicker.",
  "date": "2018-07-07 22:09:11"
}
{% endhighlight %}

### Expected for the diverge stage
For the diverge phase, we expect 10 to 20 sketches that explore design space. Your collection will be evaluated on diversity, novelty and relevance. Please find a balance between novelty and relevance: even though we want you to not be critical at this stage, don't scribble random things under the pretense of "novelty".

The image below shows an example sketch from one of your colleagues for the energy dataset.

<img src="{{ site.baseurl }}/assets/sketch_example.png" width=400 />

### Expected for the emerge stage
For the emerge phase, we expect 5 to 10 sketches that either combine different sketches, or take certain sketches a step further. Again: refer to the teaching material for inspiration on different ways to combine sketches.

### Specific instructions
As we did in the group session, please:

* put your initials in the top-right corner of each sketch
* number each sketch in the top-left corner
* clearly indicate what each mark means
* for the emerge sketches, indicate which sketch(es) from the diverge (or emerge) phase are combined

## Implementation
For the implementation part, we will use the energy dataset that we used for the exercises during the year. This is to make sure that you have access to the data. There are two designs that you need to implement. Specific instructions as well as the designs are available at [https://datavis-exercises.vercel.app/resit_project](https://datavis-exercises.vercel.app/resit_project). 

You have two choices to obtain these instructions:

1. Update your existing website by following the [Receiving new instructions](https://datavis-exercises.vercel.app/instructions/working_on_exercises) section.
2. Create a fresh website for this term:
    1. Create a new fork of the [exercise repository](https://gitlab.com/vda-lab/datavis_exercises). 
    2. Create a Vercel deployment for your new fork. 
    3. Send us your new Gitlab and Vercel urls per email!!! 

**Do not delay asking for help if you run in to issues at this stage!**

## How to submit
For the **designs**, we want you to submit a single zip-file which contains 2 folders: one called "diverge" with pictures of your diverge sketches, and one called "emerge" with pictures of your emerge sketches. We will create a Toledo/Blackboard assignment where you can upload them.

For the **implementation**, we have created an additional folder in the git repository ("resit_project"), just like we did for the final visualisations in May. Remember that your visualisations have to show up on Vercel to get graded.