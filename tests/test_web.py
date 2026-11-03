"""Checks that the browser version loads every file of the game."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_app_js_lists_every_python_file():
    app_js = (ROOT / "web" / "app.js").read_text(encoding="utf8")
    listed = set(re.findall(r'"(fury/[\w.]+\.py)"', app_js))
    on_disk = {p.relative_to(ROOT).as_posix()
               for p in (ROOT / "fury").glob("*.py")}
    assert listed == on_disk


def test_art_fits_the_50_column_terminal():
    from fury import art  # pylint: disable=import-outside-toplevel
    ansi = re.compile(r"\x1b\[[0-9;]*m")
    for name in dir(art):
        value = getattr(art, name)
        if name.isupper() and isinstance(value, str) and "\n" in value:
            widest = max(len(ansi.sub("", line)) for line in value.splitlines())
            assert widest <= 50, name
