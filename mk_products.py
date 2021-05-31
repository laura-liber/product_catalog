#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Sample python code that creates products and displays them."""

from app import db
from app.database import Product

def create_product(name, price, quantity):
    """[summary]

    Parameters
    __________
    name  :  str
        The product's name
    price  :  float
        Price expressed in this format: XX:YY
    quantity  :  int
        The total quantity available.
    """
    db.session.add(
        Product(
            name=name,
            price=price,
            quantity=quantity
        )
    )
    db.session.commit()


if __name__ == "__main__":
    create_product("Bananas", 10.00, 10)
    create_product("Oranges", 12.00, 50)
    products = Product.query.all()
    print(products)