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
```



### 문제2.



```sql
SELECT id, name FROM bands;
```



### 문제3.



```sql
SELECT name FROM bands WHERE debut<=2000;
```

