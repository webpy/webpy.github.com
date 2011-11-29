"""Script to generate index.html files in /static/ folders.
"""

import web
import os, mimetypes

TMPL = """$def with (dirname, files)
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<title>Index of $dirname</title>
<style type="text/css">
a, a:active {text-decoration: none; color: blue;}
a:visited {color: #48468F;}
a:hover, a:focus {text-decoration: underline; color: red;}
body {background-color: #F5F5F5;}
h2 {margin-bottom: 12px;}
table {margin-left: 12px;}
th, td { font: 90% monospace; text-align: left;}
th { font-weight: bold; padding-right: 14px; padding-bottom: 3px;}
td {padding-right: 14px;}
td.s, th.s {text-align: right;}
div.list { background-color: white; border-top: 1px solid #646464; border-bottom: 1px solid #646464; padding-top: 10px; padding-bottom: 14px;}
div.foot { font: 90% monospace; color: #787878; padding-top: 4px;}
</style>
</head>
<body>
<h2>Index of $dirname</h2>
<div class="list">
<table summary="Directory Listing" cellpadding="0" cellspacing="0">
<thead><tr><th class="n">Name</th><th class="m">Last Modified</th><th class="s">Size</th><th class="t">Type</th></tr></thead>
<tbody>
<tr><td class="n"><a href="../">Parent Directory</a>/</td><td class="m">&nbsp;</td><td class="s">-</td><td class="t">Directory</td></tr>
$for f in files:
    $if f.type == "Directory":
        <tr><td class="n"><a href="$f.name/">$f.name</a>/</td><td class="m">$f.last_modified</td><td class="s">$f.size</td><td class="t">$f.type</td></tr>
    $else:
        <tr><td class="n"><a href="$f.name">$f.name</a></td><td class="m">$f.last_modified</td><td class="s">$f.size</td><td class="t">$f.type</td></tr>

</tbody>
</table>
</div>
<div class="foot"></div>
</body>
</html>"""

t = web.template.Template(TMPL)

def get_filetype(path):
    if os.path.isdir(path):
        return "Directory"
    else:
        return mimetypes.guess_type(path)[0]

def makeindex(dir):
    dirname = "/" + dir + "/"
    def makefile(f):
        return web.storage(
            name=f,
            last_modified="-",
            size="-",
            type=get_filetype(os.path.join(dir, f)),
        )
    files = [makefile(f) for f in os.listdir(dir)]
    files.sort(key=lambda f: (f.type != 'Directory', f.name))

    path = os.path.join(dir, "index.html")
    with open(path, "w") as f:
        html = str(t(dirname, files))
        f.write(html)
    print "generated", path

def main():
    makeindex("static")
    makeindex("static/css")
    makeindex("static/js")
    makeindex("static/images")

if __name__ == "__main__":
    main()
