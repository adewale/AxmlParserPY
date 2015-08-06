#!/usr/bin/python

from axmlparserpy import axmlprinter
from xml.dom import minidom

import sys
import axmlparserpy.apk

USAGE = """python apk_manifest.py PATH_TO_APK"""


def main():
  if len(sys.argv) != 2:
    print USAGE
    exit(1)

  filename = sys.argv[1]
  apk_file = axmlparserpy.apk.APK(filename)

  manifest_contents = apk_file.get_file("AndroidManifest.xml")


  ap = axmlprinter.AXMLPrinter(manifest_contents)
  buff = minidom.parseString(ap.getBuff()).toprettyxml()
  print(buff)

if __name__ == "__main__":
  main()
