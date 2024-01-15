from models import User, Product, Tag, ProductTag, Transaction

def search_products(term):
    return Product.select().where(Product.name.contains(term.lower()))

def view_user_products(user_id):
    return Product.select().where(Product.owner == user_id)

def view_products_by_tag(tag_name):
    return Product.select().join(ProductTag).join(Tag).where(Tag.name == tag_name)

def add_product_to_user(user_id, name, description, price, quantity):
    user = User.get(User.id == user_id)
    return Product.create(owner=user, name=name, description=description, price=price, quantity=quantity)

def remove_product(product_id):
    product = Product.get(Product.id == product_id)
    product.delete_instance()

def update_stock(product_id, new_quantity):
    product = Product.get(Product.id == product_id)
    product.quantity = new_quantity


