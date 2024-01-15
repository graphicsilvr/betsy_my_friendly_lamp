from models import db, User, Product, Tag, ProductTag, Transaction


def populate_test_database():
    db.connect()
    db.create_tables([User, Product, Tag, ProductTag, Transaction], safe=True)

    # Define test users
    users = [
        {"name": "Alice", "address": "123 Wonderland", "billing_info": "Visa 1234"},
        {"name": "Bob", "address": "456 Nowhere", "billing_info": "MasterCard 5678"},
        {"name": "Charlie", "address": "789 Somewhere", "billing_info": "Amex 9012"},
        {"name": "David", "address": "012 Anywhere", "billing_info": "Visa 3456"},
        {"name": "Eve", "address": "345 Anywhere", "billing_info": "MasterCard 7890"},
        {"name": "Frank", "address": "678 Anywhere", "billing_info": "Amex 1234"}
    ]

    # Insert users
    for user_data in users:
        User.get_or_create(**user_data)

    # Define test products and tags
    products = [
        {
            "name": "Handmade Sweater",
            "description": "A cozy woolen sweater",
            "price": 49.99,
            "quantity": 10,
            "owner": 1,
        },
        {
            "name": "Artisan Coffee Mug",
            "description": "A mug for your morning brew",
            "price": 15.99,
            "quantity": 20,
            "owner": 2,
        },
        {"name": "Trousers", 
        "description": "A pair of trousers",
        "price": 29.99,
        "quantity": 5,
        "owner": 3,
        },
        {"name": "T-Shirt",
        "description": "A plain white t-shirt",
        "price": 9.99,
        "quantity": 15,
        "owner": 4,
        },
        {"name": "Coffee Table",
        "description": "A wooden coffee table",
        "price": 99.99,
        "quantity": 1,
        "owner": 5,
        },
        {"name": "Curtains",
        "description": "A pair of curtains",
        "price": 19.99,
        "quantity": 2,
        "owner": 6,
        },
        
    ]
    tags = ["Fashion", "Furniture", "Home Decor", "Kitchen", "Art", "Clothing", "Accessories"]

    # Insert products and tags
    for product_data in products:
        Product.get_or_create(**product_data)
    for tag_name in tags:
        Tag.get_or_create(name=tag_name)

    # Create Product-Tag relationships
    ProductTag.get_or_create(product=1, tag=1)
    ProductTag.get_or_create(product=2, tag=2)
    ProductTag.get_or_create(product=3, tag=3)
    ProductTag.get_or_create(product=4, tag=4)
    ProductTag.get_or_create(product=5, tag=5)
    ProductTag.get_or_create(product=6, tag=6)
    ProductTag.get_or_create(product=7, tag=7)
    ProductTag.get_or_create(product=8, tag=8)

    # Define test transactions
    transactions = [
        {"buyer": 1, "product": 2, "quantity": 2},
        {"buyer": 2, "product": 1, "quantity": 3},
        {"buyer": 3, "product": 3, "quantity": 8},
        {"buyer": 4, "product": 4, "quantity": 6},
        {"buyer": 5, "product": 5, "quantity": 1},
        {"buyer": 6, "product": 6, "quantity": 2},
        {"buyer": 7, "product": 2, "quantity": 9},
        {"buyer": 8, "product": 1, "quantity": 4},
        
    ]

    # Insert transactions
    for transaction_data in transactions:
        Transaction.get_or_create(**transaction_data)

    db.close()


if __name__ == "__main__":
    populate_test_database()
