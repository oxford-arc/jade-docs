# -*- coding: utf-8 -*-
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))

# General information about the project.
project = u'JADE@ARC'
copyright = u'2017–%Y, University of Oxford — JADE Tier 2 Centre'
author = u'The ARC Team'

version = u''
release = u''

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_favicon',
]

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'jade'
html_theme_path = ['themes'] 
html_theme_options = {
    'version_selector': False,
    'language_selector': False,
}

# On RTD The custom theme is ignored so we must manually load all css files  
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'                              
if on_rtd:                                                                           
    html_context = {                                                             
        'css_files': [                                                           
            '_static/css/theme.css',            
            '_static/pygments.css',       
            '_static/customtheme.css',                                       
        ],                                                                       
    }

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = 'images/JADE_2.5_Logo.svg'

html_static_path = ['_static']
favicons = [
    {"href": "JADE_Icon.svg"},
]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'JADEARCdoc'

html_show_sphinx = False

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).

latex_documents = [
    (master_doc, 'JADE.tex', u'JADE Documentation',
     u'Mozhgan K. Chimeh', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'jade', u'JADE Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'JADE', u'JADE Documentation',
     author, 'JADE', 'One line description of project.',
     'Miscellaneous'),
]


#html_sidebars = { '**': ['globaltoc.html', 'localtoc.html', 'relations.html'], }
