from importlib.metadata import entry_points

import ccpbiosim_sphinx_theme


def test_version():
    assert ccpbiosim_sphinx_theme.__version__


def test_theme_is_registered_with_sphinx():
    themes = entry_points(group="sphinx.html_themes")
    assert ccpbiosim_sphinx_theme.THEME_NAME in themes.names


def test_theme_files_are_bundled():
    theme = ccpbiosim_sphinx_theme.THEME_PATH
    for name in [
        "theme.toml",
        "layout.html",
        "ccpbiosim-footer.html",
        "static/ccpbiosim-favicon.svg",
        "static/ccpbiosim.css",
        f"static/{ccpbiosim_sphinx_theme.LOGO}",
    ]:
        assert (theme / name).is_file(), name
