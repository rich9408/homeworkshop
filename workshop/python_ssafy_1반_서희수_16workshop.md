### 문제1. 



```sql
CREATE TABLE bands(
    id INTEGER,
    name TEXT,
    debut INTEGER
);

INSERT INTO bands VALUES('1', 'Queen', 1973);
INSERT INTO bands VALUES('2', 'Coldplay', 1998);
INSERT INTO bands VALUES('3', 'MC', 2001);

ALTER TABLE bands ADD COLUMN members INREGER);

UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;

UPDATE bands SET members=5 WHERE id=3;

DELETE FROM bands WHERE id=2
```





