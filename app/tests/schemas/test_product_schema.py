import pytest
from app.schemas.product import Product

def test_product_schema():
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=22.99,
        stock=22
    )

    assert product.dict() == {
        'name': 'Camisa Mike',
        'slug': 'camisa-mike',
        'price': 22.99,
        'stock': 22
    }

def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa mike'
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='cão'
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='Camisa-mike'
        )

def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa mike',
            price=0,
            stock=22
        )

def test_product_input_schema():
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=22.99,
        stock=22
    )

    product_input = ProductInput(
        category_slug='roupa',
        product=product
    )

    assert product_input.dict() == {
        "category_slug": "roupa",
        "product": {
            "name": "Camisa Mike",
            "slug": "camisa-mike",
            "price": 22.99,
            "stock": 22
        }
    }