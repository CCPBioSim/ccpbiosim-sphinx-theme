"""CCPBioSim theme for Sphinx documentation.

A child theme of pydata-sphinx-theme that matches https://www.ccpbiosim.org/.
Enable it in ``conf.py`` with::

    html_theme = "ccpbiosim_sphinx_theme"
    html_context = {"github_repo": "my-project"}

The theme also turns on sphinx-design and sphinx-copybutton, and adds the
``ccpbiosim-hero`` directive for home pages.
"""

from pathlib import Path
from typing import Any

from sphinx.application import Sphinx
from sphinx.locale import _
from sphinx_copybutton import add_to_context as add_copybutton_settings

from .hero import HeroDirective

__version__ = "1.2.0"

THEME_NAME = "ccpbiosim_sphinx_theme"
THEME_PATH = Path(__file__).parent / "theme" / THEME_NAME

WEBSITE_URL = "https://www.ccpbiosim.org/"
HUB_URL = "https://ccpbiosim.readthedocs.io/"
# pydata-sphinx-theme links logos by file name only, so this must sit at the top
# of the theme's static folder.
LOGO = "ccpbiosim-logo-white-side-text.svg"


def _theme_options(app: Sphinx) -> dict[str, Any]:
    """Return the theme options that the builder will use.

    By ``builder-inited`` the builder holds its own copy of
    ``html_theme_options``, so changes must go there to take effect.
    """
    options = getattr(app.builder, "theme_options", None)
    if options is None:
        options = app.config.html_theme_options
    return options


def _set_defaults(app: Sphinx) -> None:
    """Fill in CCPBioSim defaults for anything the project has not set."""
    if app.config.html_theme != THEME_NAME:
        return

    context = app.config.html_context
    context.setdefault("github_user", "CCPBioSim")
    context.setdefault("github_version", "main")
    context.setdefault("doc_path", "docs/source")
    repo = context.get("github_repo")

    # Tab titles use "Project Documentation" unless the project sets html_title.
    config = app.config
    site_title = config.html_title
    if site_title == _("%s %s documentation") % (config.project, config.release):
        site_title = f"{config.project} Documentation"
    context.setdefault("ccpbiosim_site_title", site_title)

    options = _theme_options(app)
    hub_url = options.get("ccpbiosim_hub_url", HUB_URL)

    options["logo"] = {
        "image_light": LOGO,
        "image_dark": LOGO,
        "alt_text": "CCPBioSim",
        "text": app.config.project,
        **options.get("logo", {}),
    }

    for key, value in {
        "navbar_align": "left",
        "header_links_before_dropdown": 6,
        "show_toc_level": 2,
        "show_prev_next": True,
        "use_edit_page_button": bool(repo),
        "secondary_sidebar_items": [],
        "footer_start": ["copyright"],
        "footer_end": ["ccpbiosim-footer"],
    }.items():
        options.setdefault(key, value)

    # The project's own icon links come after the shared ones.
    icon_links = []
    if repo:
        icon_links.append(
            {
                "name": "GitHub",
                "url": f"https://github.com/{context['github_user']}/{repo}",
                "icon": "fa-brands fa-github",
            }
        )
    icon_links += [
        {"name": "CCPBioSim docs", "url": hub_url, "icon": "fa-solid fa-book"},
        {"name": "CCPBioSim", "url": WEBSITE_URL, "icon": "fa-solid fa-globe"},
    ]
    known = {link["url"] for link in icon_links}
    icon_links += [
        link for link in options.get("icon_links", []) if link["url"] not in known
    ]
    options["icon_links"] = icon_links


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_html_theme(THEME_NAME, str(THEME_PATH))
    app.setup_extension("sphinx_design")
    app.setup_extension("sphinx_copybutton")
    add_copybutton_settings(app, app.config)
    app.add_directive("ccpbiosim-hero", HeroDirective)
    # Run before pydata-sphinx-theme reads the options at the default priority.
    app.connect("builder-inited", _set_defaults, priority=400)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
