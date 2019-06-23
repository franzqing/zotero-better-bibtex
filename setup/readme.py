#!/usr/bin/env python3

import re

with open('README.md') as f:
  readme = f.read()
warning = '<!-- WARNING: GENERATED FROM https://github.com/retorquere/zotero-better-bibtex/blob/master/README.md. EDITS WILL BE OVERWRITTEN -->'

index = f"""
---
title: Better BibTeX for Zotero
weight: 5
aliases:
  - /Home
---
{warning}
""".split('\n')

sponsoring = """
---
title: Sponsoring BBT
---
{warning}
""".split('\n')

appendto = index
for line in readme.split('\n'):
  if 'gitter' in line: continue
  if line.startswith('# ') and 'sponsor' in line.lower():
    appendto = sponsoring
    continue

  line = re.sub(r'\[!\[.*', '', line)

  appendto.append(line)

with open('site/content/_index.md', 'w') as f:
  print("\n".join(index), file=f)
with open('site/content/sponsoring.md', 'w') as f:
  print("\n".join(sponsoring), file=f)