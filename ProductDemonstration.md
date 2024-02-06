# Product Demonstration

## Login Page

When the user first enters the website, they will be greeted with a login page.

Once the user has keyed in their email and password, they can click on the Submit button to login.

The user’s credentials will be checked against the database. 

If there is no such user or the user’s credentials do not match, an error message will appear.

In the future version, users will be able to register for an account. The security of the login feature will also be enhanced by salting and hashing the password before storing it into the database. When a user logs in, the user’s entered password will be compared against the user’s hashed password stored in the database.


## Dashboard

Once the user has successfully logged into their account, they will be directed to the Dashboard page. 

The course list data will be pulled from the database and reflect accordingly. 

The user can click on the Sign Up button to add the course into their registered course list.

The user can also utilise the side navigation bar to easily access the other pages of the website.

The search bar is currently a static UI for the MVP but in the future version, the user will be able to search for a course and the course list will dynamically reflect the search.

The “Welcome, User” string in the header is static hard-coded data and will reflect the user’s first and last name once the Profile page is set up.

My Course section currently reflects static hard-coded data and in the future version, it will reflect the following:

In Progress - Users will be able to track the progress of the course they are currently taking. The percentage of the user’s progress will be based on the total number of lessons available for the course and the total number of lessons they have completed. Users will also be able to view an overview of their training hours and the training hours that they are lacking for both skill categories (soft and technical skills).

Incoming - HR Officers and HR Supervisors will be able to assign courses to the users and the users will be able to view the courses assigned to them.

Completed - Users will be able to view the courses that they have completed.


## Courses

When the user registers for a course through the Sign Up button, the user will be directed to the Courses page.

The user will be able to view all the courses that they have registered for.

If the user wishes to unregister from any course that they have registered, the user can click on the Unregister button.

Upon clicking the Unregister button, the course will be removed for the user in the database and the Courses page will reflect accordingly.

The user is also able to click on the Register for Course button should they wish to apply for a new course. 

The Register for Course button will redirect the user to the Dashboard page for the user to view the Course List for course sign ups.

In the future version, the registered course will show the details of the course and the date and time of the course the user has registered for. The registered courses will only reflect courses with present and future dates.


## Data Modeling

The data model below reflects the current database schema of the MVP Product Demonstration.

The data model will be updated in the future to reflect new data required for the future version of the product.

