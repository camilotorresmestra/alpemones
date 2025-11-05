# alpemones
Workshop 2 from the course on Data Modelling and Design@Uniandes 202502

## The task

Your client wants to create a videogame where magical creatures called "Alpemones" can be captured, trained, and battled against each other. Each Alpemon has a set of attributes such as name, type (e.g., Fire, Water, Grass), level, health points, and special abilities. Players can capture Alpemons, train them to increase their levels and abilities, and engage in battles with other players' Alpemons.

As such, they need a database model that can efficiently store and manage the data related to Alpemons, players, and battles. The database should support operations such as adding new Alpemons, updating their attributes, recording battles and their outcomes, and querying for specific Alpemons based on various criteria.

The database should be designed to handle a large number of players and Alpemons, ensuring scalability and performance. Additionally, the model should consider relationships between players and their Alpemons, as well as the history of battles fought.

## The model

A simple document database model, using MongoDB as engine.

## The code

Is organized in the following files:
- `main.py`: main script to connect and play around with the db. Includes a simple game logic to demonstrate the usage of the database and the different operations that can be performed in the model implemented.
- `queries.py`: module with functions to run the READ operations defined in the project specifications
- `data_generation.py`: module with functions to run the CREATE operations defined in the project specifications. It is basically a mockdata engine. This module uses the Pokeapi to fetch data about alpemons and generate data with some domain logic.
- `updates.py`: module with functions to run the WRITE (UPDATES, DELETIONS) operations defined in the project specifications and used through the game logic.

---

made with ❤️ by Grupo 5 - Modelado y Diseño de Datos - Uniandes 202502