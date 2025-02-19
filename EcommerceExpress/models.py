# In-memory storage for products and carts
products = {
    1: {
        'id': 1,
        'name': 'Gaming Laptop',
        'price': 999.99,
        'description': 'High-performance gaming laptop with RGB keyboard',
        'image': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400&h=300&fit=crop',
        'stock': 10
    },
    2: {
        'id': 2,
        'name': 'Wireless Mouse',
        'price': 29.99,
        'description': 'Ergonomic wireless mouse with long battery life',
        'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400&h=300&fit=crop',
        'stock': 50
    },
    3: {
        'id': 3,
        'name': 'Mechanical Keyboard',
        'price': 89.99,
        'description': 'Mechanical gaming keyboard with Cherry MX switches',
        'image': 'https://images.unsplash.com/photo-1601445638532-3c6f6c3aa1d6?w=400&h=300&fit=crop',
        'stock': 25
    }
}

# In-memory cart storage
carts = {}