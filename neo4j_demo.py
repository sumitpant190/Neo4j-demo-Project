from neo4j import GraphDatabase

class Neo4jDemo:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self):
        self.driver.close()
        
    def add_people(self, names):
        query = "CREATE (p:Person {name: $name})"
        with self.driver.session() as session:
            for name in names:
                session.run(query, name=name)
            
    def add_movies(self, movies):
        query = "CREATE (m:Movie {title: $title, year: $year})"
        with self.driver.session() as session:
            for title,year in movies:
                session.run(query, title=title, year=year)
                
    def add_genres(self, genres):
        query = "CREATE (g:Genre {name: $name})"
        with self.driver.session() as session:
            for genre in genres:
                session.run(query,name=genre)
                
    def add_companies(self, companies):
        query = "CREATE (c:Company {name: $name})"
        with self.driver.session() as session:
            for company in companies:
                session.run(query, name=company)
                
    
    # create relationships                
    
    #creating acting relationship
    def create_acting_relationship(self, actor_movie_pairs):
        query = """
        MATCH (p:Person {name: $actor_name})
        MATCH (m:Movie {title: $movie_title})
        CREATE (p)-[:ACTED_IN {role: $role}]->(m)
        """
        with self.driver.session() as session:
            for actor_name, movie_title, role in actor_movie_pairs:
                session.run(query, actor_name=actor_name, movie_title=movie_title, role=role)
          
    #creating movie genre relationship      
    def create_genre_relationships(self, movie_genre_pairs):
        query = """
        MATCH (m:Movie {title: $movie})
        MATCH (g:Genre {name: $genre})
        CREATE (m)-[:BELONGS_TO]->(g)
        """
        with self.driver.session() as session:
            for movie, genre in movie_genre_pairs:
                session.run(query,movie=movie,genre=genre)
                
    #creating production company relationships
    def create_company_relationships(self,movie_company_pairs):
       query = """
       MATCH (m:Movie {title: $movie})
       MATCH (c:Company {name: $company})
       CREATE (m)-[:PRODUCED_BY]->(c)
       """
       with self.driver.session() as session:
            for movie,company in movie_company_pairs:
                session.run(query,movie=movie,company=company)
                
   # creating movie-director relationships
    def add_directors(self,movie_director_pairs):
        query = """
        MATCH (d:Person {name:$director})
        MATCH (m:Movie {title: $movie})
        CREATE (d)-[:DIRECTED]->(m)
        """   
        with self.driver.session() as session:
            for director,movie in movie_director_pairs:
                session.run(query,director=director ,movie=movie)
            
   
    def find_acted_in(self, person_name):
        query = """
        MATCH (p:Person {name: $person_name})-[:ACTED_IN]->(m:Movie)
        RETURN m.title AS title, m.year AS year
        """        
        
        with self.driver.session() as session:
            result = session.run(query, person_name=person_name)
            return [(record["title"], record["year"]) for record in result]