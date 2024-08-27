# Neo4j Graph Database Project

## Project Overview

This project demonstrates the use of Neo4j, a graph database, to manage and query a dataset consisting of movies, actors, genres, and production companies. The aim is to showcase how to create and manage nodes and relationships in a graph database and perform various queries using Cypher, Neo4j's query language.

## Features

- **Node Creation**: Add nodes for people (actors), movies, genres, and production companies.
- **Relationship Creation**: Establish relationships such as actors acting in movies, movies belonging to genres, movies produced by companies, and directors directing movies.
- **Data Querying**: Perform queries to retrieve data from the graph database.
- **Data Visualization**: Use Cypher queries to visualize data in the Neo4j Browser.

## Prerequisites

- **Neo4j Database**: Installed and running.
- **Python**: Version 3.x installed.
- **Neo4j Python Driver**: Installed via pip.

## Installation

### Neo4j Installation

1. Download and install Neo4j from [Neo4j's official website](https://neo4j.com/download/).
2. Start Neo4j and configure your database.
3. Note the URI, username, and password for connecting to Neo4j.

### Python Environment Setup

1. Create a virtual environment:
    ```bash
    python -m venv env
    ```
2. Activate the virtual environment:
    - **Windows**: `env\Scripts\activate`
    - **macOS/Linux**: `source env/bin/activate`
3. Install the Neo4j Python driver:
    ```bash
    pip install neo4j
    ```

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/neo4j-graph-database-project.git
    cd neo4j-graph-database-project
    ```

2. **Configure the Script**:
   Edit the `main.py` file to set the correct URI, username, and password for your Neo4j instance.

3. **Run the Script**:
    ```bash
    python main.py
    ```

   This script will:
   - Add nodes for people, movies, genres, and companies.
   - Create relationships between these nodes.
   - Query and print movies acted in by a specific person.

## Code Overview

### `neo4j_demo.py`

Contains the `Neo4jDemo` class with methods to interact with the Neo4j database. Methods include:
- **`add_people`**: Adds nodes representing people.
- **`add_movies`**: Adds nodes representing movies.
- **`add_genres`**: Adds nodes representing genres.
- **`add_companies`**: Adds nodes representing companies.
- **`create_acting_relationship`**: Creates relationships for actors acting in movies.
- **`creating_genre_relationships`**: Creates relationships for movies belonging to genres.
- **`create_company_relationships`**: Creates relationships for movies produced by companies.
- **`add_directors`**: Creates relationships for directors directing movies.
- **`find_acted_in`**: Queries movies acted in by a specific person.

### `main.py`

Contains the script to use the `Neo4jDemo` class to:
- Add data to the database.
- Create relationships.
- Query and display data.

## Cypher Queries for Visualization

To visualize the data in the Neo4j Browser, use the following Cypher queries:

- **View All Nodes and Relationships**:
  ```
  MATCH (n)
  RETURN n
 ``` 

