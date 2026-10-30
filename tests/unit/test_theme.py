"""Build a small Sphinx project with the theme and check the generated HTML."""

import textwrap
from pathlib import Path

from sphinx.cmd.build import build_main

INDEX = """\
My project
==========

.. ccpbiosim-hero::
   :logo: logo.svg
   :tagline: A one-line description of the project
   :button: usage | Get started
   :github: CCPBioSim/my-project

   A short summary of what the project does.

.. toctree::

   usage
"""

USAGE = """\
Usage
=====

Some text.
"""


def build(tmp_path: Path, conf: str = "") -> Path:
    """Build a project with warnings as errors and return the output folder."""
    src = tmp_path / "src"
    src.mkdir(exist_ok=True)
    (src / "conf.py").write_text(
        'project = "My project"\n'
        'html_theme = "ccpbiosim_sphinx_theme"\n'
        'html_context = {"github_repo": "my-project"}\n' + textwrap.dedent(conf)
    )
    (src / "index.rst").write_text(INDEX)
    (src / "usage.rst").write_text(USAGE)
    (src / "logo.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')

    out = tmp_path / "html"
    assert build_main(["-W", "-q", "-b", "html", str(src), str(out)]) == 0
    return out


def test_default_build(tmp_path: Path):
    out = build(tmp_path)
    html = (out / "usage.html").read_text()

    assert "_static/ccpbiosim.css" in html
    assert 'src="_static/ccpbiosim-logo-white-side-text.svg"' in html
    assert (out / "_static" / "ccpbiosim-logo-white-side-text.svg").is_file()
    assert "https://github.com/CCPBioSim/my-project" in html
    assert "https://www.ccpbiosim.org/" in html
    assert (
        "https://github.com/CCPBioSim/my-project/edit/main/docs/source/usage.rst"
        in html
    )


def test_banner(tmp_path: Path):
    html = (build(tmp_path) / "index.html").read_text()

    assert 'class="ccp-hero' in html
    assert 'src="_images/logo.svg"' in html
    assert "A one-line description of the project" in html
    assert "A short summary of what the project does." in html
    assert 'href="usage.html"' in html


def test_empty_sidebar_is_hidden(tmp_path: Path):
    out = build(tmp_path)
    html = (out / "usage.html").read_text()
    css = (out / "_static" / "ccpbiosim.css").read_text()

    # The CSS hides the sidebar using this empty element, so check
    # pydata-sphinx-theme still renders it on a page without sub-pages.
    assert '<div class="bd-toc-item navbar-nav"></div>' in html
    assert ".bd-toc-item:empty" in css


def test_copy_buttons_are_configured(tmp_path: Path):
    out = build(tmp_path, 'copybutton_prompt_text = "$ "\n')
    js = (out / "_static" / "copybutton.js").read_text()

    # sphinx-copybutton fills in this template from its settings, so check
    # the defaults and the project's own settings both reach it.
    assert "const COPYBUTTON_SELECTOR = 'div.highlight pre';" in js
    assert "formatCopyText(text, '$ ', false, true, true, true, '', '')" in js


def test_tab_title_and_icon(tmp_path: Path):
    out = build(tmp_path)
    index = (out / "index.html").read_text()
    usage = (out / "usage.html").read_text()
    search = (out / "search.html").read_text()

    assert "<title>My project Documentation</title>" in index
    assert "<title>Usage | My project Documentation</title>" in usage
    assert "<title>Search | My project Documentation</title>" in search
    assert 'href="_static/ccpbiosim-favicon.svg"' in usage
    assert (out / "_static" / "ccpbiosim-favicon.svg").is_file()


def test_project_html_title_is_used_in_tab_titles(tmp_path: Path):
    out = build(tmp_path, 'html_title = "My project docs"\n')
    usage = (out / "usage.html").read_text()

    assert "<title>Usage | My project docs</title>" in usage


def test_project_favicon_replaces_default(tmp_path: Path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "icon.png").write_bytes(b"")
    out = build(tmp_path, 'html_favicon = "icon.png"\n')
    html = (out / "usage.html").read_text()

    assert 'href="_static/icon.png"' in html
    assert "ccpbiosim-favicon.svg" not in html


def test_project_settings_override_defaults(tmp_path: Path):
    out = build(
        tmp_path,
        """\
        html_theme_options = {
            "logo": {"text": "Custom name"},
            "icon_links": [
                {"name": "PyPI", "url": "https://pypi.org/p/my-project",
                 "icon": "fa-brands fa-python"},
                {"name": "Website", "url": "https://www.ccpbiosim.org/",
                 "icon": "fa-solid fa-globe"},
            ],
        }
        """,
    )
    html = (out / "usage.html").read_text()
    header = html.split('class="navbar-icon-links')[1].split("</ul>")[0]

    assert "Custom name" in html
    assert "https://pypi.org/p/my-project" in header
    assert header.count('href="https://www.ccpbiosim.org/"') == 1
