# Flask execrise

Using the `classicmodels` database, and adding to `app.py`, create the following routes

## /offices
Display all the offices there are in the system, showing each office's city and address. When the user clicks on an office,
displays all the employees that there in the office in the route `/show_employees_in_office/<office_code>`

## /employees
Display all the employees there are, allowing the user to search by first name or last name. Other filtering options include
filtering by country and job title. The filtering is done via. a `<select>` dropdown.

Being able to fufill the sub-tasks below will help:
    * How do get all the distinct countries in the `employees` table?
    * How do get all the distinct job title in the `employees` table

## /create_office
Display a form that allows the user to create a new office. You can allow the user to just type in the name of the country via
a text input (though it is a good idea to have a dropdown with all the available countries for a real project).

After the user has submitted the form, create the new office and redirect the user back to the `/offices` route.

## /create_employee
Display a form that allows the user to create a new employee. Use a `<select>` dropdown for choosing which office the employee 
will belong to. In the dropdown, display each office's city and country (we assume only one office per city).

Being able to fufill the sub-tasks below will help with this question:
    * How do get all the offices there are in and present them in a `<select>`
