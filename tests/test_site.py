"""
Very simple sanity checks for the static site.
These run automatically on every Pull Request via GitHub Actions.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_index_html_exists():
    assert os.path.exists(os.path.join(ROOT, "index.html")), "index.html is missing!"


def test_stylesheet_exists():
    assert os.path.exists(os.path.join(ROOT, "assets", "style.css")), "style.css is missing!"


def test_index_html_has_title():
    with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
        content = f.read()
    assert "<title>" in content, "index.html is missing a <title> tag"


def test_index_html_links_stylesheet():
    with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
        content = f.read()
    assert "style.css" in content, "index.html does not link to style.css"
