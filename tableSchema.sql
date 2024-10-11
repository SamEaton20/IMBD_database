CREATE TABLE title_basics (
    tconst VARCHAR(20) PRIMARY KEY,
    titleType VARCHAR(50),
    primaryTitle VARCHAR(500),    
    startYear INTEGER,
    runtimeMinutes INTEGER, 
    Documentary BOOLEAN, 
	Drama BOOLEAN, 
	Mystery BOOLEAN, 
	Romance BOOLEAN, 
	Adventure BOOLEAN, 
	War BOOLEAN,
    Western BOOLEAN, 
	Musical BOOLEAN, 
	Comedy BOOLEAN, 
	Thriller BOOLEAN, 
	Crime BOOLEAN, 
	FilmNoir BOOLEAN,
    History BOOLEAN, 
	Biography BOOLEAN, 
	Fantasy BOOLEAN, 
	Action BOOLEAN, 
	Sport BOOLEAN, 
	Family BOOLEAN,
    Music BOOLEAN, 
	Horror BOOLEAN, 
	Animation BOOLEAN, 
	SciFi BOOLEAN, 
	News BOOLEAN, 
	TalkShow BOOLEAN,
    RealityTV BOOLEAN, 
	GameShow BOOLEAN, 
	Adult BOOLEAN 
);


CREATE TABLE title_ratings (
    tconst VARCHAR(20) PRIMARY KEY,
    averageRating FLOAT,
    numVotes INTEGER,
    FOREIGN KEY (tconst) REFERENCES title_basics(tconst) 
);


DROP TABLE IF EXISTS title_ratings CASCADE;


DROP TABLE IF EXISTS title_basics CASCADE;


SELECT * FROM title_basics LIMIT 10;