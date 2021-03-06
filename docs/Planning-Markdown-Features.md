---
layout: docs
title: Planning> Markdown Features
---

Gist: Render markdown on the frontend using `marked`, but sanitize the input on the server before saving to the database.

- Basic, using <https://github.com/chjj/marked> or <https://github.com/lepture/mistune>
    - Inline HTML: **Not supported in full**, due to security issues.
        - Bleach: https://github.com/jsocol/bleach
        - Plain Python: http://stackoverflow.com/a/925630
        - BeautifulSoup: http://stackoverflow.com/a/699483
    - Headers: Support ATX and underline styles. Tell authors to prefer to skip H1.
    - Paragraphs & Linebreaks: GFM style, via `marked` or `mistune`.
    - Blockquotes: Support.
    - Lists: Fully supported.
    - Horizontal rules: Support.
    - Links: Support.
    - Emphasis: Supported for bold, underline.
    - Code: Support, GFM, via `marked` and `highlight.js` or with [`pygments`](http://pygments.org/).
    - Images: Support.
    - Backslash Escapes: Support.
- Extensions
    - Strikethrough: Supported, double tildes, via GFM `marked` or `mistune`.
    - GFM Tables: Support, via `marked` or `mistune`.
    - SmartyPants (Smart quotes, ellipse, dashes...): Support, via `marked`, but not `mistune`.
    - Inline TeX: Will support, via ???.
        - https://github.com/chjj/marked/pull/180
    - Footnotes: Will support, via ???.
        - https://github.com/chjj/marked/pull/351
    - Embedding: Will support, via ???. (Such as YouTube, Slideshare, etc.)
        - https://github.com/chjj/marked/pull/35
    - Citations / Bibliography: ???.
    - Definition Lists: Not supported.
    - Table of Contents: Not supported.
