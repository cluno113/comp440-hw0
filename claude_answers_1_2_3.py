"""
Claude's answers to the three questions in questions.md.

    uv run python claude_answers_1_2_3.py

Filled in by a Claude that has never seen the student's work. Kept as it was written.
"""

import pandas as pd

from load_data import GENRES, load_all

WARM_GENRES = {"Children's", "Animation", "Musical", "Romance", "Comedy"}
COLD_GENRES = {"Horror", "Crime", "War", "Film-Noir", "Thriller"}


def question_1(ratings_df: pd.DataFrame, movies_df: pd.DataFrame) -> None:
    print("=" * 70)
    print("1(a) Basic counts and the rating distribution")
    print("=" * 70)
    n_ratings = len(ratings_df)
    n_users = ratings_df["user_id"].nunique()
    n_movies = ratings_df["movie_id"].nunique()
    print(f"{n_ratings:,} ratings, {n_users:,} users, {n_movies:,} movies")
    print()
    dist = ratings_df["rating"].value_counts().sort_index()
    for stars, count in dist.items():
        pct = 100 * count / n_ratings
        print(f"  {stars} stars: {count:>6,}  ({pct:4.1f}%)  {'#' * int(pct)}")

    print()
    print("=" * 70)
    print("1(b) Ratings per user")
    print("=" * 70)
    per_user = ratings_df.groupby("user_id").size()
    print(f"Median ratings per user: {per_user.median():.0f}")
    print(f"Mean ratings per user:   {per_user.mean():.1f}")
    n_heavy = (per_user >= 100).sum()
    print(f"Users with >= 100 ratings: {n_heavy:,} of {n_users:,} ({100 * n_heavy / n_users:.1f}%)")

    print()
    print("=" * 70)
    print("1(c) The 10 most-rated movies")
    print("=" * 70)
    counts = ratings_df.groupby("movie_id").size().rename("n_ratings")
    joined = movies_df.set_index("movie_id")[["title"]].join(counts, how="inner")
    most_rated = joined.sort_values("n_ratings", ascending=False).head(10)
    print(most_rated.reset_index(drop=True).to_string(index=False))

    print()
    print("=" * 70)
    print("1(d) Highest mean rating, among movies with >= 20 ratings")
    print("=" * 70)
    stats = ratings_df.groupby("movie_id")["rating"].agg(mean="mean", count="count")
    stats = stats.join(movies_df.set_index("movie_id")["title"])
    qualified = stats[stats["count"] >= 20]
    top_mean = qualified.sort_values("mean", ascending=False).head(10)
    top_mean = top_mean[["title", "mean", "count"]].round({"mean": 3})
    print(top_mean.reset_index(drop=True).to_string(index=False))


def question_2(ratings_df: pd.DataFrame, movies_df: pd.DataFrame) -> None:
    print()
    print("=" * 70)
    print("2. What is the best movie in this dataset?")
    print("=" * 70)
    print("""
"Best" can't just mean highest average rating: with only 20+ ratings required,
a movie with 20 near-unanimous 5s beats a movie with 500 ratings averaging 4.4,
even though the second is far better attested. I use a Bayesian shrinkage
estimate (the same idea as IMDb's old weighted rating): pull each movie's mean
toward the global mean, by an amount that shrinks as its own rating count
grows.

    weighted_score = (m * C + n * R) / (m + n)

where R is the movie's own mean, n its rating count, C the mean rating across
all movies, and m a prior strength (chosen here as the median ratings-per-movie,
so a movie needs a typical amount of evidence before its own mean dominates).
""")
    stats = ratings_df.groupby("movie_id")["rating"].agg(mean="mean", count="count")
    stats = stats.join(movies_df.set_index("movie_id")["title"])

    C = ratings_df["rating"].mean()
    m = ratings_df.groupby("movie_id").size().median()
    stats["weighted_score"] = (m * C + stats["count"] * stats["mean"]) / (m + stats["count"])

    top = stats.sort_values("weighted_score", ascending=False).head(10)
    top = top[["title", "mean", "count", "weighted_score"]].round(3)
    print(f"(global mean C = {C:.3f}, prior strength m = {m:.0f} ratings)\n")
    print(top.reset_index(drop=True).to_string(index=False))

    best = top.iloc[0]
    print(f"\nBest movie: {best['title']}  "
          f"(mean {best['mean']:.2f} over {int(best['count'])} ratings, "
          f"weighted score {best['weighted_score']:.3f})")


def question_3(ratings_df: pd.DataFrame, movies_df: pd.DataFrame) -> None:
    print()
    print("=" * 70)
    print("3. Which movie is the most warming?")
    print("=" * 70)
    print(f"""
"Warming" isn't in the data as a column, so I have to operationalize it.
I treat it as: a movie whose genre mix leans toward comfort/uplift rather
than darkness or menace, *and* that viewers actually responded warmly to
(a high mean rating with a reasonable amount of evidence).

Genres I count as "warm": {sorted(WARM_GENRES)}
Genres I count as "cold" (and exclude a movie for having any of): {sorted(COLD_GENRES)}

Among movies with at least one warm genre, none of the cold genres, and
>= 20 ratings, I rank by mean rating (the same >= 20 threshold used in 1d,
so a couple of oddball high-average, low-count movies don't dominate).
""")
    counts = ratings_df.groupby("movie_id").size().rename("count")
    means = ratings_df.groupby("movie_id")["rating"].mean().rename("mean")

    # movies_df from movies_to_pandas has one boolean column per genre, not a "genres" list.
    genre_cols = [g for g in GENRES if g in movies_df.columns]
    movies_indexed = movies_df.set_index("movie_id")
    warm_hit = movies_indexed[genre_cols].apply(lambda row: any(row[g] for g in WARM_GENRES), axis=1)
    cold_hit = movies_indexed[genre_cols].apply(lambda row: any(row[g] for g in COLD_GENRES), axis=1)

    stats = movies_indexed[["title"]].join(means).join(counts)
    stats = stats[warm_hit & ~cold_hit]
    qualified = stats[stats["count"] >= 20].dropna()

    top = qualified.sort_values("mean", ascending=False).head(10)
    top = top[["title", "mean", "count"]].round({"mean": 3})
    print(top.reset_index(drop=True).to_string(index=False))

    warmest = top.iloc[0]
    print(f"\nMost warming movie: {warmest['title']}  "
          f"(mean {warmest['mean']:.2f} over {int(warmest['count'])} ratings)")


def claude_answers():
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    question_1(ratings_df, movies_df)
    question_2(ratings_df, movies_df)
    question_3(ratings_df, movies_df)


if __name__ == "__main__":
    claude_answers()
