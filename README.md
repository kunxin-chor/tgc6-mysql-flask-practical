# Insructions to install PhpMyAdmin

Demonstrate how to use PhpMyAdmin with a project created from the code institute Gitpod Template.

The commands are found in `install.sh` - the file is now automatically run as part of the `init_tasks.sh` script inside the `.theia` folder. If you are interested in just install PHPMyAdmin for an existing GitPod instance, you can just copy the script over in a .sh file (and be sure to set the executable permission with `chmod -u=rwx` on the file first!).

You still need to do one manual step to configure PHPMyAdmin correctly:

To setup PHPMyAdmin for GitPod:

1. Find the file `public/phpmyadmin/config.inc.php`
2. Look for the string `AllowNoPassword`
3. Change the line to read: `$cfg['Servers'][$i]['AllowNoPassword'] = true;` and *remember to save*
4. Start apache with `apachectl start` and when the pop-up appears, click `Open Browser`
5. At the browser, add `/phpmyadmin` to the end of the URL in the address bar
6. Login with user `root` and no password.

# Installing existing database

At the terminal, type in

```
mysql -u root < chinook-sql.sql
```

# Logging in to MySQL client

```
mysql -u root
```

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
## JOINS

Join employees on office code where the emplyoee's officecode matches the office code in the offices table.
THEN select the last name, first name, city, country, addressLine and addressLine 2 columns
```
SELECT lastName, firstName, city, country, addressLine1, addressLine2 
FROM employees INNER JOIN offices ON employees.officeCode = offices.officeCode
```

Selct all emplyoees where their offices are in USA
```
SELECT * FROM employees JOIN offices
 ON employees.officeCode = offices.officeCode
 WHERE country="USA" 
```

If we want to select a column that is repeated on both side, we must specify a table name in front of it:
```
SELECT  products.productCode, productName, orderNumber, quantityOrdered FROM products JOIN orderdetails
ON products.productCode = orderdetails.productCode
```

Find all the customers and the name of the product they have ordered and the quantity ordred:
```
SELECT customerName, productName, quantityOrdered FROM products JOIN orderdetails
ON products.productCode = orderdetails.productCode
JOIN orders
ON orderdetails.orderNumber = orders.orderNumber
JOIN customers
ON orders.customerNumber = customers.customerNumber
```

## sorting
```
SELECT * FROM customers order by creditLimit DESC
```

## Group By
Group all employees by their city and count how many there are in each group
```
SELECT city, count(*)  FROM employees JOIN offices 
ON employees.officeCode = offices.officeCode
group by city

```

## Order of the select claues
```
SELECT city, count(*)  FROM employees JOIN offices 
ON employees.officeCode = offices.officeCode
WHERE country="USA"
group by city
order by count(*) DESC
limit 2
```

1. JOIN
2. WHERE
3. GROUP By
4. SELECT
5. ORDER By
6. limit


## Aggregate functions

Show the sum of credit limit for all the customers in each country
```
SELECT country, SUM(creditLimit) FROM customers
GROUP BY country
```

Show the maximum credit limit in each country

```
SELECT country, MAX(creditLimit) FROM customers
GROUP BY country
```

Show the minimum credit limit in each country
```
SELECT country, MIN(creditLimit) FROM customers
GROUP BY country
```

Show the average credit limit in each country
```
SELECT country, AVG(creditLimit) FROM customers
GROUP BY country
```
