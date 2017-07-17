-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- 'player' and 'match' tables are created.

CREATE TABLE player (
	player_id SERIAL PRIMARY KEY,
	player_name VARCHAR(25) NOT NULL
	);

CREATE TABLE match (
	match_id SERIAL PRIMARY KEY,
	winner INTEGER REFERENCES player (player_id),
	loser INTEGER REFERENCES player (player_id)
	);

-- 'score' view is created.

CREATE OR REPLACE VIEW score AS
	SELECT p.player_id , p.player_name, count(m.match_id) AS player_score
	FROM player AS p LEFT JOIN match AS m
	ON p.player_id = m.winner OR p.player_id = m.loser
GROUP BY p.player_id;
