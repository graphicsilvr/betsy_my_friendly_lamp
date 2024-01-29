<p><a target="_blank" href="https://app.eraser.io/workspace/LBT0Qn6f6ATu7GVqvSV3" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# Besty Marketplace
## Introduction
Betsy Marketplace is aonline platform for selling and purchasing a variety of products. The platform is designed as a web marketplace where users can list and sell homemade goods, making it an ideal testbed for database modeling, SQL joins, and the implementation of functional programming using Python and Peewee ORM.

## Prerequisites
- Python 3.6 or higher
- Peewee ORM
- SQLite database
## Installation and Setup
1. Clone the repository.
2. Ensure Python 3.6+ is installed.
3. Install Peewee ORM: `pip install peewee` .
4. Run the `main.py`  script to start the application.
## Database Structure
Betsy Marketplace employs an SQLite database, with the following models managed through the Peewee ORM:

### User Model
- Represents users with attributes like name, address, and billing information.
- Users can own multiple products and make purchases.
### Product Model
- Includes details such as product name, description, price, and stock quantity.
- Products are owned by users and can be tagged with various descriptors.
### Tag Model
- Provides a system for tagging products, ensuring unique identification.
### Transaction Model
- Tracks purchases made on the marketplace, linking buyers with products and quantities.
## Functionalities
The `main.py` file contains several key functionalities:

### User Interactions
- **Registering and Managing Users**: Create and handle user accounts, including their personal and billing information.
### Product Management
- **Adding and Removing Products**: Users can list new products and remove existing ones.
- **Updating Product Details**: Modify product information like price and stock quantity.
### Transaction Handling
- **Purchase Processing**: Record and manage the buying and selling transactions between users.
### Tagging System
- **Product Tagging**: Assign tags to products for better categorization and searchability.
### Search and Query Features
- **Product Search**: Implement a case-insensitive search for products based on names.
- **View Products by User**: Display all products listed by a specific user.
- **Products by Tag**: Retrieve products associated with a given tag.
## Testing and Data Population
- The `populate_test_database.py`  script is used to fill the database with example data, ensuring the smooth functionality of queries and operations.
## Future Enhancements
- **Advanced Search**: Enhance search functionality to include product descriptions and handle spelling variations.
- **Performance Optimization**: Implement product indexing for faster query execution.
- **Complex SQL Joins**: Further develop the querying system to handle more intricate database relationships, particularly in transactions.
## Debugging and Development
- The project has undergone rigorous debugging and iterative development to ensure robust performance and user-friendly interfaces.
## Conclusion
Betsy Marketplace serves as a dynamic platform demonstrating advanced database operations, ORM usage, and Python programming capabilities. The project is an ongoing endeavor with potential for further enhancements and optimizations.

## License
Please refer to the provided license file for detailed licensing information.

---

This `README.md` is designed to offer a clear and concise overview of the Betsy Marketplace project, highlighting its features, structure, and future development directions. Adjust and expand as necessary to align with your project's specifics.


<!--- Eraser file: https://app.eraser.io/workspace/LBT0Qn6f6ATu7GVqvSV3 --->