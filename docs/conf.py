project = "nextcord.ext.activities"
copyright = "2022, MaskDuck"
author = "MaskDuck"
release = "2022.04.02"
version = "2022.04.02"

autosectionlabel_prefix_document = True
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel"
]

language = "en"

autodoc_member_order = "bysource"

html_theme = "furo"

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "nextcord": ("https://nextcord.readthedocs.io/en/latest/", None),
}
