# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

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

# Mapping for intersphinx (links to other documentation)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Paths to templates
templates_path = ['_templates']

# Source file suffixes
source_suffix = '.rst'

# Master document (source file without extension)
master_doc = 'index'

# Source directory
source_dir = 'docs/source'

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
