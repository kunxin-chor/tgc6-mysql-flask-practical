# Create database

## Create database
```
create database <name of database>;
```

## Show databases
```
show databases;
```

## Switch active database
```
use library;
```

## Show all tables in database
```
show tables;
```

## Create `book` tables
```
create table book (
    id int not null auto_increment primary key,
    title varchar(200) not null,
    isbn varchar(20) not null
);
```

## Insert into table
```
insert into book (title, isbn) values ('Lord of the Rings', '123-X-123-X');
```

### Insert many
```
insert into book (title, isbn) values ('Twilight', '1234-A'),
    ('Chronicles of Narina', '1233-B'),
    ('Watership Down', '4560X');
```

## Delete items
```
delete from book where id = 4
```

## Update a row
```
update author set first_name="Clark Staples" where id = 2;
```

## Add in a new column
```
ALTER TABLE book
ADD language varchar(100);
```

## SELECTING
```
/* Select ALL columns from the table */
select * from author
```

```
/* Select only a few columns from the table */
select first_name, last_name from author
```

```
/* Select specific rows from the table */
select * from author where nationality like "UK";
select first_name, last_name from author where nationality like "UK"
```

```
/* compunds */
/* we are join multiple criteria with AND/OR */
select * from author where first_name like "Lewis" and nationality like "UK"
select * from author where first_name like "Lewis" or nationality like "UK
```
```
/* wild cards */
/* select all authors whose first name starts with "lew"
select * from author where first_name like "lew%"

/* select all authors whose first name ends with "lew"
select * from author where first_name like "%lew"

/* select all authors whose first name contains "lew" anywhere */
select * from author where first_name like "%lew%"
```
