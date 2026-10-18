#!/bin/bash
# Deploy with cache busting (same as the coffee site): rebuilds every lesson and the index,
# stamps one BUILD into every page's SITE_BUILD, every .pdf?v= link and version.json,
# then commits and pushes. Pages rebuilds in ~60s.
set -e
cd "$(dirname "$0")"
for f in lessons/*/lesson.py; do python3 "$f" >/dev/null; done
python3 build_index.py >/dev/null
B=$(date +%Y%m%d-%H%M%S)
python3 - "$B" <<'PY'
import re,sys,glob
b=sys.argv[1]
for p in ['index.html']+glob.glob('lessons/*/index.html'):
    s=open(p).read()
    s,n=re.subn(r"var SITE_BUILD='[^']*';", "var SITE_BUILD='%s';"%b, s)
    assert n==1, p+': SITE_BUILD missing'
    s=re.sub(r'(\.pdf)(\?v=[\w-]+)?(?=["\'])', r'\1?v='+b, s)
    open(p,'w').write(s)
open('version.json','w').write('{"build":"%s"}\n'%b)
PY
git add -A
git commit -qm "${1:-Update} (build $B)"
git push -q
echo "pushed build $B"
