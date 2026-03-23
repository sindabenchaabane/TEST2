import html


html.escape("This is a test & only a test.")
# 'This is a test &amp; only a test.'
html.escape("This is a test & only a test.", quote=True)
# 'This is a test &amp; only a test.'
html.escape('This is a "test" & only a test.', quote=True)
# 'This is a &quot;test&quot; &amp; only a test.'
html.unescape('This is a &quot;test&quot; &amp; only a test.')
# 'This is a "test" & only a test.'



if __name__ == "__main__":
    import doctest

    doctest.testmod()   