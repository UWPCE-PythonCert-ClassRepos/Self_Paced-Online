#Test file for html_render.pytest

import pytest
from io import StringIO
from html_render import Element


def test_step1():
    el = Element()
    assert el.tag == 'html'
    assert el.indent == 0
    assert el.content == []
    
    el.append('hi')
    assert el.content == ['hi']
    el.append('bye')
    assert el.content == ['hi', 'bye']
    
    f = StringIO()
    el.render(f)
    assert f.getvalue() == ('<html>\n    hi\n    bye\n</html>')
    
    f = StringIO()
    el.render(f, 1)
    assert f.getvalue() == ('    <html>\n        hi\n        bye\n    </html>')
