"""
Part 1: basic rating statistics.

    uv run python human_part1.py

Answer the four questions below with your own code, print each answer under its label, and
explain each in one sentence in WRITEUP.md.
"""

from load_data import load_all


def human_part1(ratings, ratings_df, movies, movies_df, users, users_df):
    print("part 1 unimplemented")  # delete this line when you start

    print("== (a) ==")
    # (a) How many ratings, users, and movies are there, and how are ratings distributed across 1-5 stars?
    counts = ratings_df['rating'].value_counts()
    counts = counts.sort_index()
    print(f"Number of ratings: {len(ratings_df)}")
    print(f"Number of users: {len(users_df)}")
    print(f"Number of movies: {len(movies_df)}")
    print("Rating distribution:")
    for rating, count in counts.items():
        print(f"  {rating} stars: {count}")

    print("== (b) ==")
    # (b) What is the median number of ratings per user, and how many users have 100 or more ratings?
    ratings_per_user = ratings_df.groupby('user_id')
    ratings_per_user = ratings_per_user.size()
    median_ratings = ratings_per_user.median()
    users_with_100_or_more = (ratings_per_user >= 100)
    users_with_100_or_more = users_with_100_or_more.sum()

    print(f"Median number of ratings per user: {median_ratings}")
    print(f"Number of users with 100 or more ratings: {users_with_100_or_more}")

    print("== (c) ==")
    # (c) Join ratings to titles. Which 10 movies have the most ratings?
    ratings_with_titles = ratings_df.merge(movies_df[['movie_id', 'title']], on='movie_id')
    top_movies = ratings_with_titles.groupby('title').size().sort_values(ascending=False).head(10)
    print("Top 10 movies by rating count:")
    for movie, count in top_movies.items():
        print(f"  {movie}: {count}")

    print("== (d) ==")
    # (d) Among movies with at least 20 ratings, which 10 have the highest mean rating?
    #     Show title, mean, and count.
    movies_with_20_ratings = ratings_df.groupby('movie_id').filter(lambda x: len(x) >= 20)
    movies_with_20_ratings = movies_with_20_ratings.merge(movies_df[['movie_id', 'title']], on='movie_id')
    top_movies_mean = movies_with_20_ratings.groupby('title').agg({'rating': ['mean', 'count']}).sort_values(('rating', 'mean'), ascending=False).head(10)
    print("Top 10 movies by mean rating (with at least 20 ratings):")
    for movie, (mean, count) in top_movies_mean.iterrows():
        print(f"  {movie}: {mean:.2f} ({count} ratings)")


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part1(ratings, ratings_df, movies, movies_df, users, users_df)
