import sys, re

body = open('mailbody.zhuww', 'r').read()
html = '''
<html>
    <head></head>
        <body>
''' + body.replace('\n', '<br>\n') + ''' 
        </body>
</html>'''
p = re.compile('(?P<code>arXiv:\d{4,4}\.\d{4,4})\s(?P<crosslist>\(.*\)\s)*\[(?P<files>.+)\]')
#p = re.compile('(?P<code>arXiv:\d{4,4}\.\d{4,4})')
def myreplace(match):
    code = match.group('code')
    files = match.group('files')
    codelink = '<a href="http://arxiv.org/abs/%s">%s</a>' % (code, code)
    p = re.compile('(?P<fmt>ps|pdf)')
    filelinks = p.sub('<a href="http://arxiv.gov/\g<fmt>/%s">\g<fmt></a>' % (code), files)
    if match.group('crosslist'):
        return codelink+' '+match.group('crosslist')+' ['+filelinks+']'
    else:
        return codelink+' ['+filelinks+']'
newhtml = p.sub(myreplace, html)
f = open('mailhtml.zhuww', 'w')
f.write(newhtml)
