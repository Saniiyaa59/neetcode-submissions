CREATE TABLE humans (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    owner_id INTEGER REFERENCES humans(id),
    name TEXT
);

INSERT INTO humans (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David'),
(5, 'Eve');

INSERT INTO pets (id, owner_id, name) VALUES
(1, 1, 'Whiskers'),
(2, 2, 'Buddy'),
(3, 5, 'Max'),
(4, 5, 'Bella');
-- Do not modify above this line. --

ALTER TABLE humans
RENAME COLUMN name TO human_name;

ALTER TABLE pets 
RENAME COLUMN name TO pet_name;

SELECT h.human_name, p.pet_name
FROM humans h
LEFT JOIN pets p ON h.id = p.owner_id
ORDER BY h.human_name, p.pet_name;



