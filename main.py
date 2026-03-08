import os
import webbrowser
from datetime import date

import click
import requests
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("apod.html.j2")

BASE_URL = "https://api.nasa.gov/planetary"
TIMEOUT = 3


@click.command()
@click.option(
    "--date",
    default=date.today().isoformat(),
    help="The date for the pic-of-the-day. Must be between June 16, 1995 and today. Format: YYYY-MM-DD",
)
@click.option("--api_key", envvar="NASA_API_KEY", default="DEMO_KEY", help="Your NASA API key.")
def apod(date: str, api_key: str) -> None:
    endpoint: str = f"{BASE_URL}/apod"

    try:
        response = requests.get(
            endpoint,
            params={
                "api_key": api_key,
                "date": date,
            },
            timeout=TIMEOUT,
        )

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to NASA API: {e}")
        return

    data: dict = response.json()
    if response.status_code != 200:
        print(data.get("msg", "An unknown error occurred."))
        return

    content: str = template.render(data)

    with open("apod.html", "w") as f:
        f.write(content)

    webbrowser.open_new_tab(f"file://{os.path.realpath(f.name)}")


if __name__ == "__main__":
    apod()
