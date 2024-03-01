# Library Management
A CLI library management system, a project deeply rooted in Object-Oriented Programming (OOP) principles.


## Features
The application provides a range of services tailored to meet the needs of both users and administrators:

### User Experience:
- **User Registration/Login:** Users can easily register or log in, allowing them to access various services.

- **Book Search:** Users can search for books using filters such as title, author, or publisher.

- **Book Rental/Return:** Users can rent and return books hassle-free, with fees calculated based on rental duration and book price.

### Administrative Tools:

- **Transaction Management:** Administrators can list and view detailed transaction information, including rental and return activities, fees, and dates.

- **Book Management:** Administrators have full control over the library's inventory, with the ability to add or remove books from the database.

- **Financial Oversight:** Administrators can monitor the library's total balance, ensuring financial stability.


## Tools & Technologies
The project leverages various tools and technologies to deliver a robust solution:

- **OOP:** Object-oriented programming forms the backbone of our project, facilitating modular and maintainable code.  

- **Unit Testing:** Rigorous unit testing ensures the reliability and functionality of our application.

- **Regular Expressions (RegEx):** RegEx simplifies user input handling, enhancing user experience and reducing complexity.

- **Exceptions Handling:** Effective exception handling provides clear error messages and prevents error propagation.

- **Database Management:** Was used SQLAlchemy with a Sqlite3 engine to manage the application's database, ensuring efficient data storage and management.


## Challenges
Building this application posed several challenges, including:

- **Python Programming**  
Choosing Python as the programming language offered numerous advantages, including its simplicity and widespread use. However, this decision also brought unique challenges. Python's approach to encapsulation and access control differs from languages like Java. While we can signalize that a certain attribute is private by prefixing it with an underscore (_), Python itself doesn't prevent it from being directly accessed. This presented challenges when implementing private/protected attributes, requiring solutions to maintain data integrity and security.

- **Object-Oriented Programming Complexity**  
Object-Oriented Programming (OOP) is a powerful paradigm for structuring code, but it can be complex, particularly when working with ORM (Object-Relational Mapping) libraries like SQLAlchemy. Designing a well-structured implementation of the application required a good understanding of OOP concepts such as abstraction, encapsulation, and inheritance. Managing multiple modules simultaneously and navigating concepts like classes/objects, inheritance, class methods, and message passing added layers of complexity to the development process.

- **Application Safety & Data Integrity**  
Ensuring the safety and integrity of the application and its data was a base idea. Python's flexibility provided considerable freedom in managing access to data, but it also introduced potential security risks. Implementing robust safeguards was essential to prevent unauthorized access and maintain data integrity. For example, booting book and administrative account datasets in a separate configuration module instead of hardcoding them helped enhance security and mitigate the risk of data manipulation.

