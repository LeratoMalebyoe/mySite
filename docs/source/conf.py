import os
import sys
import django

# Add the project root (folder containing mySite) to Python path
sys.path.insert(0, os.path.abspath('../..'))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'mySite.settings'

# Setup Django
django.setup()

# -- Project information -----------------------------------------------------
project = 'mySite'
copyright = '2025, Lerato Malebyoe'
author = 'Lerato Malebyoe'
release = '2025'

# -- General configuration ---------------------------------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
exclude_patterns = []

language = 'English'

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
