# -- Project information -----------------------------------------------------
project = 'NexAris Digital Systems'
author = 'MrRamyg'
release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
html_show_sourcelink = False

html_favicon = "https://images.nexarisds.org/evidence/67281bb3775a1.jpg"
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


templates_path = ['_templates']
# -- Sidebar Buttons  -------------------------------------------------
html_sidebars = {
    '**': [
        'searchbox.html',
        'globaltoc.html',
    ]
}

master_doc = 'index'
exclude_patterns = []
html_css_files = [
    'custom.css',
]
html_last_updated_fmt = "%b %d, %Y"

html_theme = 'sphinx_wagtail_theme'
html_theme_options = {
    'project_name': "NexAris Digital Systems",
    'logo': "https://cdn.crazydev.org/_data/i/upload/2024/08/29/20240829135605-1e4ae887-th.png",
    'github_url': "https://github.com/NexAris-Digital-Systems/nds-docs/",
    'logo_alt': "nds",
    'logo_height': 59,
    'logo_width': 45,
    'logo_url': "/",}

html_context = {
    "display_github": False,
    "last_updated": True,
}

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
