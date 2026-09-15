"""
Part 3: the most ___ movie.

    uv run python human_part3.py

Pick an adjective. Write it on the `**My adjective:**` line of WRITEUP.md and a one-sentence
definition a classmate could code on the `**My definition:**` line. Print the top 5 movies
under it.
"""

from load_data import load_all


def top5_my_definition(ratings, ratings_df, movies, movies_df):
    print("== My definition ==")
    # Movies that are the most warming according to my definition:
    # movies_df.info()
    warming_movies = movies_df[
        (movies_df["Children's"] == 1) |
        (movies_df["Musical"] == 1) |
        (movies_df["Romance"] == 1)
    ]
    warming_ratings = ratings_df.merge(warming_movies[['movie_id', 'title']], on='movie_id') \
    .groupby(['movie_id', 'title']).agg({'rating': ['mean', 'count']}) \
    .sort_values(('rating', 'mean'), ascending=False)
    warming_ratings = warming_ratings.reset_index()
    print(warming_ratings.head(5)[["title"]])
    
def human_part3(ratings, ratings_df, movies, movies_df):
    top5_my_definition(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part3(ratings, ratings_df, movies, movies_df)
