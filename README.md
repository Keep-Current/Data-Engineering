# Keep-Current-Storage - Data Engineering
This module handles the DB and storage of documents info, users, relations between the two and the recommendations

<!-- Badges section here. -->
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fc0eb9354c4742fca2af56a21267532a)](https://app.codacy.com/app/Keep-Current/Data-Engineering?utm_source=github.com&utm_medium=referral&utm_content=Keep-Current/Data-Engineering&utm_campaign=badger)
[![Build Status](https://travis-ci.org/Keep-Current/Data-Engineering.svg?branch=master)](https://travis-ci.org/Keep-Current/Data-Engineering)[![BCH compliance](https://bettercodehub.com/edge/badge/Keep-Current/Data-Engineering?branch=master)](https://bettercodehub.com/)

After studying a topic, keeping current with the news, published papers, advanced technologies and such proved to be a hard work.
One must attend conventions, subscribe to different websites and newsletters, go over different emails, alerts and such while filtering the relevant data out of these sources.

In this project, we aspire to create a platform for students, researchers, professionals and enthusiasts to discover news on relevant topics. The users are encouraged to constantly give a feedback on the suggestions, in order to adapt and personalize future results.

The goal is to create an automated system that scans the web, through a list of trusted sources, classify and categorize the documents it finds, and match them to the different users, according to their interest. It then presents it as a timely summarized digest to the user, whether by email or within a site.

## Who are we?

This project intends to be a shared work of *Vienna Data Science Cafe* Meet-Up members, with the purpose, beside the obvious result, to also be used as a learning platform, while advancing the Natural Language Processing / Machine Learning field by exploring, comparing and hacking different models.

Please feel free to [contribute](CONTRIBUTING.md).

Project board is on [Trello](https://trello.com/b/KmMEPjfT/keep-current) and we use [Slack](https://keep-current.slack.com) as our communication channel. If you're new, you can join using [this link](https://join.slack.com/t/keep-current/shared_invite/enQtMzY4MTA0OTQ0NTAzLTcxY2U5NmIwNmM0NmU2MmMyMWQ0YTIyMTg4MWRjMWUyYmVlNWQxMzU3ZWJlNjM4NzVmNTFhM2FjYjkzZDU3YWM ).

## I want to help

We welcome anyone who would like to join and contribute. We meet regularly every month in Vienna through the Data Science Cafe meetup of the VDSG, show our progress and discuss the next steps.

## Data Engineering

This component exposes API for the other components, to save and retrieve the data they need in a secured way.



## The repository

This repository is for Data engineering.
If you wish to assist in different aspects (Data Engineering / Web development / DevOps), we have divided the project to several additional repositories focusing on these topics:

* The machine-learning engine can be found in our [Main repository](https://github.com/Keep-Current/Keep-Current)
* Web Development & UI/UX experiments can be found in our [App repository](https://github.com/Keep-Current/Keep-Current-App)
* Website crawling and spider tasks are concentrated in our [Web Crawler repository](https://github.com/Keep-Current/Keep-Current-Crawler)
* Devops tasks are all across the project. We are trying to develop this project in a serverless architecture, and currently looking into Docker and Kubernetes as well as different hosting providers and plans. Feel free to join the discussion and provide your input!

[travis-badge-url]: https://travis-ci.org/liadmagen/Keep-Current.svg?branch=master