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
    src.mkdir()
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
