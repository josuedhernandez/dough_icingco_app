"""Main application module for the Dough & Icing Co. Flask website."""

import os
from flask import Flask, render_template, current_app, request

app = Flask(__name__)

SOCIAL_LINKS = {
    "Facebook": "https://www.facebook.com/profile.php?id=61579114576580",
    "Instagram": "https://www.instagram.com/doughandicingco",
}


@app.context_processor
def inject_social_links() -> dict[str, dict[str, str]]:
    """Make social_links available to all templates automatically."""
    return {"social_links": SOCIAL_LINKS}

@app.route("/")
def home() -> str:
    """Render the home page of the bakery website."""
    # Use current_app.root_path to get the absolute path to your project folder
    image_folder = os.path.join(current_app.root_path, "static", "images")

    # Safety check: if the folder doesn't exist, return an empty list instead of crashing
    if not os.path.exists(image_folder):
        images = []
    else:
        images = [
            f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".jpeg"))
        ]

    if not images:
        app.logger.warning("No images found in the %s directory.", image_folder)
    else:
        app.logger.info("Successfully loaded %s images for the gallery.", len(images))

    return render_template(
        "index.html",
        header="Dough & Icing Co.",
        content="Welcome to Dough & Icing Co.—a small-batch bakery specializing in beautiful "
        "cookies and handcrafted treats, where every cookie tells a story. Each batch is "
        "thoughtfully created to make your special moments even sweeter.",
        images=images,
    )


@app.route("/products")
def products() -> str:
    """Render the products page showing daily availability."""
    # Sample data for the dynamic grid
    daily_items = [
        {
            "name": "Sourdough Loaf",
            "description": "Freshly baked rustic sourdough.",
            "tag": "Limited Quantity",
        },
        {
            "name": "Sugar Cookies",
            "description": "Custom decorated vanilla bean cookies.",
            "tag": "Available",
        },
        {
            "name": "Cinnamon Rolls",
            "description": "Warm, gooey, and glazed.",
            "tag": "Sold Out",
        },
        {
            "name": "Focaccia",
            "description": "Rosemary and sea salt.",
            "tag": "Limited Quantity",
        },
    ]

    return render_template(
        "products.html",
        header="Today's Oven",
        content="Here is what is available to order.",
        items=daily_items,
    )


@app.route("/order", methods=["GET", "POST"])
def order() -> str:
    """Render the order/contact page."""
    if request.method == "POST":
        # Placeholder for form processing logic
        pass

    return render_template(
        "order.html",
        header="Say Hello & Reserve Your Batch",
        content="Reach out to place an order or just say hello!",
    )


@app.route("/about")
def about() -> str:
    """Render the about page with information about the bakery."""
    return render_template(
        "about.html",
        header="About Us",
        content="We are a family-owned bakery specializing in delicious custom sugar cookies "
        "and beautiful sourghdough bread.",
    )


if __name__ == "__main__":
    app.run(debug=True)
