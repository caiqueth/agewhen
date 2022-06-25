# Introduction

Python script to retrieve informations from Wikipedia and OMDB (Open Movie Database).
It makes requests in both APIs to get the birthday from someone and a movie release date, by that movie's title.
With those infos, it calculates that person's age by the time the movie was released.

I only made this to mess around with both APIs.

## Setup
First of all, you have to get your own OMDB API key, you can get one here:
https://www.omdbapi.com/apikey.aspx

It's free for 1.000 usages a day (should be enough, right?).

Then:
* `cd` to the project's directory
* `pip install -r requirements.txt`
* `cd` to `src` directory
* Put the OMDB key in the `.env` file where it says YOUR_OMDB_KEY_HERE.
* Just run `python main.py "Person's Name" "Movie Title"`

### Usage

`python main.py "Timothée Chalamet" "Dune"`

Should return:
```
Timothée Chalamet was born in 1995-12-27 and Dune released in 2021-10-22.
By that time, Timothée Chalamet was 25 years old.
```

Have fun.