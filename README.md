# Knowledgebot - Chatbot using GloVe

## Description

nlp-server is designed to allow remote access to a set of [GloVe](https://nlp.stanford.edu/projects/glove/) vectors to compare phrase similarity

It allows for a chat system to 'discover' what people are interested in and then 'link' them together (suggest they talk to each other) if they talk about similar topics, e.g. one talks about "auto manufacturers" and another "car producers"

It also allows users to build smart alerts to follow a news story as it evolves, as "Boy discovers X" might be similar enough to a headline for "Child finds X" for the system to intelligently alert the user to headlines similar to the ones he/she already follows

## Demo

1. nlp-server correctly uncovers the structure of the auto market, similarity between Chipotle and Mexican food, and many other scenarios as can be seen in the below conversation

[logo]: images/chatbotdemo.png "KnowledgeBot Demo"

![alt text][logo]

## Installation

1. Run
    ```bash
    ./bootstrap.sh
    ```
1. Run
    ```bash
    source activate spacyenv
    ```
1. Run
    ```bash
    ./startServer.sh
    ```

See also the [related chatbot extension](https://github.com/LRParser/bot-butler)
