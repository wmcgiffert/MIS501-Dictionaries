# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # MIS 501 — Lecture 7: Dictionaries
    ### In-class exercise — the coffee shop terminal

    Same coffee shop as the loops lab, but the menu is now a **dictionary**:
    item names are keys and prices are values.

    Fill in each function. Do not change the run cell at the bottom.

    1. `print_menu(menu)` — loop through the dictionary and print each item with its price
    2. `get_price(menu, item)` — look up one item's price (`if` / `else`; unknown items return `0.0`)
    3. `take_order()` — a **while loop** reads items until the user types `END`
    4. `calculate_total(menu, order)` — a **for loop** adds each price into a running total
    """)
    return


@app.cell
def _():
    # Our coffee shop menu (item name -> price)
    menu = {
        "latte": 4.50,
        "muffin": 3.00,
        "drip coffee": 2.25,
        "bagel": 2.50,
    }
    return (menu,)


@app.function
# Task 1 — loop through the dictionary and print each item (for loop)
def print_menu(menu):
    return


@app.function
# Task 2 — return the price for a single item from the dictionary
# unknown items should return 0.0
def get_price(menu, item):
    return 0.0


@app.function
# Task 3 — keep asking with input() until the user types "END" (while loop)
def take_order():
    return []


@app.function
# Task 4 — look up each item's price, then total them
def calculate_total(menu, order):
    return 0.0


@app.cell
def _(menu):
    # Run it — prints the menu, asks for your order, shows the total
    print_menu(menu)
    order = take_order()
    print("You ordered:", order)
    print(f"Total: ${calculate_total(menu, order):.2f}")
    return


if __name__ == "__main__":
    app.run()
