#!/usr/bin/python

from axmlparserpy import axmlprinter
from xml.dom import minidom
import sys

def main():
  ap = axmlprinter.AXMLPrinter(open(sys.argv[1], 'rb').read())
  buff = minidom.parseString(ap.getBuff()).toxml()
  print(buff)

if __name__ == "__main__":
  main()
