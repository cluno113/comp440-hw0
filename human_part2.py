"""
Part 2: the best movie.

    uv run python human_part2.py

Write your rule on the `**My rule:**` line of WRITEUP.md. Print the top 10 movies (id, title,
ratings count, mean rating) under it.
"""

from load_data import load_all


def top10_my_rule(ratings, ratings_df, movies, movies_df):
    print("== My rule ==")
    # Movies with the a rating higher than 4.0 and top 10 movies with the highest ratings
    best_movies = ratings_df.groupby('movie_id').filter(lambda x: x['rating'].mean() > 4.0)
    best_movies = best_movies.merge(movies_df[['movie_id', 'title']], on='movie_id')
    top_movies = best_movies.groupby(['movie_id', 'title']).agg({'rating': ['mean', 'count']}).sort_values(('rating', 'count'), ascending=False).head(10)
    print("Top 10 best movies by my rule (with a mean rating > 4.0, highest rating count):")
    for (movie_id, title), (mean, count) in top_movies.iterrows():
        print(f"  {movie_id}: {title} - {count} ratings, mean rating: {mean:.2f}") 
   




def human_part2(ratings, ratings_df, movies, movies_df):
    top10_my_rule(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part2(ratings, ratings_df, movies, movies_df)
