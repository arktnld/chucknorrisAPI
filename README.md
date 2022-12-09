
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

# query on linux
http localhost:5000/api/jokes/random

# query on windows powershell
Invoke-RestMethod -Uri http://localhost:5000/api/jokes/random
```
## GET

### Random Joke
```bash
# Linux
http localhost:5000/api/jokes/random

# Windows
Invoke-RestMethod -Uri http://localhost:5000/api/jokes/random
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
# Linux
http localhost:5000/api/jokes/categories

# Windows
Invoke-RestMethod -Uri http://localhost:5000/api/jokes/categories
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

### Joke by ID
```bash
# Linux
http localhost:5000/api/jokes/id/<id>

# Windows
Invoke-RestMethod -Uri http://localhost:5000/api/jokes/id/<id>

```

#### Output:
```bash
{
    "categories": [],
    "id": "lx5mMleKQ_OjYAN6ZU3BNw",
    "joke": "God offered Chuck Norris the gift to fly, which he swiftly declined for super strength roundhouse ability."
}
```

### Random Joke by Category
```bash
# Linux
http localhost:5000/api/jokes/<category>

# Windows
Invoke-RestMethod -Uri http://localhost:5000/api/jokes/<category>
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

## POST

### Search Joke With Limit

Search have two parameters:
- search=*{string}*
- limit=*{number}*
```bash
# linux
http --form post localhost:5000/api/jokes/filter search=computer limit=3

# windows
Invoke-RestMethod -Method POST -Uri "http://localhost:5000/api/jokes/filter" -Body @{search="computer"; limit="3"} | Format-List
```

#### Output:
```bash
{
    "result": [
        {
            "categories": [],
            "id": "y-b7g8trr96pfmopdplf4g",
            "joke": "Chuck Norris doesn't use a computer because a computer does everything slower than Chuck Norris."
        },
        {
            "categories": [],
            "id": "AN7_hBUjSW-Fnbn-28jaVQ",
            "joke": "When Chuck Norris wants cookies, he crashes open a computer."
        },
        {
            "categories": [],
            "id": "mHaLxKzVRjiBLgE1KhEZ_g",
            "joke": "Chuck Norris can build a computer with Windows 7."
        }
    ],
    "total": "3"
}

```
## TODO

>If you spell Chuck Norris in Scrabble, you win. Forever.

