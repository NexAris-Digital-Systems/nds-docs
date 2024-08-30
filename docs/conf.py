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
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

html_theme_options = dict(
    project_name = "Crazy Development",
    logo = "https://cdn.crazydev.org/_data/i/upload/2024/08/29/20240829135605-1e4ae887-th.png",
    logo_alt = "crazydev",
    logo_height = 59,
    logo_url = "/",
    logo_width = 45,
)

# -- Options for HTML output -------------------------------------------------
extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'


# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
