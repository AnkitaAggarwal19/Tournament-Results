Project Overview --

In this project, we have written a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

We have developed0 a database schema to store the game matches between players. Then we have written a Python module to rank the players and pair them up in matches in a tournament.


Project Description --

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.


Code Templates --

The templates for this project are in the tournament subdirectory of your VM’s /vagrant directory. There are three files:
 tournament.sql, tournament.py, and tournament_test.py.

The template file tournament.sql is where we put the database schema, in the form of SQL create table commands. We created the database.

The template file tournament.py is where we put the code of our module.

Finally, the file tournament_test.py contains unit tests that will test the functions we’ve written in tournament.py. We can run the tests from the command line, using the command python tournament_test.py.


Creating Your Database --

Before we can run the code or create the tables, we need to use the create database command in psql to create the database.

Then we can connect psql to our new database and create the tables from the statements we've written in tournament.sql. We can do this in either of two ways:

    -Paste each statement in to psql.

    -Use the command \i tournament.sql to import the whole file into psql at once.


Functions in tournament.py --

registerPlayer(name)
Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

countPlayers()
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

deletePlayers()
Clear out all the player records from the database.

reportMatch(winner, loser)
Stores the outcome of a single match between two players in the database.

deleteMatches()
Clear out all the match records from the database.

playerStandings()
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

swissPairings()
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.


Steps:

1. Install Vagrant and VirtualBox
2. Clone the fullstack-nanodegree-vm repository
3. Launch the Vagrant VM
4. Write SQL database and table definitions in a file (tournament.sql)
5. Write Python functions filling out a template of an API (tournament.py)
6. Run a test suite to verify your code (tournament_test.py)


