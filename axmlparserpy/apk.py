# This file is part of Androguard.
#
# Copyright (C) 2010, Anthony Desnos <desnos at t0t0.fr>
# All rights reserved.
#
# Androguard is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Androguard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Androguard.  If not, see <http://www.gnu.org/licenses/>.
from axmlprinter import AXMLPrinter

import zipfile
try:
    import StringIO
except ImportError:
    from io import StringIO, BytesIO


class APK:
    """APK manages apk file format"""
    def __init__(self, filename):
        """
            @param filename: specify the path of the file, or raw data
        """

        fd = open(filename, "rb")
        self.__raw = fd.read()
        fd.close()

        try:
            self.zip = zipfile.ZipFile(StringIO.StringIO(self.__raw))
        except Exception:
            self.zip = zipfile.ZipFile(BytesIO(self.__raw))

        raw_manifest = AXMLPrinter(self.zip.read("AndroidManifest.xml")).getBuff()
        if 'xmlns:amazon="http://schemas.amazon.com/apk/res/android"' in raw_manifest:
            raw_manifest = raw_manifest.replace('xmlns:amazon="http://schemas.amazon.com/apk/res/android"', 'xmlns:android="http://schemas.android.com/apk/res/android" xmlns:amazon="http://schemas.amazon.com/apk/res/android"')
        self.raw_manifest = raw_manifest

