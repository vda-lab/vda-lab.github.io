---
layout: post
title:  "Projecting a map in clojure"
date:   2020-03-28
author: Jan Aerts
categories: main
tags:
- clojure
- vega
---
This took me a while to figure out, but finally nailed it using the example shown in the scicloj COVIC-19 hackathon screencast at [https://www.youtube.com/watch?v=-441SPx8lTo](https://www.youtube.com/watch?v=-441SPx8lTo)... So this post is just a piece of external memory.

Although vega is very useful for creating data visualisations, you'll almost always need data preprocessing before you can actually load the data in vega. There are many options for this: you can do that in separate scripts, or create vega plots within a python notebook for example.

As I still find clojure conceptually to best way to work with data, I'd thought I'd try things out using the [`oz` library](https://github.com/metasoarous/oz). After all, a vega specification looks a lot like a clojure data structure:

The vega specification:
```json
{
  "data": {"values": [{"x": 1, "y": 5}, {"x": 2, "y": 8}]},
  "mark": "circle",
  "encoding": {
    "x": {"field": "x", "type": "quantitative"},
    "y": {"field": "y", "type": "quantitative"},
    "color": {"value": "red"}
  }
}
```

A corresponding clojure data structure:
```clojure
{
  :data: {:values: [{:x 1 :y 5}, {:x 2 :y 8}]}
  :mark "circle"
  :encoding {
    :x {:field "x" :type "quantitative"}
    :y {:field "y" :type "quantitative"}
    :color {:value "red"}
  }
}
```

One of the problems that I encountered is that vega needs a separate data structure for each point that will be plotted. So for example:

```clojure
[{:date1 "6",
  :date2 "13",
  :date3 "0",
  :name "country 1",
  :part-of "continent 1",
  :kind "country",
  :date4 "2"}
 {:date1 "2",
  :date2 "3",
  :date3 "5",
  :name "country 2",
  :part-of "continent 1",
  :kind "country",
  :date4 "2"}]
```

(i.e. 2 records) needs to be converted into something like this:

```clojure
[{:date "date1" :nr_of_cases 6 :place "country 1"},
 {:date "date2" :nr_of_cases 13 :place "country 1"},
 {:date "date3" :nr_of_cases 0 :place "country 1"},
 {:date "date4" :nr_of_cases 2 :place "country 1"},
 {:date "date1" :nr_of_cases 2 :place "country 2"},
 {:date "date2" :nr_of_cases 3 :place "country 2"},
 {:date "date3" :nr_of_cases 5 :place "country 2"},
 {:date "date4" :nr_of_cases 2 :place "country 2"}]
```
(i.e. 8 records).

Suppose that your initial data is stored in the variable `data`:
```clojure
(def data
  [{:date1 "6",
    :date2 "13",
    :date3 "0",
    :name "country 1",
    :part-of "continent 1",
    :kind "country",
    :date4 "2"}
   {:date1 "2",
    :date2 "3",
    :date3 "5",
    :name "country 2",
    :part-of "continent 1",
    :kind "country",
    :date4 "2"}])
```

To transform the data, we run
```clojure
(->> data
  (reduce (fn [acc m]
            (apply conj acc
              (map (fn [[d n]] {:date d :cases n :place (:name m)})
                   (dissoc m :name :state :kind :part-of))))
    []))
```

Now how does this work? Let's work from the inside-out, replacing `m` with `(first data)` because we'll loop over `data` eventually:
```clojure
(dissoc (first data) :name :state :kind :part-of)
```
removes these particular keys from the initial map. The result:
```clojure
{:date3 "0", :date2 "13", :date4 "2", :date1 "6"}
```

Next, we convert this map into a map with `date` and `cases`:
```clojure
(map (fn [[k v]] {:date (str k) :cases v})
     {:date3 "0", :date2 "13", :date4 "2", :date1 "6"})
```
This code takes the map we had, and goes over it by each key-value pair to create the following:
```clojure
({:date ":date3", :cases "0"}
 {:date ":date2", :cases "13"}
 {:date ":date4", :cases "2"}
 {:date ":date1", :cases "6"})
```

The `apply conj acc` (for "accumulator") puts this list into a vector. As we're only looking at a single example here, we'll use `[]` instead of the accumulator.
```clojure
(apply conj [] (map (fn [[k v]] {:date (str k) :cases v})
     {:date3 "0", :date2 "13", :date4 "2", :date1 "6"}))
```
gives:
```clojure
[{:date ":date3", :cases "0"}
 {:date ":date2", :cases "13"}
 {:date ":date4", :cases "2"}
 {:date ":date1", :cases "6"}]
```

Finally, we want to do this for all the maps with a `reduce`:
```clojure
(reduce (fn [acc m]
          (apply conj acc
            (map (fn [[d n]] {:date d :cases n :place (:name m)})
                 (dissoc m :name :state :kind :part-of))))
   [] data)
```
which gives us the final
```clojure
[{:date :date1, :place "country 1", :cases "6"}
 {:date :date2, :place "country 1", :cases "13"}
 {:date :date3, :place "country 1", :cases "0"}
 {:date :date4, :place "country 1", :cases "2"}
 {:date :date1, :place "country 2", :cases "2"}
 {:date :date2, :place "country 2", :cases "3"}
 {:date :date3, :place "country 2", :cases "5"}
 {:date :date4, :place "country 2", :cases "2"}]
```

Success...
