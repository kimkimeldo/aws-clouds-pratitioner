# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'CC6L'
copyright = '2025, BSIT3'
author = 'Eldo Kimverlie, Chicano Darnel Dave, Espinosa Luwella, Pampanga Mayvill Joy'
group = '6'

release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
