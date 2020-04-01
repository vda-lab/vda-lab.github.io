---
layout: post
title:  "How to run an online exercise session"
date:   2020-04-01
author: Jan Aerts
categories: main
tags:
- teaching
- covid19
- jitsi
---
Not being allowed to teach face-to-face at university in these COVID-19 times, we are resorting to online tools like Google Hangouts, Zoom, Blackboard Collaborate and others. Each of these has their pros and cons, but I don't intend this post to be a full review of these different tools. Let's just mention that they're not an ideal fit to what we want.

## Online exercise sessions != online lectures
Running exercise sessions instead of regular teaching adds additional constraints on the type of tool that we can use. In a normal face-to-face setting, students will all work on their own while the teachings assistants and I walk around. Although students will typically raise their hands if they are stuck with an exercise, we have quick glances at their screens to see how they're coping as some are more active in asking questions than others. When someone is stuck, we'll look deeper into what they're doing and provide one-on-one feedback.

### Specific requirements
Given the above, we have some additional requirements for teleconferencing tools:
- We should be able to **see everyone's screen**. (Most teleconferencing tools do not allow everyone sharing their screen simultaneously.)
- We should be able to **speak with one or two students separately**. (In most teleconferencing tools, whenever you want to say something goes to _all_ participants.)
- **Students should be able to catch our attention**. (In most teleconferencing tools you can only do that by either starting to talk or chatting.)
- This should work for our group of 30-40 students.

## A possible setup and workflow
After some very brief testing, we have come up with a possible workflow. The tools that we will use:

<img src="{{ site.baseurl }}/assets/jitsi.png" width="200px"/>

- [jitsi](http://jitsi.org): a multi-platform open source video conferencing tool (which was recommended by a student)
- [Google sheets](http://sheets.google.com)

#### Why jitsi?
- It allows for **everyone to share their screen at once**, so that we can "look over the shoulder" of our students as they are working, just like we'd do during an in-person session.
- The procedure to **connect to a meeting is very lightweight**, which is necessary in the workflow that I'll explain below.
- As it's open source, it can if necessary be installed locally on a university server so that we have complete control.

This is what jitsi looks like:

<img src="{{ site.baseurl }}/assets/jitsi-screenshot.png" width="400" />

### Preparatory work
- Get myself a good internet connection...
- Create a **google sheet to track progress of all students across the exercises**, and share it with all students. One row per student, one column per exercise. I set auto-formatting on all cells so that they get a background colour when something is put into the cell. As students are going through the exercises, they should indicate the finished exercises as they complete them. This makes it possible to identify who is lagging behind. Towards the end of the session, you hope the sheet to look like this:

![vega progress]({{ site.baseurl }}/assets/vega-progress.png)

### During the session itself

Here's the overview:

![jitsi workflow]({{ site.baseurl }}/assets/jitsi-workflow.png)

- The teacher **starts a general jitsi meeting** by sharing a URL with the students like this: https://meet.jit.si/FashionableRecruitsMobilizeHalf. To start yours, just go to http://meet.jit.si to get an automatically generated URL, or just append a quite-specific string to the main URL itself. A nice consequence of how it works, is that you can re-use the same URL for every session of a given course.
- Each member of the teaching team creates an **additional separate jitsi meeting for one-on-one discussions** with the students. Make sure to mute your sound in that one.
- I also **connect with an ipad** that will serve as my monitoring device for who raises their hand, etc. Sound and video switched off, and a _headphone plugged into the ipad_ so that it's silent as well.
- Each **student connects** to the meeting, and should:
  - set their **display name** (by clicking on the 3 dots in the bottom right, then on `Settings`, and `Profile`; see the screenshot above)
  - **share their screen** (by clicking on the display icon in the bottom left)
- The teacher **mutes everyone**, including the teaching team. **Sound and video in the one-on-one meeting can now be enabled**.
- Each student opens the **google spreadsheet** that we created above.
- Students start working on the exercises, and indicate in the google spreadsheet every time they finished an exercise.
- If the teaching team sees that a **student lags a bit behind** based on the google spreadsheet, they reach out to the student in the chat window.
- If a student has a question:
  - they **raise their hand** using the hand icon in the bottom right.
  - the teaching team reaches out to the student and **tries to answer the question in chat**
  - if chat is not enough:
    - the teacher **invites the student to the separate one-on-one meeting room**
    - all issues are resolved and the student is able to work further
    - the **student leaves the one-on-one meeting room** (or the teacher removes them)
    - the teacher can continue monitoring the main meeting room

## What we don't know yet
- What will the audio and video quality be for a large group?
- Is the fact that anyone can connect (initially without password) an issue?
