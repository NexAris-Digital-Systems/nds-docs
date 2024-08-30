# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Crazy Development Docs'
author = 'MrRamyg'

release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',  
    'sphinx_wagtail_theme',  
]

templates_path = ['_templates']
exclude_patterns = []

# Mapping for intersphinx (links to other documentation)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Source file suffixes
source_suffix = '.md'

# Master document (source file without extension)
master_doc = 'index'

# Source directory
source_dir = 'docs/source'

# -- Options for HTML output -------------------------------------------------

extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
