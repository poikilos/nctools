#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Converts lines and arcs from a DXF file and prints them.
#
# Copyright © 2011,2012 R.F. Smith <rsmith@xs4all.nl>. All rights reserved.
# $Date$
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import sys 
import dxfgeom


__proginfo__ = ('readdxf [ver. ' + '$Revision$'[11:-2] +
                '] ('+'$Date$'[7:-2]+')')


def findentities(filename):
    """Get the entities from a file

    :filename: name of the file to read
    :returns: a 3-tuple of lists (contours, lines, arcs)
    """
    ent = dxfgeom.read_entities(filename)
    lo = dxfgeom.find_entities("LINE", ent)
    lines = []
    if len(lo) > 0:
        lines = [dxfgeom.line_from_elist(ent, n) for n in lo]
    ao = dxfgeom.find_entities("ARC", ent)
    arcs = []
    if len(ao) > 0:
        arcs = [dxfgeom.arc_from_elist(ent, m) for m in ao]
    return dxfgeom.find_contours(lines, arcs)
 

def main(argv):
    """Main program for the readdxf utility.
    
    :argv: command line arguments
    """
    if len(argv) == 1:
        print __proginfo__
        print "Usage: {} dxf-file(s)".format(sys.argv[0])
        exit(1)
    del argv[0]
    for f in argv:
        (contours, lines, arcs) = findentities(f) 
        # Sort in x1, then in y1.
        contours.sort()
        lines.sort()
        arcs.sort()
        # Output
        print "#File: {}".format(f)
        for c in contours:
            print c
        for l in lines:
            print l
        for a in arcs:
            print a


if __name__ == '__main__':
    main(sys.argv)

