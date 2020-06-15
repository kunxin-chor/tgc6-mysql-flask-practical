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