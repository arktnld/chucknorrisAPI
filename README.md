# chucknorrisAPI
Simple API to show jokes about Chuck Norris.

## TL;DR

```bash
# enter the project
cd chucknorrisAPI

# install requirements
pip install -r requirements.txt

# run the server
flask run

# query the API on linux
http get localhost:5000/api/jokes/random

# query the API on windows powershell
Invoke-RestMethod -Uri localhost:5000/api/jokes/random
```
## GET

### Random Joke
```bash
http get localhost:5000/api/jokes/random
```

#### Output:
```bash
{
    "categories": [],
    "id": "_fM8fGOdT5iH2Eibtgu4Vg",
    "joke": "Schindlers List is based on one of Chuck Norris wet dreams"
}
```
### List of Categories
```bash
http get 127.0.0.1:5000/api/jokes/categories
```

#### Output:
```bash
[
    "animal",
    "career",
    "celebrity",
    "dev",
    "explicit",
    "fashion",
    "food",
    "history",
    "money",
    "movie",
    "music",
    "political",
    "religion",
    "science",
    "sport",
    "travel"
]
```

## POST

### Random Joke by Categories
```bash
http post localhost:5000/api/jokes/<category>
```

#### Output:
```bash
{
    "categories": [
        "dev"
    ],
    "id": "s4ymkruzsks7loog8eqsya",
    "joke": "Chuck Norris hosting is 101% uptime guaranteed."
}
```
### Search Joke With Limit

Search have two parameters:
- search=*{string}*
- limit=*{number}*
```bash
http --form post localhost:5000/api/jokes/filter search=test limit=3
```

#### Output:
```bash
{
    "result": [
        {
            "categories": [
                "explicit"
            ],
            "id": "RX3L0rCGRc6pSCzghxzL3g",
            "joke": "Horses have long faces because they keep challenging Chuck Norris to \"whos got the biggest dick\" contests."
        },
        {
            "categories": [
                "dev"
            ],
            "id": "7ver3y48qqsfktpelir7ua",
            "joke": "Don't worry about tests, Chuck Norris's test cases cover your code too."
        },
        {
            "categories": [
                "explicit"
            ],
            "id": "br0nodo6sl2q1u_i2s6uja",
            "joke": "For some, the left testicle is larger than the right one. For Chuck Norris, each testicle is larger than the other one."
        }
    ],
    "total": "3"
}
```
### Joke by ID
```bash
http post 127.0.0.1:5000/api/jokes/id/lx5mMleKQ_OjYAN6ZU3BNw
```

#### Output:
```bash
{
    "categories": [],
    "id": "lx5mMleKQ_OjYAN6ZU3BNw",
    "joke": "God offered Chuck Norris the gift to fly, which he swiftly declined for super strength roundhouse ability."
}
```
## TODO

>If you spell Chuck Norris in Scrabble, you win. Forever.

