import json
import os
import requests
import typer
from typing import Optional
from pathlib import Path

CWD = os.getcwd()
APP_NAME = str(CWD + "/op1fun")

app = typer.Typer(name=APP_NAME)

email = os.getenv("OP1FUN_EMAIL")
token = os.getenv("OP1FUN_TOKEN")


# Setup authentication
def get_headers(email: Optional[str], token: Optional[str]):
    app_dir = typer.get_app_dir(APP_NAME)
    config_path: Path = Path(app_dir) / "headers.json"

    if config_path.is_file():
        typer.secho("Loading Headers", color=typer.colors.BRIGHT_GREEN)
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            typer.secho(
                "Headers file exists but is empty, deleting file. Re-run the last command",
                color=typer.colors.BRIGHT_MAGENTA,
            )
            os.remove(config_path)
    else:
        typer.secho(
            "Headers file not found, creating it now", color=typer.colors.MAGENTA
        )

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-User-Token": f"{token}",
            "X-User-Email": f"{email}",
        }

        with open(config_path, "w") as f:
            json.dump(headers, f)

        typer.secho("Headers file created", color=typer.colors.BRIGHT_GREEN)


headers = get_headers(email, token)


@app.command()
def get_user(username: str = "jaek"):
    url = f"https://api.op1.fun/v1/users/{username}"
    response = requests.get(url, headers=headers)
    typer.echo(json.dumps(response.json(), indent=2, sort_keys=True))
    return json.dumps(response.json(), indent=2, sort_keys=True)


@app.command()
def get_patches(username: str = "jaek"):
    url = f"https://api.op1.fun/v1/users/{username}/patches"
    response = requests.get(url, headers=headers)
    typer.echo(json.dumps(response.json(), indent=2, sort_keys=True))


@app.command()
def get_patch(username: str = "jaek", patch_id: str = None):
    url = f"https://api.op1.fun/v1/users/{username}/patches/{patch_id}"
    response = requests.get(url, headers=headers)
    typer.echo(json.dumps(response.json(), indent=2, sort_keys=True))


@app.command()
def get_packs(username: str = "jaek"):
    url = f"https://api.op1.fun/v1/users/{username}/packs"
    response = requests.get(url, headers=headers)
    typer.echo(json.dumps(response.json(), indent=2, sort_keys=True))


@app.command()
def get_pack(username: str = "jaek", pack_id: str = ""):
    url = f"https://api.op1.fun/v1/users/{username}/packs/{pack_id}"
    response = requests.get(url, headers=headers)
    typer.echo(json.dumps(response.json(), indent=2, sort_keys=True))


@app.command()
def download_pack(username: str = "jaek", pack_id: str = "drums-36107"):
    url = f"https://api.op1.fun/v1/users/{username}/packs/{pack_id}/download"
    response = requests.get(url, headers=headers)
    with open(f"{pack_id}.zip", "wb") as f:
        f.write(response.content)
    typer.echo(f"Downloaded {pack_id}.zip")


if __name__ == "__main__":
    app()  # pragma: nocover
