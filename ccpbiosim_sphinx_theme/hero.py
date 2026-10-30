"""The ``ccpbiosim-hero`` directive for project home pages."""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class HeroDirective(SphinxDirective):
    """Render a home page banner with a logo, tagline, summary and buttons.

    Every option is optional, and the directive content becomes the summary.
    The page title is hidden on pages with a hero, because the hero replaces it.

    With ``:logo:``, the banner is a dark navy panel, so use a logo with white
    text. With ``:logo-light:`` and ``:logo-dark:`` instead, the banner has no
    panel and shows the logo for the current light or dark mode.

    Example::

        .. ccpbiosim-hero::
           :logo: _static/logo-white-text.svg
           :tagline: A one-line description of the project
           :button: installation | Get started
           :github: CCPBioSim/my-project

           A short summary of what the project does.
    """

    has_content = True
    option_spec = {
        "logo": directives.unchanged,
        "logo-light": directives.unchanged,
        "logo-dark": directives.unchanged,
        "logo-alt": directives.unchanged,
        "tagline": directives.unchanged,
        "button": directives.unchanged,
        "github": directives.unchanged,
    }

    def run(self) -> list[nodes.Node]:
        alt = self.options.get("logo-alt", f"{self.config.project} logo")
        light = self.options.get("logo-light")
        dark = self.options.get("logo-dark")
        plain = bool(light and dark)

        lines = [".. container:: ccp-hero" + (" ccp-hero-plain" if plain else ""), ""]

        if plain:
            for logo, mode in [(light, "only-light"), (dark, "only-dark")]:
                lines += [
                    f"   .. image:: {logo}",
                    f"      :alt: {alt}",
                    f"      :class: {mode}",
                    "",
                ]
        elif logo := self.options.get("logo"):
            lines += [
                f"   .. image:: {logo}",
                f"      :alt: {alt}",
                "      :class: dark-light",
                "",
            ]

        if tagline := self.options.get("tagline"):
            lines += ["   .. container:: ccp-hero-tagline", "", f"      {tagline}", ""]

        if self.content:
            lines += ["   .. container:: ccp-hero-summary", ""]
            lines += [f"      {line}" for line in self.content]
            lines += [""]

        buttons = []
        if button := self.options.get("button"):
            target, _, text = button.partition("|")
            buttons += [
                f"      .. button-ref:: {target.strip()}",
                "         :ref-type: doc",
                "         :color: primary",
                "",
                f"         {text.strip() or 'Get started'}",
                "",
            ]
        if github := self.options.get("github"):
            buttons += [
                f"      .. button-link:: https://github.com/{github}",
                f"         :color: {'primary' if plain else 'light'}",
                "         :outline:",
                "",
                "         :fab:`github` View on GitHub",
                "",
            ]
        if buttons:
            lines += ["   .. container:: ccp-hero-buttons", ""] + buttons

        return self.parse_text_to_nodes("\n".join(lines), offset=self.content_offset)
