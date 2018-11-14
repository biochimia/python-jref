import os
import textwrap

import jref.context
import jref.pointer

# All references are evaluated in a context, so start with one
ctx = jref.context.RemoteContext()

# Reference a remote document
spec = ctx.parse_reference('https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml')

# Reference portions of that document
spec_title = spec.context.parse_reference('#/info/title')
spec_version = spec.context.parse_reference('#/info/version')

# Print out the references, not the content (which hasn't been loaded)
print(textwrap.dedent('''
    * JSON References
    Spec:    {}
    Title:   {}
    Version: {}
    ''')
    .lstrip()
    .format(spec, spec_title, spec_version))

# Expand references, triggering loading of content
print(textwrap.dedent('''
    * Evaluated references
    Title:   {}
    Version: {}
    ''')
    .lstrip()
    .format(spec_title.expand(), spec_version.expand()))
