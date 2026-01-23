# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ariel of Hamble Navigation'
copyright = 'BBCYC 2026'
author = 'Simon Thompson'
version = '0.2'
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx.ext.mathjax', 'sphinx_simplepdf']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'

html_static_path = ['_static']

# -- Options for PDF output -------------------------------------------------
# https://sphinx-simplepdf.readthedocs.io/en/latest/configuration.html

from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%Y%m%d")

simplepdf_file_name = "AoH-Navigation-v" + version + "-" + date_time +  ".pdf"
simplepdf_debug = True

