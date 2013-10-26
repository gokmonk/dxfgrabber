# Created: 12.08.2012
# Copyright (C) 2012, Manfred Moitzi
# License: MIT-License
from __future__ import unicode_literals

import unittest

from io import StringIO

from dxfgrabber.drawing import Drawing

class TestDrawingDXF12withBlocks(unittest.TestCase):
    def setUp(self):
        stream = StringIO(DXF12)
        options = {
            'grab_blocks': True
        }
        self.dwg = Drawing(stream, options)

    def test_blocks(self):
        self.assertEqual(len(self.dwg.blocks), 8)

    def test_header_var(self):
        self.assertEqual(self.dwg.header['$ACADVER'], 'AC1009')

    def test_layers(self):
        self.assertEqual(len(self.dwg.layers), 5)

    def test_entities(self):
        self.assertEqual(len(self.dwg.entities), 1)

    def test_iter_entities(self):
        entities = list(self.dwg.entities)
        self.assertEqual(1, len(entities))

    def test_get_entity(self):
        self.assertEqual('INSERT', self.dwg.entities[0].dxftype)

    def test_modelspace(self):
        self.assertEqual(len(list(self.dwg.modelspace())), 1)

    def test_paperspace(self):
        self.assertEqual(len(list(self.dwg.paperspace())), 0)

class TestDrawingDXF12withoutBlocks(TestDrawingDXF12withBlocks):
    def setUp(self):
        stream = StringIO(DXF12)
        options = {
            'grab_blocks': False
        }
        self.dwg = Drawing(stream, options)

    def test_blocks(self):
        self.assertEqual(len(self.dwg.blocks), 0)

class TestDrawingDXF13withBlocks(unittest.TestCase):
    def setUp(self):
        stream = StringIO(DXF13)
        options = {
            'grab_blocks': True
        }
        self.dwg = Drawing(stream, options)

    def test_blocks(self):
        self.assertEqual(len(self.dwg.blocks), 5)

    def test_header_var(self):
        self.assertEqual(self.dwg.header['$ACADVER'], 'AC1024')

    def test_layers(self):
        self.assertEqual(len(self.dwg.layers), 3)

    def test_entities(self):
        self.assertEqual(len(self.dwg.entities), 2)

class TestDrawingDXF13withoutBlocks(TestDrawingDXF13withBlocks):
    def setUp(self):
        stream = StringIO(DXF13)
        options = {
            'grab_blocks': False
        }
        self.dwg = Drawing(stream, options)

    def test_blocks(self):
        self.assertEqual(len(self.dwg.blocks), 0)

DXF12 = """  0
SECTION
  2
HEADER
  9
$ACADVER
  1
AC1009
  9
$INSBASE
 10
0.0
 20
0.0
 30
0.0
  9
$EXTMIN
 10
25.640047515181092
 20
46.607903478102791
 30
0.0
  9
$EXTMAX
 10
107.700724762178
 20
103.37084827237931
 30
0.0
  9
$LIMMIN
 10
0.0
 20
0.0
  9
$LIMMAX
 10
12.0
 20
9.0
  9
$ORTHOMODE
 70
     0
  9
$REGENMODE
 70
     1
  9
$FILLMODE
 70
     1
  9
$QTEXTMODE
 70
     0
  9
$MIRRTEXT
 70
     0
  9
$DRAGMODE
 70
     2
  9
$LTSCALE
 40
1.0
  9
$OSMODE
 70
    37
  9
$ATTMODE
 70
     1
  9
$TEXTSIZE
 40
3.0
  9
$TRACEWID
 40
0.05
  9
$TEXTSTYLE
  7
NOTES
  9
$CLAYER
  8
0
  9
$CELTYPE
  6
BYLAYER
  9
$CECOLOR
 62
   256
  9
$DIMSCALE
 40
1.0
  9
$DIMASZ
 40
3.0
  9
$DIMEXO
 40
1.5
  9
$DIMDLI
 40
6.0
  9
$DIMRND
 40
0.0
  9
$DIMDLE
 40
0.0
  9
$DIMEXE
 40
3.0
  9
$DIMTP
 40
0.0
  9
$DIMTM
 40
0.0
  9
$DIMTXT
 40
3.0
  9
$DIMCEN
 40
3.0
  9
$DIMTSZ
 40
0.0
  9
$DIMTOL
 70
     0
  9
$DIMLIM
 70
     0
  9
$DIMTIH
 70
     0
  9
$DIMTOH
 70
     0
  9
$DIMSE1
 70
     0
  9
$DIMSE2
 70
     0
  9
$DIMTAD
 70
     1
  9
$DIMZIN
 70
     3
  9
$DIMBLK
  1

  9
$DIMASO
 70
     1
  9
$DIMSHO
 70
     1
  9
$DIMPOST
  1

  9
$DIMAPOST
  1

  9
$DIMALT
 70
     0
  9
$DIMALTD
 70
     2
  9
$DIMALTF
 40
25.399999999999999
  9
$DIMLFAC
 40
1.0
  9
$DIMTOFL
 70
     0
  9
$DIMTVP
 40
0.0
  9
$DIMTIX
 70
     0
  9
$DIMSOXD
 70
     0
  9
$DIMSAH
 70
     0
  9
$DIMBLK1
  1

  9
$DIMBLK2
  1

  9
$DIMSTYLE
  2
CIVIL-METRIC
  9
$DIMCLRD
 70
     0
  9
$DIMCLRE
 70
     0
  9
$DIMCLRT
 70
     0
  9
$DIMTFAC
 40
1.0
  9
$DIMGAP
 40
2.0
  9
$LUNITS
 70
     2
  9
$LUPREC
 70
     4
  9
$SKETCHINC
 40
0.1
  9
$FILLETRAD
 40
0.0
  9
$AUNITS
 70
     4
  9
$AUPREC
 70
     5
  9
$MENU
  1
.
  9
$ELEVATION
 40
0.0
  9
$PELEVATION
 40
0.0
  9
$THICKNESS
 40
0.0
  9
$LIMCHECK
 70
     0
  9
$BLIPMODE
 70
     0
  9
$CHAMFERA
 40
0.0
  9
$CHAMFERB
 40
0.0
  9
$SKPOLY
 70
     0
  9
$TDCREATE
 40
2455617.6962399771
  9
$TDUPDATE
 40
2455619.376983982
  9
$TDINDWG
 40
0.0047825347
  9
$TDUSRTIMER
 40
0.0047778125
  9
$USRTIMER
 70
     1
  9
$ANGBASE
 50
0.0
  9
$ANGDIR
 70
     0
  9
$PDMODE
 70
     0
  9
$PDSIZE
 40
0.0
  9
$PLINEWID
 40
0.0
  9
$COORDS
 70
     1
  9
$SPLFRAME
 70
     0
  9
$SPLINETYPE
 70
     6
  9
$SPLINESEGS
 70
     8
  9
$ATTDIA
 70
     0
  9
$ATTREQ
 70
     1
  9
$HANDLING
 70
     1
  9
$HANDSEED
  5
56C
  9
$SURFTAB1
 70
     6
  9
$SURFTAB2
 70
     6
  9
$SURFTYPE
 70
     6
  9
$SURFU
 70
     6
  9
$SURFV
 70
     6
  9
$UCSNAME
  2

  9
$UCSORG
 10
0.0
 20
0.0
 30
0.0
  9
$UCSXDIR
 10
1.0
 20
0.0
 30
0.0
  9
$UCSYDIR
 10
0.0
 20
1.0
 30
0.0
  9
$PUCSNAME
  2

  9
$PUCSORG
 10
0.0
 20
0.0
 30
0.0
  9
$PUCSXDIR
 10
1.0
 20
0.0
 30
0.0
  9
$PUCSYDIR
 10
0.0
 20
1.0
 30
0.0
  9
$USERI1
 70
     0
  9
$USERI2
 70
     0
  9
$USERI3
 70
     0
  9
$USERI4
 70
     0
  9
$USERI5
 70
     0
  9
$USERR1
 40
0.0
  9
$USERR2
 40
0.0
  9
$USERR3
 40
0.0
  9
$USERR4
 40
0.0
  9
$USERR5
 40
0.0
  9
$WORLDVIEW
 70
     1
  9
$SHADEDGE
 70
     3
  9
$SHADEDIF
 70
    70
  9
$TILEMODE
 70
     1
  9
$MAXACTVP
 70
    64
  9
$PLIMCHECK
 70
     0
  9
$PEXTMIN
 10
0.6288667663970601
 20
0.7999999523162842
 30
0.0
  9
$PEXTMAX
 10
9.0288663849273352
 20
7.1999995708465567
 30
0.0
  9
$PLIMMIN
 10
-0.7005418191744587
 20
-0.2281003861915408
  9
$PLIMMAX
 10
10.299457940529649
 20
8.2718993735125697
  9
$UNITMODE
 70
     0
  9
$VISRETAIN
 70
     1
  9
$PLINEGEN
 70
     0
  9
$PSLTSCALE
 70
     1
  0
ENDSEC
  0
SECTION
  2
TABLES
  0
TABLE
  2
VPORT
 70
     1
  0
VPORT
  2
*ACTIVE
 70
     0
 10
0.0
 20
0.0
 11
1.0
 21
1.0
 12
108.41536023058531
 22
104.9012768215983
 13
0.0
 23
0.0
 14
0.5
 24
0.5
 15
0.5
 25
0.5
 16
0.0
 26
0.0
 36
1.0
 17
0.0
 27
0.0
 37
0.0
 40
38.490099844867721
 41
2.1396648044692732
 42
50.0
 43
0.0
 44
0.0
 50
0.0
 51
0.0
 71
     0
 72
  1000
 73
     1
 74
     3
 75
     0
 76
     0
 77
     0
 78
     0
  0
ENDTAB
  0
TABLE
  2
LTYPE
 70
     5
  0
LTYPE
  2
CONTINUOUS
 70
     0
  3
Solid line
 72
    65
 73
     0
 40
0.0
  0
LTYPE
  2
CENTER
 70
     0
  3
Center ____ _ ____ _ ____ _ ____ _ ____ _ ____
 72
    65
 73
     4
 40
2.0
 49
1.25
 49
-0.25
 49
0.25
 49
-0.25
  0
LTYPE
  2
DASHED
 70
     0
  3
Dashed __ __ __ __ __ __ __ __ __ __ __ __ __ _
 72
    65
 73
     2
 40
0.75
 49
0.5
 49
-0.25
  0
LTYPE
  2
PHANTOM
 70
     0
  3
Phantom ______  __  __  ______  __  __  ______
 72
    65
 73
     6
 40
2.5
 49
1.25
 49
-0.25
 49
0.25
 49
-0.25
 49
0.25
 49
-0.25
  0
LTYPE
  2
HIDDEN
 70
     0
  3
Hidden __ __ __ __ __ __ __ __ __ __ __ __ __ __
 72
    65
 73
     2
 40
9.5249999999999986
 49
6.3499999999999979
 49
-3.174999999999998
  0
ENDTAB
  0
TABLE
  2
LAYER
 70
     5
  0
LAYER
  2
0
 70
     0
 62
     7
  6
CONTINUOUS
  0
LAYER
  2
VIEW_PORT
 70
     0
 62
     7
  6
CONTINUOUS
  0
LAYER
  2
DEFPOINTS
 70
     0
 62
     7
  6
CONTINUOUS
  0
LAYER
  2
0___1
 70
     0
 62
     7
  6
CONTINUOUS
  0
LAYER
  2
0___10
 70
     0
 62
     7
  6
CONTINUOUS
  0
ENDTAB
  0
TABLE
  2
STYLE
 70
     5
  0
STYLE
  2
STANDARD
 70
     0
 40
0.0
 41
1.0
 50
0.0
 71
     0
 42
0.2
  3
txt
  4

  0
STYLE
  2
ANNOTATIVE
 70
     0
 40
0.0
 41
1.0
 50
0.0
 71
     0
 42
0.2
  3
txt
  4

  0
STYLE
  2
NOTES
 70
     0
 40
3.0
 41
1.0
 50
0.0
 71
     0
 42
3.0
  3
txt
  4

  0
STYLE
  2
TITLES
 70
     0
 40
6.0
 41
1.0
 50
0.0
 71
     0
 42
0.2
  3
txt
  4

  0
STYLE
  2

 70
     1
 40
0.0
 41
1.0
 50
0.0
 71
     0
 42
0.2
  3
ltypeshp.shx
  4

  0
ENDTAB
  0
TABLE
  2
VIEW
 70
     0
  0
ENDTAB
  0
TABLE
  2
UCS
 70
     0
  0
ENDTAB
  0
TABLE
  2
APPID
 70
    14
  0
APPID
  2
ACAD
 70
     0
  0
APPID
  2
ACADANNOTATIVE
 70
     0
  0
APPID
  2
ACADANNOPO
 70
     0
  0
APPID
  2
ACAD_DSTYLE_DIMJAG
 70
     0
  0
APPID
  2
ACAD_DSTYLE_DIMTALN
 70
     0
  0
APPID
  2
ACAD_MLEADERVER
 70
     0
  0
APPID
  2
ACAECLAYERSTANDARD
 70
     0
  0
APPID
  2
ACAD_EXEMPT_FROM_CAD_STANDARDS
 70
     0
  0
APPID
  2
ACAD_DSTYLE_DIMBREAK
 70
     0
  0
APPID
  2
ACAD_PSEXT
 70
     0
  0
APPID
  2
ACADANNOTATIVEDECOMPOSITION
 70
     0
  0
APPID
  2
ACADANNOTATIVEATTRIBUTEDEC
 70
     0
  0
APPID
  2
CONTENTBLOCKICON
 70
     0
  0
APPID
  2
ACADANNOTATIVEATTRIBUTEDE0
 70
     0
  0
ENDTAB
  0
TABLE
  2
DIMSTYLE
 70
     3
  0
DIMSTYLE
  2
STANDARD
 70
     0
  3

  4

  5

  6

  7

 40
1.0
 41
3.0
 42
2.0
 43
9.0
 44
5.0
 45
0.0
 46
0.0
 47
0.0
 48
0.0
140
3.0
141
2.0
142
0.0
143
25.399999999999999
144
1.0
145
0.0
146
1.0
147
2.0
 71
     0
 72
     0
 73
     1
 74
     1
 75
     0
 76
     0
 77
     0
 78
     0
170
     0
171
     2
172
     0
173
     0
174
     0
175
     0
176
     0
177
     0
178
     0
  0
DIMSTYLE
  2
ANNOTATIVE
 70
     0
  3

  4

  5

  6

  7

 40
0.0
 41
3.0
 42
2.5
 43
10.0
 44
5.0
 45
0.0
 46
0.0
 47
0.0
 48
0.0
140
3.0
141
2.0
142
0.0
143
25.399999999999999
144
1.0
145
0.0
146
1.0
147
2.0
 71
     0
 72
     0
 73
     1
 74
     1
 75
     0
 76
     0
 77
     0
 78
     0
170
     0
171
     2
172
     0
173
     0
174
     0
175
     0
176
     0
177
     0
178
     0
  0
DIMSTYLE
  2
CIVIL-METRIC
 70
     0
  3

  4

  5

  6

  7

 40
1.0
 41
3.0
 42
1.5
 43
6.0
 44
3.0
 45
0.0
 46
0.0
 47
0.0
 48
0.0
140
3.0
141
3.0
142
0.0
143
25.399999999999999
144
1.0
145
0.0
146
1.0
147
2.0
 71
     0
 72
     0
 73
     0
 74
     0
 75
     0
 76
     0
 77
     1
 78
     3
170
     0
171
     2
172
     0
173
     0
174
     0
175
     0
176
     0
177
     0
178
     0
  0
ENDTAB
  0
ENDSEC
  0
SECTION
  2
BLOCKS
  0
BLOCK
  8
0
  2
$MODEL_SPACE
 70
     0
 10
0.0
 20
0.0
 30
0.0
  3
$MODEL_SPACE
  1

  0
ENDBLK
  5
4CF
  8
0
  0
BLOCK
 67
     1
  8
0
  2
$PAPER_SPACE
 70
     0
 10
0.0
 20
0.0
 30
0.0
  3
$PAPER_SPACE
  1

  0
ENDBLK
  5
4CB
 67
     1
  8
0
  0
BLOCK
  8
0
  2
_ARCHTICK
 70
     0
 10
0.0
 20
0.0
 30
0.0
  3
_ARCHTICK
  1

  0
POLYLINE
  5
239
  8
0
  6
BYBLOCK
 62
     0
 66
     1
 10
0.0
 20
0.0
 30
0.0
 40
0.15
 41
0.15
  0
VERTEX
  5
52B
  8
0
  6
BYBLOCK
 62
     0
 10
-0.5
 20
-0.5
 30
0.0
  0
VERTEX
  5
52C
  8
0
  6
BYBLOCK
 62
     0
 10
0.5
 20
0.5
 30
0.0
  0
SEQEND
  5
52D
  8
0
  6
BYBLOCK
 62
     0
  0
ENDBLK
  5
23B
  8
0
  0
BLOCK
  8
0
  2
_OPEN30
 70
     0
 10
0.0
 20
0.0
 30
0.0
  3
_OPEN30
  1

  0
LINE
  5
23D
  8
0
  6
BYBLOCK
 62
     0
 10
-1.0
 20
0.26794919
 30
0.0
 11
0.0
 21
0.0
 31
0.0
  0
LINE
  5
23E
  8
0
  6
BYBLOCK
 62
     0
 10
0.0
 20
0.0
 30
0.0
 11
-1.0
 21
-0.26794919
 31
0.0
  0
LINE
  5
23F
  8
0
  6
BYBLOCK
 62
     0
 10
0.0
 20
0.0
 30
0.0
 11
-1.0
 21
0.0
 31
0.0
  0
ENDBLK
  5
241
  8
0
  0
BLOCK
  8
0
  2
TESTBLOCK1
 70
     2
 10
0.0
 20
0.0
 30
0.0
  3
TESTBLOCK1
  1

  0
POLYLINE
  5
3D9
  8
0
 66
     1
 10
0.0
 20
0.0
 30
0.0
 70
     1
  0
VERTEX
  5
532
  8
0
 10
25.640047515181092
 20
57.311229467739082
 30
0.0
  0
VERTEX
  5
533
  8
0
 10
30.868023232803921
 20
57.311229467739082
 30
0.0
  0
VERTEX
  5
534
  8
0
 10
30.868023232803921
 20
54.201189025262387
 30
0.0
  0
VERTEX
  5
535
  8
0
 10
25.640047515181092
 20
54.201189025262387
 30
0.0
  0
SEQEND
  5
536
  8
0
  0
ATTDEF
  5
3DA
  8
0
 10
32.859632986017751
 20
54.201189025262387
 30
0.0
 40
3.0
  1
xxx
  7
NOTES
  3
Testeingabe
  2
TEST
 70
     0
1001
ACADANNOTATIVE
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
1001
ACADANNOPO
1070
     1
  0
ENDBLK
  5
3D8
  8
0
  0
BLOCK
  8
0
  2
*U5
 70
     1
 10
0.0
 20
0.0
 30
0.0
  3
*U5
  1

  0
INSERT
  5
3F5
  8
0
 66
     1
  2
TESTBLOCK1
 10
0.0
 20
0.0
 30
0.0
  0
ATTRIB
  5
3F6
  8
0___1
 10
32.859632986017751
 20
54.201189025262387
 30
0.0
 40
3.0
  1
xxx
  7
NOTES
  2
TEST
 70
     0
1001
ACADANNOPO
1070
     1
1001
ACADANNOTATIVE
1000
AnnotativeData
1002
{
1070
     1
1070
     0
1002
}
  0
SEQEND
  5
3FB
  8
0
  0
ENDBLK
  5
3F4
  8
0
  0
BLOCK
  8
0
  2
*U6
 70
     1
 10
0.0
 20
0.0
 30
0.0
  3
*U6
  1

  0
INSERT
  5
405
  8
0
 66
     1
  2
TESTBLOCK1
 10
0.0
 20
-6.593285547159609
 30
0.0
  0
ATTRIB
  5
406
  8
0___1
 10
32.859632986017751
 20
47.607903478102799
 30
0.0
 40
3.0
  1
yyy
  7
NOTES
  2
TEST
 70
     0
1001
ACADANNOPO
1070
     1
1001
ACADANNOTATIVE
1000
AnnotativeData
1002
{
1070
     1
1070
     0
1002
}
  0
SEQEND
  5
40B
  8
0
  0
ENDBLK
  5
404
  8
0
  0
BLOCK
  8
0
  2
*U7
 70
     1
 10
0.0
 20
0.0
 30
0.0
  3
*U7
  1

  0
INSERT
  5
51D
  8
0
 66
     1
  2
TESTBLOCK1
 10
66.841091776160255
 20
46.059618804640209
 30
0.0
  0
ATTRIB
  5
51E
  8
0___10
 10
99.700724762178012
 20
100.2608078299026
 30
0.0
 40
3.0
  1
aaa
  7
NOTES
  2
TEST
 70
     0
1001
ACADANNOPO
1070
     1
1001
ACADANNOTATIVE
1000
AnnotativeData
1002
{
1070
     1
1070
     0
1002
}
  0
SEQEND
  5
523
  8
0
  0
ENDBLK
  5
51C
  8
0
  0
ENDSEC
  0
SECTION
  2
ENTITIES
  0
INSERT
  5
503
  8
0
  2
*U7
 10
0.0
 20
0.0
 30
0.0
1001
ACADANNOTATIVEATTRIBUTEDE0
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
  0
VIEWPORT
  5
28B
 67
     1
  8
0
 10
4.7994580606775941
 20
4.0218994936605128
 30
0.0
 40
17.88061277576319
 41
8.9929997457669462
 68
     1
 69
     1
1001
ACAD
1000
MVIEW
1002
{
1070
    16
1010
0.0
1020
0.0
1030
0.0
1010
0.0
1020
0.0
1030
1.0
1040
0.0
1040
8.9929997457669462
1040
4.7994580606775941
1040
4.0218994936605128
1040
50.0
1040
0.0
1040
0.0
1070
     0
1070
  1000
1070
     1
1070
     1
1070
     0
1070
     0
1070
     0
1070
     0
1040
0.0
1040
0.0
1040
0.0
1040
0.5
1040
0.5
1040
0.5
1040
0.5
1070
     0
1002
{
1002
}
1002
}
  0
VIEWPORT
  5
290
 67
     1
  8
VIEW_PORT
 10
4.8288665756621958
 20
3.99999976158142
 30
0.0
 40
8.3999996185302752
 41
6.3999996185302734
 68
     2
 69
     2
1001
ACAD
1000
MVIEW
1002
{
1070
    16
1010
0.0
1020
0.0
1030
0.0
1010
0.0
1020
0.0
1030
1.0
1040
0.0
1040
6.3999996185302734
1040
6.0
1040
4.5
1040
50.0
1040
0.0
1040
0.0
1070
     0
1070
  1000
1070
     1
1070
     3
1070
     0
1070
     0
1070
     0
1070
     0
1040
0.0
1040
0.0
1040
0.0
1040
0.5
1040
0.5
1040
0.5
1040
0.5
1070
     0
1002
{
1002
}
1002
}
  0
ENDSEC
  0
EOF
"""

DXF13 = """  0
SECTION
  2
HEADER
  9
$ACADVER
  1
AC1024
  9
$ACADMAINTVER
 70
     6
  9
$DWGCODEPAGE
  3
ANSI_1252
  9
$LASTSAVEDBY
  1
manfred
  9
$INSBASE
 10
0.0
 20
0.0
 30
0.0
  9
$EXTMIN
 10
25.6400475151811
 20
46.7197725094807
 30
0.0
  9
$EXTMAX
 10
43.57041061221146
 20
57.99518629674945
 30
0.0
  9
$LIMMIN
 10
0.0
 20
0.0
  9
$LIMMAX
 10
12.0
 20
9.0
  9
$ORTHOMODE
 70
     0
  9
$REGENMODE
 70
     1
  9
$FILLMODE
 70
     1
  9
$QTEXTMODE
 70
     0
  9
$MIRRTEXT
 70
     0
  9
$LTSCALE
 40
1.0
  9
$ATTMODE
 70
     1
  9
$TEXTSIZE
 40
3.0
  9
$TRACEWID
 40
0.05
  9
$TEXTSTYLE
  7
Notes
  9
$CLAYER
  8
0
  9
$CELTYPE
  6
ByLayer
  9
$CECOLOR
 62
   256
  9
$CELTSCALE
 40
1.0
  9
$DISPSILH
 70
     0
  9
$DIMSCALE
 40
1.0
  9
$DIMASZ
 40
3.0
  9
$DIMEXO
 40
1.5
  9
$DIMDLI
 40
6.0
  9
$DIMRND
 40
0.0
  9
$DIMDLE
 40
0.0
  9
$DIMEXE
 40
3.0
  9
$DIMTP
 40
0.0
  9
$DIMTM
 40
0.0
  9
$DIMTXT
 40
3.0
  9
$DIMCEN
 40
3.0
  9
$DIMTSZ
 40
0.0
  9
$DIMTOL
 70
     0
  9
$DIMLIM
 70
     0
  9
$DIMTIH
 70
     0
  9
$DIMTOH
 70
     0
  9
$DIMSE1
 70
     0
  9
$DIMSE2
 70
     0
  9
$DIMTAD
 70
     1
  9
$DIMZIN
 70
     3
  9
$DIMBLK
  1

  9
$DIMASO
 70
     1
  9
$DIMSHO
 70
     1
  9
$DIMPOST
  1

  9
$DIMAPOST
  1

  9
$DIMALT
 70
     0
  9
$DIMALTD
 70
     2
  9
$DIMALTF
 40
25.4
  9
$DIMLFAC
 40
1.0
  9
$DIMTOFL
 70
     0
  9
$DIMTVP
 40
0.0
  9
$DIMTIX
 70
     0
  9
$DIMSOXD
 70
     0
  9
$DIMSAH
 70
     0
  9
$DIMBLK1
  1

  9
$DIMBLK2
  1

  9
$DIMSTYLE
  2
Civil-Metric
  9
$DIMCLRD
 70
     0
  9
$DIMCLRE
 70
     0
  9
$DIMCLRT
 70
     0
  9
$DIMTFAC
 40
1.0
  9
$DIMGAP
 40
2.0
  9
$DIMJUST
 70
     0
  9
$DIMSD1
 70
     0
  9
$DIMSD2
 70
     0
  9
$DIMTOLJ
 70
     1
  9
$DIMTZIN
 70
     0
  9
$DIMALTZ
 70
     0
  9
$DIMALTTZ
 70
     0
  9
$DIMUPT
 70
     0
  9
$DIMDEC
 70
     2
  9
$DIMTDEC
 70
     2
  9
$DIMALTU
 70
     2
  9
$DIMALTTD
 70
     2
  9
$DIMTXSTY
  7
Standard
  9
$DIMAUNIT
 70
     0
  9
$DIMADEC
 70
     2
  9
$DIMALTRND
 40
0.0
  9
$DIMAZIN
 70
     2
  9
$DIMDSEP
 70
    46
  9
$DIMATFIT
 70
     3
  9
$DIMFRAC
 70
     1
  9
$DIMLDRBLK
  1

  9
$DIMLUNIT
 70
     2
  9
$DIMLWD
 70
    -2
  9
$DIMLWE
 70
    -2
  9
$DIMTMOVE
 70
     0
  9
$DIMFXL
 40
1.0
  9
$DIMFXLON
 70
     0
  9
$DIMJOGANG
 40
0.7853981633974483
  9
$DIMTFILL
 70
     0
  9
$DIMTFILLCLR
 70
     0
  9
$DIMARCSYM
 70
     0
  9
$DIMLTYPE
  6

  9
$DIMLTEX1
  6

  9
$DIMLTEX2
  6

  9
$DIMTXTDIRECTION
 70
     0
  9
$LUNITS
 70
     2
  9
$LUPREC
 70
     4
  9
$SKETCHINC
 40
0.1
  9
$FILLETRAD
 40
0.0
  9
$AUNITS
 70
     4
  9
$AUPREC
 70
     5
  9
$MENU
  1
.
  9
$ELEVATION
 40
0.0
  9
$PELEVATION
 40
0.0
  9
$THICKNESS
 40
0.0
  9
$LIMCHECK
 70
     0
  9
$CHAMFERA
 40
0.0
  9
$CHAMFERB
 40
0.0
  9
$CHAMFERC
 40
0.0
  9
$CHAMFERD
 40
0.0
  9
$SKPOLY
 70
     0
  9
$TDCREATE
 40
2455617.696239977
  9
$TDUCREATE
 40
2455617.654573310
  9
$TDUPDATE
 40
2455617.699600544
  9
$TDUUPDATE
 40
2455617.657933877
  9
$TDINDWG
 40
0.0033621065
  9
$TDUSRTIMER
 40
0.0033606250
  9
$USRTIMER
 70
     1
  9
$ANGBASE
 50
0.0
  9
$ANGDIR
 70
     0
  9
$PDMODE
 70
     0
  9
$PDSIZE
 40
0.0
  9
$PLINEWID
 40
0.0
  9
$SPLFRAME
 70
     0
  9
$SPLINETYPE
 70
     6
  9
$SPLINESEGS
 70
     8
  9
$HANDSEED
  5
45A
  9
$SURFTAB1
 70
     6
  9
$SURFTAB2
 70
     6
  9
$SURFTYPE
 70
     6
  9
$SURFU
 70
     6
  9
$SURFV
 70
     6
  9
$UCSBASE
  2

  9
$UCSNAME
  2

  9
$UCSORG
 10
0.0
 20
0.0
 30
0.0
  9
$UCSXDIR
 10
1.0
 20
0.0
 30
0.0
  9
$UCSYDIR
 10
0.0
 20
1.0
 30
0.0
  9
$UCSORTHOREF
  2

  9
$UCSORTHOVIEW
 70
     0
  9
$UCSORGTOP
 10
0.0
 20
0.0
 30
0.0
  9
$UCSORGBOTTOM
 10
0.0
 20
0.0
 30
0.0
  9
$UCSORGLEFT
 10
0.0
 20
0.0
 30
0.0
  9
$UCSORGRIGHT
 10
0.0
 20
0.0
 30
0.0
  9
$UCSORGFRONT
 10
0.0
 20
0.0
 30
0.0
  9
$UCSORGBACK
 10
0.0
 20
0.0
 30
0.0
  9
$PUCSBASE
  2

  9
$PUCSNAME
  2

  9
$PUCSORG
 10
0.0
 20
0.0
 30
0.0
  9
$PUCSXDIR
 10
1.0
 20
0.0
 30
0.0
  9
$PUCSYDIR
 10
0.0
 20
1.0
 30
0.0
  9
$PUCSORTHOREF
  2

  9
$PUCSORTHOVIEW
 70
     0
  9
$PUCSORGTOP
 10
0.0
 20
0.0
 30
0.0
  9
$PUCSORGBOTTOM
 10
0.0
 20
0.0
 30
0.0
  9
$PUCSORGLEFT
 10
0.0
 20
0.0
 30
0.0
  9
$PUCSORGRIGHT
 10
0.0
 20
0.0
 30
0.0
  9
$PUCSORGFRONT
 10
0.0
 20
0.0
 30
0.0
  9
$PUCSORGBACK
 10
0.0
 20
0.0
 30
0.0
  9
$USERI1
 70
     0
  9
$USERI2
 70
     0
  9
$USERI3
 70
     0
  9
$USERI4
 70
     0
  9
$USERI5
 70
     0
  9
$USERR1
 40
0.0
  9
$USERR2
 40
0.0
  9
$USERR3
 40
0.0
  9
$USERR4
 40
0.0
  9
$USERR5
 40
0.0
  9
$WORLDVIEW
 70
     1
  9
$SHADEDGE
 70
     3
  9
$SHADEDIF
 70
    70
  9
$TILEMODE
 70
     1
  9
$MAXACTVP
 70
    64
  9
$PINSBASE
 10
0.0
 20
0.0
 30
0.0
  9
$PLIMCHECK
 70
     0
  9
$PEXTMIN
 10
0.62886676639706
 20
0.7999999523162842
 30
0.0
  9
$PEXTMAX
 10
9.028866384927335
 20
7.199999570846558
 30
0.0
  9
$PLIMMIN
 10
-0.7005418191744587
 20
-0.2281003861915408
  9
$PLIMMAX
 10
10.29945794052965
 20
8.271899373512569
  9
$UNITMODE
 70
     0
  9
$VISRETAIN
 70
     1
  9
$PLINEGEN
 70
     0
  9
$PSLTSCALE
 70
     1
  9
$TREEDEPTH
 70
  3020
  9
$CMLSTYLE
  2
Standard
  9
$CMLJUST
 70
     0
  9
$CMLSCALE
 40
1.0
  9
$PROXYGRAPHICS
 70
     1
  9
$MEASUREMENT
 70
     1
  9
$CELWEIGHT
370
    -1
  9
$ENDCAPS
280
     0
  9
$JOINSTYLE
280
     0
  9
$LWDISPLAY
290
     0
  9
$INSUNITS
 70
     4
  9
$HYPERLINKBASE
  1

  9
$STYLESHEET
  1

  9
$XEDIT
290
     1
  9
$CEPSNTYPE
380
     0
  9
$PSTYLEMODE
290
     1
  9
$FINGERPRINTGUID
  2
{839630CB-8D74-430B-BAEB-14BEBC39A98E}
  9
$VERSIONGUID
  2
{DA208811-7EC4-4225-A192-688F9D4AC7E6}
  9
$EXTNAMES
290
     1
  9
$PSVPSCALE
 40
0.0
  9
$OLESTARTUP
290
     0
  9
$SORTENTS
280
   127
  9
$INDEXCTL
280
     0
  9
$HIDETEXT
280
     1
  9
$XCLIPFRAME
280
     0
  9
$HALOGAP
280
     0
  9
$OBSCOLOR
 70
   257
  9
$OBSLTYPE
280
     0
  9
$INTERSECTIONDISPLAY
280
     0
  9
$INTERSECTIONCOLOR
 70
   257
  9
$DIMASSOC
280
     2
  9
$PROJECTNAME
  1

  9
$CAMERADISPLAY
290
     0
  9
$LENSLENGTH
 40
50.0
  9
$CAMERAHEIGHT
 40
0.0
  9
$STEPSPERSEC
 40
2.0
  9
$STEPSIZE
 40
6.0
  9
$3DDWFPREC
 40
2.0
  9
$PSOLWIDTH
 40
0.25
  9
$PSOLHEIGHT
 40
4.0
  9
$LOFTANG1
 40
1.570796326794896
  9
$LOFTANG2
 40
1.570796326794896
  9
$LOFTMAG1
 40
0.0
  9
$LOFTMAG2
 40
0.0
  9
$LOFTPARAM
 70
     7
  9
$LOFTNORMALS
280
     1
  9
$LATITUDE
 40
37.795
  9
$LONGITUDE
 40
-122.394
  9
$NORTHDIRECTION
 40
0.0
  9
$TIMEZONE
 70
 -8000
  9
$LIGHTGLYPHDISPLAY
280
     1
  9
$TILEMODELIGHTSYNCH
280
     1
  9
$CMATERIAL
347
96
  9
$SOLIDHIST
280
     1
  9
$SHOWHIST
280
     1
  9
$DWFFRAME
280
     2
  9
$DGNFRAME
280
     0
  9
$REALWORLDSCALE
290
     1
  9
$INTERFERECOLOR
 62
     1
  9
$INTERFEREOBJVS
345
A3
  9
$INTERFEREVPVS
346
A0
  9
$CSHADOW
280
     0
  9
$SHADOWPLANELOCATION
 40
0.0
  0
ENDSEC
  0
SECTION
  2
CLASSES
  0
CLASS
  1
ACDBDICTIONARYWDFLT
  2
AcDbDictionaryWithDefault
  3
ObjectDBX Classes
 90
        0
 91
        1
280
     0
281
     0
  0
CLASS
  1
DICTIONARYVAR
  2
AcDbDictionaryVar
  3
ObjectDBX Classes
 90
        0
 91
       13
280
     0
281
     0
  0
CLASS
  1
TABLESTYLE
  2
AcDbTableStyle
  3
ObjectDBX Classes
 90
     4095
 91
        1
280
     0
281
     0
  0
CLASS
  1
MATERIAL
  2
AcDbMaterial
  3
ObjectDBX Classes
 90
     1153
 91
        3
280
     0
281
     0
  0
CLASS
  1
VISUALSTYLE
  2
AcDbVisualStyle
  3
ObjectDBX Classes
 90
     4095
 91
       19
280
     0
281
     0
  0
CLASS
  1
SCALE
  2
AcDbScale
  3
ObjectDBX Classes
 90
     1153
 91
       17
280
     0
281
     0
  0
CLASS
  1
MLEADERSTYLE
  2
AcDbMLeaderStyle
  3
ACDB_MLEADERSTYLE_CLASS
 90
     4095
 91
        3
280
     0
281
     0
  0
CLASS
  1
CELLSTYLEMAP
  2
AcDbCellStyleMap
  3
ObjectDBX Classes
 90
     1152
 91
        2
280
     0
281
     0
  0
CLASS
  1
EXACXREFPANELOBJECT
  2
ExAcXREFPanelObject
  3
EXAC_ESW
 90
     1025
 91
        0
280
     0
281
     0
  0
CLASS
  1
NPOCOLLECTION
  2
AcDbImpNonPersistentObjectsCollection
  3
ObjectDBX Classes
 90
     1153
 91
        0
280
     0
281
     0
  0
CLASS
  1
LAYER_INDEX
  2
AcDbLayerIndex
  3
ObjectDBX Classes
 90
        0
 91
        0
280
     0
281
     0
  0
CLASS
  1
SPATIAL_INDEX
  2
AcDbSpatialIndex
  3
ObjectDBX Classes
 90
        0
 91
        0
280
     0
281
     0
  0
CLASS
  1
IDBUFFER
  2
AcDbIdBuffer
  3
ObjectDBX Classes
 90
        0
 91
        0
280
     0
281
     0
  0
CLASS
  1
DIMASSOC
  2
AcDbDimAssoc
  3
"AcDbDimAssoc|Product Desc:     AcDim ARX App For Dimension|Company:          Autodesk, Inc.|WEB Address:      www.autodesk.com"
 90
        0
 91
        0
280
     0
281
     0
  0
CLASS
  1
ACDB_MTEXTATTRIBUTEOBJECTCONTEXTDATA_CLASS
  2
AcDbMTextAttributeObjectContextData
  3
ObjectDBX Classes
 90
     1153
 91
        6
280
     0
281
     0
  0
ENDSEC
  0
SECTION
  2
TABLES
  0
TABLE
  2
VPORT
  5
8
330
0
100
AcDbSymbolTable
 70
     1
  0
VPORT
  5
94
330
8
100
AcDbSymbolTableRecord
100
AcDbViewportTableRecord
  2
*Active
 70
     0
 10
0.0
 20
0.0
 11
1.0
 21
1.0
 12
68.7397286580374
 22
40.61031242579786
 13
0.0
 23
0.0
 14
0.5
 24
0.5
 15
0.5
 25
0.5
 16
0.0
 26
0.0
 36
1.0
 17
0.0
 27
0.0
 37
0.0
 40
55.73192435061998
 41
2.139664804469273
 42
50.0
 43
0.0
 44
0.0
 50
0.0
 51
0.0
 71
     0
 72
  1000
 73
     1
 74
     3
 75
     0
 76
     0
 77
     0
 78
     0
281
     0
 65
     1
110
0.0
120
0.0
130
0.0
111
1.0
121
0.0
131
0.0
112
0.0
122
1.0
132
0.0
 79
     0
146
0.0
348
9F
 60
     2
 61
     5
292
     1
282
     1
141
0.0
142
0.0
 63
   250
421
  3355443
  0
ENDTAB
  0
TABLE
  2
LTYPE
  5
5
330
0
100
AcDbSymbolTable
 70
     5
  0
LTYPE
  5
14
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
ByBlock
 70
     0
  3

 72
    65
 73
     0
 40
0.0
  0
LTYPE
  5
15
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
ByLayer
 70
     0
  3

 72
    65
 73
     0
 40
0.0
  0
LTYPE
  5
16
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
Continuous
 70
     0
  3
Solid line
 72
    65
 73
     0
 40
0.0
  0
LTYPE
  5
1B1
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
CENTER
 70
     0
  3
Center ____ _ ____ _ ____ _ ____ _ ____ _ ____
 72
    65
 73
     4
 40
2.0
 49
1.25
 74
     0
 49
-0.25
 74
     0
 49
0.25
 74
     0
 49
-0.25
 74
     0
  0
LTYPE
  5
1B2
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
DASHED
 70
     0
  3
Dashed __ __ __ __ __ __ __ __ __ __ __ __ __ _
 72
    65
 73
     2
 40
0.75
 49
0.5
 74
     0
 49
-0.25
 74
     0
  0
LTYPE
  5
1B3
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
PHANTOM
 70
     0
  3
Phantom ______  __  __  ______  __  __  ______
 72
    65
 73
     6
 40
2.5
 49
1.25
 74
     0
 49
-0.25
 74
     0
 49
0.25
 74
     0
 49
-0.25
 74
     0
 49
0.25
 74
     0
 49
-0.25
 74
     0
  0
LTYPE
  5
39E
330
5
100
AcDbSymbolTableRecord
100
AcDbLinetypeTableRecord
  2
HIDDEN
 70
     0
  3
Hidden __ __ __ __ __ __ __ __ __ __ __ __ __ __
 72
    65
 73
     2
 40
9.524999999999998
 49
6.349999999999999
 74
     0
 49
-3.174999999999999
 74
     0
  0
ENDTAB
  0
TABLE
  2
LAYER
  5
2
102
{ACAD_XDICTIONARY
360
2A2
102
}
330
0
100
AcDbSymbolTable
 70
     3
  0
LAYER
  5
10
102
{ACAD_XDICTIONARY
360
E6
102
}
330
2
100
AcDbSymbolTableRecord
100
AcDbLayerTableRecord
  2
0
 70
     0
 62
     7
  6
Continuous
370
    -3
390
F
347
98
  0
LAYER
  5
1B4
330
2
100
AcDbSymbolTableRecord
100
AcDbLayerTableRecord
  2
View Port
 70
     0
 62
     7
  6
Continuous
290
     0
370
    -3
390
F
347
98
1001
AcAecLayerStandard
1000

1000
View Ports, set to Not Plot
  0
LAYER
  5
21D
330
2
100
AcDbSymbolTableRecord
100
AcDbLayerTableRecord
  2
Defpoints
 70
     0
 62
     7
  6
Continuous
290
     0
370
    -3
390
F
347
98
  0
ENDTAB
  0
TABLE
  2
STYLE
  5
3
330
0
100
AcDbSymbolTable
 70
     5
  0
STYLE
  5
11
330
3
100
AcDbSymbolTableRecord
100
AcDbTextStyleTableRecord
  2
Standard
 70
     0
 40
0.0
 41
1.0
 50
0.0
 71
     0
 42
0.2
  3
arial.ttf
  4

1001
ACAD
1000
Arial
1071
       34
  0
STYLE
  5
DC
330
3
100
AcDbSymbolTableRecord
100
AcDbTextStyleTableRecord
  2
Annotative
 70
     0
 40
0.0
 41
1.0
 50
0.0
 71
     0
 42
0.2
  3
arial.ttf
  4

1001
AcadAnnotative
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
1001
ACAD
1000
Arial
1071
       34
  0
STYLE
  5
178
330
3
100
AcDbSymbolTableRecord
100
AcDbTextStyleTableRecord
  2
Notes
 70
     0
 40
3.0
 41
1.0
 50
0.0
 71
     0
 42
3.0
  3
arial.ttf
  4

1001
AcadAnnotative
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
1001
AcadAnnoPO
1070
     1
1001
ACAD
1000
Arial
1071
       34
  0
STYLE
  5
179
330
3
100
AcDbSymbolTableRecord
100
AcDbTextStyleTableRecord
  2
Titles
 70
     0
 40
6.0
 41
1.0
 50
0.0
 71
     0
 42
0.2
  3
arial.ttf
  4

1001
AcadAnnotative
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
1001
AcadAnnoPO
1070
     1
1001
ACAD
1000
Arial
1071
       34
  0
STYLE
  5
1AF
330
3
100
AcDbSymbolTableRecord
100
AcDbTextStyleTableRecord
  2

 70
     1
 40
0.0
 41
1.0
 50
0.0
 71
     0
 42
0.2
  3
ltypeshp.shx
  4

  0
ENDTAB
  0
TABLE
  2
VIEW
  5
6
330
0
100
AcDbSymbolTable
 70
     0
  0
ENDTAB
  0
TABLE
  2
UCS
  5
7
330
0
100
AcDbSymbolTable
 70
     0
  0
ENDTAB
  0
TABLE
  2
APPID
  5
9
330
0
100
AcDbSymbolTable
 70
    10
  0
APPID
  5
12
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
ACAD
 70
     0
  0
APPID
  5
DD
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
AcadAnnoPO
 70
     0
  0
APPID
  5
DE
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
AcadAnnotative
 70
     0
  0
APPID
  5
DF
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
ACAD_DSTYLE_DIMJAG
 70
     0
  0
APPID
  5
E0
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
ACAD_DSTYLE_DIMTALN
 70
     0
  0
APPID
  5
107
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
ACAD_MLEADERVER
 70
     0
  0
APPID
  5
1B5
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
AcAecLayerStandard
 70
     0
  0
APPID
  5
1BA
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
ACAD_EXEMPT_FROM_CAD_STANDARDS
 70
     0
  0
APPID
  5
237
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
ACAD_DSTYLE_DIMBREAK
 70
     0
  0
APPID
  5
28E
330
9
100
AcDbSymbolTableRecord
100
AcDbRegAppTableRecord
  2
ACAD_PSEXT
 70
     0
  0
ENDTAB
  0
TABLE
  2
DIMSTYLE
  5
A
330
0
100
AcDbSymbolTable
 70
     3
100
AcDbDimStyleTable
 71
     3
340
242
340
27
340
E1
  0
DIMSTYLE
105
27
330
A
100
AcDbSymbolTableRecord
100
AcDbDimStyleTableRecord
  2
Standard
 70
     0
 41
3.0
 42
2.0
 43
9.0
 44
5.0
140
3.0
141
2.0
147
2.0
340
11
1001
ACAD_DSTYLE_DIMJAG
1070
   388
1040
38.0
1001
ACAD_DSTYLE_DIMBREAK
1070
   391
1040
90.0
1001
ACAD_DSTYLE_DIMTALN
1070
   392
1070
     0
  0
DIMSTYLE
105
E1
330
A
100
AcDbSymbolTableRecord
100
AcDbDimStyleTableRecord
  2
Annotative
 70
     0
 40
0.0
 41
3.0
 42
2.5
 43
10.0
 44
5.0
140
3.0
141
2.0
147
2.0
340
11
1001
AcadAnnotative
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
1001
ACAD_DSTYLE_DIMJAG
1070
   388
1040
38.0
1001
ACAD_DSTYLE_DIMBREAK
1070
   391
1040
90.0
1001
ACAD_DSTYLE_DIMTALN
1070
   392
1070
     0
  0
DIMSTYLE
105
242
330
A
100
AcDbSymbolTableRecord
100
AcDbDimStyleTableRecord
  2
Civil-Metric
 70
     0
 41
3.0
 42
1.5
 43
6.0
 44
3.0
 73
     0
 74
     0
 77
     1
 78
     3
 79
     2
140
3.0
141
3.0
147
2.0
179
     2
271
     2
272
     2
276
     1
340
11
1001
ACAD_DSTYLE_DIMBREAK
1070
   391
1040
3.0
1001
ACAD_DSTYLE_DIMJAG
1070
   388
1040
38.0
1001
ACAD_DSTYLE_DIMTALN
1070
   392
1070
     0
  0
ENDTAB
  0
TABLE
  2
BLOCK_RECORD
  5
1
330
0
100
AcDbSymbolTable
 70
     3
  0
BLOCK_RECORD
  5
1F
102
{ACAD_XDICTIONARY
360
15D
102
}
330
1
100
AcDbSymbolTableRecord
100
AcDbBlockTableRecord
  2
*Model_Space
340
22
 70
     0
280
     1
281
     0
  0
BLOCK_RECORD
  5
58
330
1
100
AcDbSymbolTableRecord
100
AcDbBlockTableRecord
  2
*Paper_Space
340
59
 70
     0
280
     1
281
     0
  0
BLOCK_RECORD
  5
238
330
1
100
AcDbSymbolTableRecord
100
AcDbBlockTableRecord
  2
_ArchTick
340
0
 70
     0
280
     1
281
     0
  0
BLOCK_RECORD
  5
23C
330
1
100
AcDbSymbolTableRecord
100
AcDbBlockTableRecord
  2
_Open30
340
0
 70
     0
280
     1
281
     0
  0
BLOCK_RECORD
  5
3D6
330
1
100
AcDbSymbolTableRecord
100
AcDbBlockTableRecord
  2
Testblock1
340
0
310
2800000020000000200000000100080000000000000400000000000000000000000000000000000000000000000080000080000000808000800000008000800080800000C0C0C000C0DCC000F0CAA6000020400000206000002080000020A0000020C0000020E00000400000004020000040400000406000004080000040A0
310
000040C0000040E00000600000006020000060400000606000006080000060A0000060C0000060E00000800000008020000080400000806000008080000080A0000080C0000080E00000A0000000A0200000A0400000A0600000A0800000A0A00000A0C00000A0E00000C0000000C0200000C0400000C0600000C0800000C0
310
A00000C0C00000C0E00000E0000000E0200000E0400000E0600000E0800000E0A00000E0C00000E0E00040000000400020004000400040006000400080004000A0004000C0004000E00040200000402020004020400040206000402080004020A0004020C0004020E000404000004040200040404000404060004040800040
310
40A0004040C0004040E00040600000406020004060400040606000406080004060A0004060C0004060E00040800000408020004080400040806000408080004080A0004080C0004080E00040A0000040A0200040A0400040A0600040A0800040A0A00040A0C00040A0E00040C0000040C0200040C0400040C0600040C08000
310
40C0A00040C0C00040C0E00040E0000040E0200040E0400040E0600040E0800040E0A00040E0C00040E0E00080000000800020008000400080006000800080008000A0008000C0008000E00080200000802020008020400080206000802080008020A0008020C0008020E00080400000804020008040400080406000804080
310
008040A0008040C0008040E00080600000806020008060400080606000806080008060A0008060C0008060E00080800000808020008080400080806000808080008080A0008080C0008080E00080A0000080A0200080A0400080A0600080A0800080A0A00080A0C00080A0E00080C0000080C0200080C0400080C0600080C0
310
800080C0A00080C0C00080C0E00080E0000080E0200080E0400080E0600080E0800080E0A00080E0C00080E0E000C0000000C0002000C0004000C0006000C0008000C000A000C000C000C000E000C0200000C0202000C0204000C0206000C0208000C020A000C020C000C020E000C0400000C0402000C0404000C0406000C0
310
408000C040A000C040C000C040E000C0600000C0602000C0604000C0606000C0608000C060A000C060C000C060E000C0800000C0802000C0804000C0806000C0808000C080A000C080C000C080E000C0A00000C0A02000C0A04000C0A06000C0A08000C0A0A000C0A0C000C0A0E000C0C00000C0C02000C0C04000C0C06000
310
C0C08000C0C0A000F0FBFF00A4A0A000808080000000FF0000FF000000FFFF00FF000000FF00FF00FFFF0000FFFFFF00FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
310
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
310
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
310
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000FFFFFFFF00FF0000000000000000FFFF0000FFFFFFFF00FFFFFFFFFFFFFFFF00FF
310
FFFFFF00FF000000000000000000FF0000FFFFFFFF00FFFFFFFFFFFFFFFF00FFFFFFFF00FF000000000000000000FF0000FFFFFFFF00FFFFFFFFFFFFFFFF00FFFFFFFF00FF000000000000000000FF0000FFFFFFFF00FFFFFFFFFFFFFFFF00FFFF000000000000000000000000000000000000FFFF00000000000000000000
310
FFFF000000000000000000000000FF0000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
310
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
310
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
310
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
102
{BLKREFS
331
3E6
331
3DF
102
}
 70
     4
280
     1
281
     0
  0
ENDTAB
  0
ENDSEC
  0
SECTION
  2
BLOCKS
  0
BLOCK
  5
20
330
1F
100
AcDbEntity
  8
0
100
AcDbBlockBegin
  2
*Model_Space
 70
     2
 10
0.0
 20
0.0
 30
0.0
  3
*Model_Space
  1

  0
ENDBLK
  5
21
330
1F
100
AcDbEntity
  8
0
100
AcDbBlockEnd
  0
BLOCK
  5
5A
330
58
100
AcDbEntity
 67
     1
  8
0
100
AcDbBlockBegin
  2
*Paper_Space
 70
     0
 10
0.0
 20
0.0
 30
0.0
  3
*Paper_Space
  1

  0
ENDBLK
  5
5B
330
58
100
AcDbEntity
 67
     1
  8
0
100
AcDbBlockEnd
  0
BLOCK
  5
23A
330
238
100
AcDbEntity
  8
0
100
AcDbBlockBegin
  2
_ArchTick
 70
     0
 10
0.0
 20
0.0
 30
0.0
  3
_ArchTick
  1

  0
LWPOLYLINE
  5
239
330
238
100
AcDbEntity
  8
0
  6
ByBlock
 62
     0
100
AcDbPolyline
 90
        2
 70
     0
 43
0.15
 10
-0.5
 20
-0.5
 10
0.5
 20
0.5
  0
ENDBLK
  5
23B
330
238
100
AcDbEntity
  8
0
100
AcDbBlockEnd
  0
BLOCK
  5
240
330
23C
100
AcDbEntity
  8
0
100
AcDbBlockBegin
  2
_Open30
 70
     0
 10
0.0
 20
0.0
 30
0.0
  3
_Open30
  1

  0
LINE
  5
23D
330
23C
100
AcDbEntity
  8
0
  6
ByBlock
 62
     0
370
    -2
100
AcDbLine
 10
-1.0
 20
0.26794919
 30
0.0
 11
0.0
 21
0.0
 31
0.0
  0
LINE
  5
23E
330
23C
100
AcDbEntity
  8
0
  6
ByBlock
 62
     0
370
    -2
100
AcDbLine
 10
0.0
 20
0.0
 30
0.0
 11
-1.0
 21
-0.26794919
 31
0.0
  0
LINE
  5
23F
330
23C
100
AcDbEntity
  8
0
  6
ByBlock
 62
     0
370
    -2
100
AcDbLine
 10
0.0
 20
0.0
 30
0.0
 11
-1.0
 21
0.0
 31
0.0
  0
ENDBLK
  5
241
330
23C
100
AcDbEntity
  8
0
100
AcDbBlockEnd
  0
BLOCK
  5
3D7
330
3D6
100
AcDbEntity
  8
0
100
AcDbBlockBegin
  2
Testblock1
 70
     2
 10
0.0
 20
0.0
 30
0.0
  3
Testblock1
  1

  0
LWPOLYLINE
  5
3D9
330
3D6
100
AcDbEntity
  8
0
100
AcDbPolyline
 90
        4
 70
     1
 43
0.0
 10
25.6400475151811
 20
57.31122946773908
 10
30.86802323280392
 20
57.31122946773908
 10
30.86802323280392
 20
54.2011890252624
 10
25.6400475151811
 20
54.2011890252624
  0
ATTDEF
  5
3DA
102
{ACAD_XDICTIONARY
360
3DB
102
}
330
3D6
100
AcDbEntity
  8
0
100
AcDbText
 10
32.85963298601775
 20
54.2011890252624
 30
0.0
 40
3.0
  1
xxx
  7
Notes
100
AcDbAttributeDefinition
280
     0
  3
Testeingabe
  2
TEST
 70
     0
280
     0
1001
AcadAnnotative
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
1001
AcadAnnoPO
1070
     1
  0
ENDBLK
  5
3D8
330
3D6
100
AcDbEntity
  8
0
100
AcDbBlockEnd
  0
ENDSEC
  0
SECTION
  2
ENTITIES
  0
INSERT
  5
3DF
330
1F
100
AcDbEntity
  8
0
100
AcDbBlockReference
 66
     1
  2
Testblock1
 10
0.0
 20
0.0
 30
0.0
  0
ATTRIB
  5
3E1
102
{ACAD_XDICTIONARY
360
3E2
102
}
330
3DF
100
AcDbEntity
  8
0
100
AcDbText
 10
32.85963298601775
 20
54.2011890252624
 30
0.0
 40
3.0
  1
xxx
  7
Notes
100
AcDbAttribute
280
     0
  2
TEST
 70
     0
280
     0
1001
AcadAnnotative
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
1001
AcadAnnoPO
1070
     1
  0
SEQEND
  5
3E0
330
3DF
100
AcDbEntity
  8
0
  0
INSERT
  5
3E6
330
1F
100
AcDbEntity
  8
0
100
AcDbBlockReference
 66
     1
  2
Testblock1
 10
0.0
 20
-6.593285547159609
 30
0.0
  0
ATTRIB
  5
3E8
102
{ACAD_XDICTIONARY
360
3E9
102
}
330
3E6
100
AcDbEntity
  8
0
100
AcDbText
 10
32.85963298601775
 20
47.6079034781028
 30
0.0
 40
3.0
  1
yyy
  7
Notes
100
AcDbAttribute
280
     0
  2
TEST
 70
     0
280
     0
1001
AcadAnnotative
1000
AnnotativeData
1002
{
1070
     1
1070
     1
1002
}
1001
AcadAnnoPO
1070
     1
  0
SEQEND
  5
3E7
330
3E6
100
AcDbEntity
  8
0
  0
VIEWPORT
  5
28B
102
{ACAD_XDICTIONARY
360
28C
102
}
330
58
100
AcDbEntity
 67
     1
  8
0
100
AcDbViewport
 10
4.799458060677595
 20
4.021899493660514
 30
0.0
 40
17.88061277576319
 41
8.992999745766949
 68
     1
 69
     1
 12
4.799458060677595
 22
4.021899493660514
 13
0.0
 23
0.0
 14
0.5
 24
0.5
 15
0.5
 25
0.5
 16
0.0
 26
0.0
 36
1.0
 17
0.0
 27
0.0
 37
0.0
 42
50.0
 43
0.0
 44
0.0
 45
8.992999745766949
 50
0.0
 51
0.0
 72
  1000
 90
   819232
  1

281
     0
 71
     1
 74
     0
110
0.0
120
0.0
130
0.0
111
1.0
121
0.0
131
0.0
112
0.0
122
1.0
132
0.0
 79
     0
146
0.0
170
     0
 61
     5
348
9F
292
     1
282
     1
141
0.0
142
0.0
 63
   250
421
  3355443
  0
VIEWPORT
  5
290
102
{ACAD_XDICTIONARY
360
291
102
}
330
58
100
AcDbEntity
 67
     1
  8
View Port
100
AcDbViewport
 10
4.828866575662197
 20
3.999999761581421
 30
0.0
 40
8.399999618530275
 41
6.399999618530274
 68
     2
 69
     2
 12
6.0
 22
4.5
 13
0.0
 23
0.0
 14
0.5
 24
0.5
 15
0.5
 25
0.5
 16
0.0
 26
0.0
 36
1.0
 17
0.0
 27
0.0
 37
0.0
 42
50.0
 43
0.0
 44
0.0
 45
6.399999618530274
 50
0.0
 51
0.0
 72
  1000
 90
   557152
  1

281
     0
 71
     1
 74
     0
110
0.0
120
0.0
130
0.0
111
1.0
121
0.0
131
0.0
112
0.0
122
1.0
132
0.0
 79
     0
146
0.0
170
     0
 61
     5
348
9F
292
     1
282
     1
141
0.0
142
0.0
 63
   250
421
  3355443
  0
ENDSEC
  0
EOF
"""
