#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM match"
    cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM player"
    cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    query = "SELECT count(*) as num FROM player"
    cursor.execute(query)
    result = cursor.fetchone()
    db.close()
    return result[0]


def registerPlayer(p_name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    db = connect()
    cursor = db.cursor()
    query = "INSERT into player (player_name) VALUES (%s)"
    cursor.execute(query, (p_name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    query = "SELECT p.player_id, p.player_name, count(m.match_id) as matches_played, count(m.winner) as matches_won"
            "from player p, match m"
            "where p.player_id = match.winner group by p.player_id order by matches_won desc"
    cursor.execute(query)
    r = cursor.fetchall()
    db.close()
    return r


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cursor = db.cursor()
    query = "INSERT into match (match_id, winner, loser) values (default, %s, %s)"
    cursor.execute(query, (winner, loser,))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    arr = []

    position = playerStandings()

    for i in range(0, len(position), 2):

        if len(position) % 2 == 0:

            p_id1 = position[i][0]
            p_name1 = position[i][1]
            p_id2 = position[i+1][0]
            p_name2 = position[i+1][1]

            pair = (p_id1, p_name1, p_id2, p_name2)

            arr.append(pair)

    return arr
