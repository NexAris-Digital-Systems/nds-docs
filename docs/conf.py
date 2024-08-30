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
    'sphinx_wagtail_theme',  
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

html_sidebars = {
    "**": [
        "searchbox.html",
        "about.html",
    ]
}

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = []
html_static_path = ['_static']
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
}

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
