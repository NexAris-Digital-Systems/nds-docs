# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Crazy Development'
author = 'MrRamyg'
release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx_wagtail_theme',  # Added here, no need to append separately
]

# Paths to templates
templates_path = ['_templates']

# Patterns to ignore when looking for source files
exclude_patterns = []

# Mapping for intersphinx (links to other documentation)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Source file suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Master document (source file without extension)
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
