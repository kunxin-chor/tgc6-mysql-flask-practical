/* create a table */
create table book (
    id int not null auto_increment primary key,
    title varchar(200) not null,
    isbn varchar(20) not null
);

insert into book (title, isbn) values ('Lord of the Rings', '123-X-123-X');