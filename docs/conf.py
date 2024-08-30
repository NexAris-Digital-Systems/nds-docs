# -- Project information -----------------------------------------------------
project = 'Crazy Development'
author = 'MrRamyg'
release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_wagtail_theme',
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst',
}


templates_path = ['_sidebar_btemplates']
# -- Sidebar Buttons  -------------------------------------------------
html_sidebars = {"**": [
    "searchbox.html",
    "globaltoc.html",
    "./_sidebar_btemplates/about.html",   
]}


master_doc = 'index'
exclude_patterns = []
html_css_files = [
    'custom.css',
]
html_last_updated_fmt = "%b %d, %Y"

html_theme = 'sphinx_wagtail_theme'
html_theme_options = {
    'project_name': "Crazy Development",
    'logo': "/assets/logo.png",
    'github_url': "https://github.com/Crazy-Development/crazydev-docs",
    'logo_alt': "crazydev",
    'logo_height': 59,
    'logo_width': 45,
    'logo_url': "/",
    'header_links': "Crazydev - Blog |http://crazydev.org", }


# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
