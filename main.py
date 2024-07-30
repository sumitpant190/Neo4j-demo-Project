from neo4j_demo import Neo4jDemo

def main():
    #create neo4j instance
    neo4j_demo = Neo4jDemo("bolt://localhost:7687", "neo4j", "12345678")

    
    # Create some nodes
    
    # Add nodes
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

    # Create relationships
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

    # Close the connection
    neo4j_demo.close()
    
if __name__ == "__main__":
    main()
    
    