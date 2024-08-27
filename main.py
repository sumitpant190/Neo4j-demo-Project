from neo4j_demo import Neo4jDemo, MongoDBDemo

def main():
    # Initialize Neo4j and MongoDB instances
    neo4j_demo = Neo4jDemo("bolt://localhost:7687", "neo4j", "12345678")
    mongo_demo = MongoDBDemo("mongodb://localhost:27017/", "movie_database")

    # Add nodes and relationships in Neo4j
    neo4j_demo.add_people([
        "Sandra Bullock", "Matt Damon", "Lana Wachowski", "Lilly Wachowski",
        "Keanu Reeves", "Carrie-Anne Moss", "Hugo Weaving", "Laurence Fishburne",
        "Christopher Nolan", "Tom Hardy", "Joseph Gordon-Levitt"
    ])

    neo4j_demo.add_movies([
        ("The Matrix", 1999), ("John Wick", 2014),
        ("Inception", 2010), ("The Dark Knight", 2008),
        ("V for Vendetta", 2005), ("Interstellar", 2014)
    ])

    neo4j_demo.add_genres([
        "Action", "Sci-Fi", "Thriller", "Drama", "Adventure"
    ])

    neo4j_demo.add_companies([
        "Warner Bros", "Universal Pictures",
        "Warner Bros Pictures", "Syncopy", "DC Films"
    ])

    neo4j_demo.create_acting_relationship([
        ("Sandra Bullock", "Gravity", "Lead"),
        ("Keanu Reeves", "The Matrix", "Lead"),
        ("Carrie-Anne Moss", "The Matrix", "Lead"),
        ("Hugo Weaving", "The Matrix", "Villain"),
        ("Tom Hardy", "Inception", "Lead"),
        ("Joseph Gordon-Levitt", "Inception", "Supporting")
    ])

    neo4j_demo.create_genre_relationships([
        ("The Matrix", "Sci-Fi"),
        ("John Wick", "Action"),
        ("Inception", "Sci-Fi"),
        ("The Dark Knight", "Action"),
        ("V for Vendetta", "Action"),
        ("Interstellar", "Sci-Fi")
    ])

    neo4j_demo.create_company_relationships([
        ("The Matrix", "Warner Bros"),
        ("John Wick", "Universal Pictures"),
        ("Inception", "Warner Bros"),
        ("The Dark Knight", "Warner Bros"),
        ("V for Vendetta", "Warner Bros"),
        ("Interstellar", "Warner Bros")
    ])

    neo4j_demo.add_directors([
        ("Lana Wachowski", "The Matrix"),
        ("Lilly Wachowski", "The Matrix"),
        ("Christopher Nolan", "Inception"),
        ("Christopher Nolan", "The Dark Knight"),
        ("James McTeigue", "V for Vendetta")
    ])

    # MongoDB: Add detailed movie information
    movie_details = [
        {"title": "The Matrix", "director": "Lana Wachowski", "plot": "A computer hacker learns from mysterious rebels about the true nature of his reality."},
        {"title": "John Wick", "director": "Chad Stahelski", "plot": "An ex-hitman comes out of retirement to track down the gangsters that killed his dog."},
        {"title": "Inception", "director": "Christopher Nolan", "plot": "A thief who steals corporate secrets through the use of dream-sharing technology."},
    ]
    mongo_demo.add_movie_details(movie_details)

    # MongoDB: Retrieve and print a movie's details
    matrix_details = mongo_demo.get_movie_details("The Matrix")
    print("Details of The Matrix:", matrix_details)

    # MongoDB: Add actor biographies
    actor_biographies = [
        {"name": "Keanu Reeves", "biography": "Canadian actor known for his roles in The Matrix and John Wick."},
        {"name": "Sandra Bullock", "biography": "American actress known for her roles in Gravity and The Blind Side."},
    ]
    mongo_demo.add_actor_biographies(actor_biographies)

    # MongoDB: Retrieve and print an actor's biography
    reeves_bio = mongo_demo.get_actor_biography("Keanu Reeves")
    print("Biography of Keanu Reeves:", reeves_bio)

    # Close connections
    neo4j_demo.close()
    mongo_demo.close()

if __name__ == "__main__":
    main()
