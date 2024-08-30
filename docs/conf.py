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
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'


# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
