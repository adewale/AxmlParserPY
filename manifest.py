#!/usr/bin/python

from axmlparserpy import axmlprinter
from xml.dom import minidom

import sys
import axmlparserpy.apk

USAGE = """python manifest.py PATH_TO_APK"""


def main():
  if len(sys.argv) != 2:
    print USAGE
    exit(1)
  
  filename = sys.argv[1]
  apk_file = axmlparserpy.apk.APK(filename)

  manifest_contents = apk_file.raw_manifest

  buff = minidom.parseString(manifest_contents).toprettyxml()
  print(buff)

if __name__ == "__main__":
  main()
