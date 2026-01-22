# Documentation

This repo generates documentation for AoH Navigation Systems

Pages are written in [https://www.markdownguide.org/](MarkDown)

Each individual markdown page is hosted in doc/pages

The index (that the page creation tools use to create the output) and which lists the order to add MarkDown files is at doc/index.rst

The configuration is stored in doc/conf.py

Two actions run each time a file is committed:
1. Generate an HTML site in the style of ReadTheDocs and copy to [https://st599.github.io/ArielOfHamble-NavigationDocumentation/index.html](here)
2. Generate a PDF file and copy to /doc
