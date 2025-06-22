
import click
from lib.models.base import Session
from lib import Flower, Customer, Order

@click.group()
def app():
    """ Welcome to Lush & Leaf CLI """
    pass

@app.command()
def view_flowers():
    session = Session()
    flowers = session.query(Flower).all()
    if not flowers:
        click.echo("No flowers available.")
    for f in flowers:
        click.echo(f"{f.id}. {f.name} - ${f.price} (Stock: {f.stock})")
    session.close()

@app.command()
@click.option("--customer-id", prompt="Customer ID", type=int)
@click.option("--flower-id", prompt="Flower ID", type=int)
@click.option("--quantity", prompt="Quantity", type=int)
def order_flower(customer_id, flower_id, quantity):
    session = Session()
    customer = session.query(Customer).get(customer_id)
    flower = session.query(Flower).get(flower_id)

    if not customer or not flower:
        click.echo("Invalid customer or flower ID.")
        return

    if flower.stock < quantity:
        click.echo("Not enough stock!")
        return

    order = Order(customer=customer, flower=flower, quantity=quantity)
    flower.stock -= quantity
    session.add(order)
    session.commit()
    click.echo("Order placed!")
    session.close()

if __name__ == "__main__":
    app()

