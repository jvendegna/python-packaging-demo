import os
from typer.testing import CliRunner
from op1fun.main import app, get_headers
from pathlib import Path

runner = CliRunner()


def test_create_headers_file():
    # Set path to headers file
    headers_path: Path = Path(str(os.getcwd() + "/op1fun/headers.json"))
    # It should exist
    assert headers_path.is_file()
    # Delete it and recreate but leave empty
    os.remove(headers_path)
    open(headers_path, "w+")
    assert headers_path.is_file()
    assert os.stat(headers_path).st_size == 0
    # next line tests that an empty headers file is deleted
    get_headers(os.getenv("OP1FUN_EMAIL"), os.getenv("OP1FUN_TOKEN"))
    assert not headers_path.is_file()
    # recreate the file and populate accordingly, must pass for the rest of the tests to work
    get_headers(os.getenv("OP1FUN_EMAIL"), os.getenv("OP1FUN_TOKEN"))
    assert headers_path.is_file()


def test_get_user():
    result = runner.invoke(app, ["get-user"])
    assert result.exit_code == 0
    assert "jaek" in result.output


def test_get_patches():
    result = runner.invoke(app, ["get-patches"])
    assert result.exit_code == 0
    assert "data" in result.output


def test_get_patch():
    result = runner.invoke(
        app,
        [
            "get-patch",
            "--username",
            "chadzyy",
            "--patch-id",
            "patch-drum-6a8c20f4-17d3-4543-b814-808a43007de7",
        ],
    )
    assert result.exit_code == 0
    assert "Futon Hats" in result.output


def test_get_packs():
    result = runner.invoke(app, ["get-packs"])
    assert result.exit_code == 0
    assert "drums-36107" in result.output


def test_get_pack():
    result = runner.invoke(app, ["get-pack", "--pack-id", "drums-36107"])
    assert result.exit_code == 0
    assert '"name": "RLND_TR808"' in result.output


def test_download_pack():
    result = runner.invoke(
        app, ["download-pack", "--username", "jaek", "--pack-id", "drums-36107"]
    )
    assert result.exit_code == 0
    zip_path: Path = Path(str(os.getcwd() + "/drums-36107.zip"))
    assert zip_path.is_file()
    os.remove(zip_path)
    assert not zip_path.is_file()


def test_all_commands_present_in_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "get-user" in result.output
    assert "download-pack" in result.output
    assert "get-pack" in result.output
    assert "get-packs" in result.output
    assert "get-patch" in result.output
    assert "get-patches" in result.output
