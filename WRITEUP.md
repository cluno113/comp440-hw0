# HW0 writeup

**Name:** Claire Kuno
**Date:** 2026-09-12

Replace every placeholder below with your answer. Every number you give comes from a script in this repo; say which one.

## Part 1. Basic rating statistics

Code: `human_part1.py`. One or two sentences per answer, with the numbers.

**(a) How many ratings, users, and movies are there, and how are ratings distributed across 1–5 stars?**

Number of ratings: 100000
Number of users: 943
Number of movies: 1682
Rating distribution:
  1 stars: 6110
  2 stars: 11370
  3 stars: 27145
  4 stars: 34174
  5 stars: 21201

The code takes ratings data set and counts the number of ratings before sorting them 1-5. 
Then, creates a four loop that displays each star rating and the count attributed to it.

**(b) What is the median number of ratings per user, and how many users have 100 or more ratings?**

Median number of ratings per user: 65.0
Number of users with 100 or more ratings: 364

This groups the ratings by user_id and looks at what users have 100 or more ratings with the median of the how many ratings users make. 

**(c) Which 10 movies have the most ratings?**

Top 10 movies by rating count:
  Star Wars (1977): 583
  Contact (1997): 509
  Fargo (1996): 508
  Return of the Jedi (1983): 507
  Liar Liar (1997): 485
  English Patient, The (1996): 481
  Scream (1996): 478
  Toy Story (1995): 452
  Air Force One (1997): 431
  Independence Day (ID4) (1996): 429

The code joins movies_df with ratings_df by movie_id. Then, groups ratings by title and arranges it to see which 10 movies have the most ratings.

**(d) Among movies with at least 20 ratings, which 10 have the highest mean rating?**

Top 10 movies by mean rating (with at least 20 ratings):
  Close Shave, A (1995): 4.49 (112.0 ratings)
  Schindler's List (1993): 4.47 (298.0 ratings)
  Wrong Trousers, The (1993): 4.47 (118.0 ratings)
  Casablanca (1942): 4.46 (243.0 ratings)
  Wallace & Gromit: The Best of Aardman Animation (1996): 4.45 (67.0 ratings)
  Shawshank Redemption, The (1994): 4.45 (283.0 ratings)
  Rear Window (1954): 4.39 (209.0 ratings)
  Usual Suspects, The (1995): 4.39 (267.0 ratings)
  Star Wars (1977): 4.36 (583.0 ratings)
  12 Angry Men (1957): 4.34 (125.0 ratings)

By filtering ratings_df's movies (grouped by 'movie_id) to see which movies have at least 20 ratings, the code takes the mean rating for each of the top 10 movies and counts the number of ratings for each movie.

**Anything you got stuck on (what you tried, where it broke), or "none":**

I was ready to code, but then my copilot tried it for me. So, I went through what it did and broke it down to do every step of wrangling on a separate line. 

## Part 2. The best movie

Code: `human_part2.py`.

**My rule:** 

Movies with the a rating higher than 4.0 and top 10 movies with the highest ratings.

**One rule I considered and rejected, and why:** 

I considered looking at the highest rated movies, but when I ran the code, I realized that some movies had only 1 rating. One person enjoying a movie doesn't make it the best movie of all time.

**Top 10 under my rule:**

Top 10 best movies by my rule (with a mean rating > 4.0, highest rating count):
  50: Star Wars (1977) - 583.0 ratings, mean rating: 4.36
  100: Fargo (1996) - 508.0 ratings, mean rating: 4.16
  181: Return of the Jedi (1983) - 507.0 ratings, mean rating: 4.01
  174: Raiders of the Lost Ark (1981) - 420.0 ratings, mean rating: 4.25
  127: Godfather, The (1972) - 413.0 ratings, mean rating: 4.28
  56: Pulp Fiction (1994) - 394.0 ratings, mean rating: 4.06
  98: Silence of the Lambs, The (1991) - 390.0 ratings, mean rating: 4.29
  172: Empire Strikes Back, The (1980) - 367.0 ratings, mean rating: 4.20
  313: Titanic (1997) - 350.0 ratings, mean rating: 4.25
  79: Fugitive, The (1993) - 336.0 ratings, mean rating: 4.04

My rule makes a dataframe that filters for movies with a rating higher than 4, then arranges the rating count (number of user ratings) into an ascending order.

**Why my rule, in at most 150 words. Name one thing it gains and one thing it loses:**

My rule makes sense to me because it is considering the popularity of movies and the rating of the popular movies. I looked at the results from part 1 and personally agreed with the results of 'Which 10 movies had the most ratings' and 'Among movies with at least 20 ratings, which have the highest mean rating?'. It made me want to pull from these prompts and create a list that fits better with my movie familiarity. I experimented with looking at what movies had the highest rating, and how many ratings popular movies had. By combining these two aspects, I feel good at the list of 10 I conjured for this portion of the homework.

## Part 3. The most ___ movie

Code: `human_part3.py`.

**My adjective:** 

Warming

**My definition** (one sentence, precise enough that a classmate could code it)**:** 

Movies that are feel good in a comforting way. 

**One definition I considered and rejected, and why:** 

I considered the definition exciting, but that adjective is too subjective and not descriptive enough to capture a movie genre. 

**Top 5 under my definition:**

0                  Star Kid (1997)
1                Casablanca (1942)
2                 Star Wars (1977)
3                   Titanic (1997)
4  Empire Strikes Back, The (1980)

**What your definition captures, what it misses, and where "___-ness" lives in this data — the genre labels, what the crowd did, or the words in the titles. At most 150 words:**

My definition captures movies that weren't made to scare you or feel bad in anyway. I think it brings up lists of movies that are exciting in joy, not in thrill or fear. Warmness lives in this data through the Romance, Children's, and Musical labels and the high ratings make them movies that people enjoy. 

## Part 4. Claude's answers

Claude answers the same three questions in `claude_answers_1_2_3.py`, without seeing your code or your answers.

**Did its numbers for Part 1 match yours? If not, which, and what did you find?**

Yes, they all matched except I didn't calculate the percentages of ratings in each star. 

## Part 5. Comparing the best movie

**Claude's rule:**

— raw mean is misleading with a 20-rating floor, so I used a Bayesian-shrinkage weighted score (IMDb-style) pulling each movie's mean toward the global average by an amount that shrinks as evidence grows. Winner: **Schindler's List (1993)** (mean 4.47 over 298 ratings, weighted score 4.39), edging out **Shawshank Redemption** and **Casablanca**.

**Read what Claude wrote about its rule. Does it anywhere admit the rule was a choice, and that a different rule was possible? Or does it give its answer as simply the answer? Quote the sentence that decides it:**

Claude admits their rule was a choice: "I used a Bayesian-shrinkage weighted score (IMBDb-style) pulling each movie's mean toward the global average by an amount that shrinks as evidence grows". 

**Your Part 2 top 10 and Claude's Part 2 top 10 — not the Part 1(d) lists. Where do they differ, and why?**

I filtered for movies with a rating higher than 4.0 and picked the top 10 with the most number of ratings. Claude used a method that took the mean of each movie's rating. They differ completely in the method that was used to capture a high rating.


**Better for what purpose? Name a situation where your rule is the right one and a situation where Claude's is. At most 150 words. You may conclude yours, its, or neither:**

I believe Claude's method is nice in that it captures movies with even small numbers of very high rating. So, it would be good for a real cinephile. While mine considers popularity in choosing the best movie as I consider more ratings to be a component in deciphering the 'best' movie. 

## Part 6. Comparing the most ___ movie

**Claude's definition:**

Since "warming" isn't a data column, I operationalized it as movies with a warm-leaning genre(Comedy, Romance, Children's, Animation, Musical) and none of the dark genres (Horror, Crime, War, Thriller, Film-Noir), then ranked by mean rating among those with ≥20 ratings. Winner: **The Wrong Trousers (1993)** (mean 4.47, Wallace & Gromit's claymation follow-up), just ahead of **Wallace & Gromit: The Best of Aardman Animation**.

**Is Claude's film in your top 5?**

No, it was not. 

**What Claude's definition sees that yours does not, and the reverse. At most 150 words:**

My part 2 top 10 was under a definition I set for myself. I only included warming-leaning genres (Comedy, Romance, and Musical), unlike Claude which included additional Comedy and Animation genres. I also ranked the mean ratings over 4.0 and picked the top 5 movies with the highest number of ratings.

## Working with Claude

**What you asked Claude for during Parts 1–3** **(debugging and installing only — say what you got stuck on)**

I asked Claude to list the steps I needed to take to accomplish this homework. I also asked it to read errors in my code!

**Something Claude said that you could not verify, and why. Or "none," and how you checked:**

Claude could not verify my definition of 'best movie' and could not show me the structural connections between the datasets I created. This came up when I was trying to merge and join things I created for my failed attempts at 'best warming movies'. 

**What you would do differently next time, in 3–5 sentences:**

I would disable Co-Pilot before I started the activity and think about more creative ways I can measure things like 'best'. I think I was limiting myself to the examples from parts 1 through 3. 

**Where did this assignment slow you down for a reason that was its fault, not yours? Point at the step. Or "nowhere." One or two sentences:**

I slowed down during the wrangling of the data in Parts 1 through 3. It was my fault because it has been a while since I wrote script in Python. 

**Hours spent:** 

5 hours? 

**Anyone who helped you, or "no one":** 

"No one"
