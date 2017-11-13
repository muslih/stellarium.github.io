#!/usr/bin/python
# coding: utf-8

import glob
import re
import babel.messages
import babel.messages.pofile
import subprocess

# Update the file po/stellarium-website.pot from the source files

all_files = glob.glob('po/*.po')
for fn in all_files:
  lcode = re.match('po/(.*)\.po', fn).group(1)
  print "Generate locale stuff for " + lcode
  subprocess.call(["rm", "-r", "_i18n/" + lcode])
  subprocess.call(["cp", "-r", "_i18n/en", "_i18n/" + lcode])
  fout = open("_data/i18n/" + lcode + ".json", 'w')
  subprocess.call(["pojson", "po/" + lcode +".po", "-e", "utf-8"], stdout=fout)
