# --------------------------------------------------------------
#  shape_repeater.py
#  Version: 1.0.0
#  Author: Attila Gasparetz
#
#  Last Modified by: Attila Gasparetz
#  Last Updated:  05/01/2020
# --------------------------------------------------------------

#####

import nuke

thisNode = nuke.thisGroup()

iRepeats1 = thisNode.knob("copy1").getValue()

iRepeats = int(iRepeats1)

bfirstLoop = True

nDot = nuke.nodes.Dot()

for i in range(iRepeats):
    nTrans = nuke.nodes.Transform(name="t" + str(i), translate="20 20")
    nMerge = nuke.nodes.Merge2(name="m" + str(i))
    nMerge.setInput(1, nTrans)

    if bfirstLoop:
        bfirstLoop = False
        nTrans.setInput(0, nDot)
        nMerge.setInput(0, nDot)
    else:
        nTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)

    nPrevMerge = nMerge

#####

import nuke

thisNode = nuke.thisNode()

cCopies_1 = thisNode.knob("copy1").getValue()
cCopies_2 = thisNode.knob("copy2").getValue()

cCopies1 = int(cCopies_1)
cCopies2 = int(cCopies_2)

CfirstLoop1 = True
CfirstLoop2 = True

CDot = nuke.nodes.Dot()

CopyTrans1 = nuke.toNode('Trans_COPY1')
CopyTrans2 = nuke.toNode('Trans_COPY2')

 for i in range(CfirstLoop1):
     cTrans = nuke.nodes.Transform(name="t" + str(i))
     cMerge = nuke.nodes.Merge2(name="m" + str(i))
     cMerge.setInput(1,cTrans)

     if cfirstLoop1:
         cfirstLoop = False
         cTrans.setInput(0, CopyTrans1)
         cMerge.setInput(0, CopyTrans1)
     else:
         cTrans.setInput(0, cPrevMerge)
         cMerge.setInput(0, cPrevMerge)

     cPrevMerge = cMerge

#####

CopyTrans1 = nuke.toNode('Trans_COPY1')
CopyTrans2 = nuke.toNode('Trans_COPY2')

m = nuke.thisNode()
kc = nuke.thisKnob()
if kc.name() in ["copy1"]:
    i = nuke.toNode('Trans_COPY1')
    o = nuke.toNode('EndCopy1')

    slices = int(['copy1'].value())
    step = int(1)
    for x in range(1,slices+step,step):

        b1 = nuke.nodes.Blur()
        b1.setInput(0, i)
        b1['size'].setExpression("parent.size.w", 0)
        b1['size'].setExpression("parent.size.h", 1)

        m1 = nuke.nodes.Merge()
        m1.setInput(1, b1)
        m1.setInput(0, g1)
        m1['operation'].setValue("divide")

        if x < slices:
            m2 = nuke.nodes.Merge()
        m2.setInput(1, b2)
        m2.setInput(0, g1)
        m2['operation'].setValue("divide")

        i = m1
        i2 = m2

        o.setInput(0, i)

####

thisNode = nuke.thisNode()

cCopies_1 = thisNode.knob("copy1").getValue()
cCopies_2 = thisNode.knob("copy2").getValue()

cCopies1 = int(cCopies_1)
cCopies2 = int(cCopies_2)

CopyTrans1 = nuke.toNode('Trans_COPY1')
CopyTrans2 = nuke.toNode('Trans_COPY2')

CTrans = nuke.nodes.Transform(name="t" + str(i))
CTrans.knob('translate').setExpression('Trans_COPY1.translate')
CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
CTrans.knob('scale').setExpression('Trans_COPY1.scale')
CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
CTrans.knob('center').setExpression('Trans_COPY1.center')
CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
CTrans.knob('filter').setExpression('Trans_COPY1.filter')

CTrans.setInput(0,CopyTrans1)

CMerge = nuke.nodes.Merge2(name="m" + str(i))

CMerge.setInput(0, CTrans)

###

w = nuke.toNode('Transform25')
v = nuke.createNode('Transform')
p = nuke.createNode('Merge2')
v.setInput(0, v)
p.setInput(0, w)

####

iRepeats = 5
bfirstLoop = True

nDot = nuke.nodes.Dot()
w = nuke.toNode('Transform4')
b = nuke.toNode('Blur4')
nDot.setInput(0, w)

for i in range(iRepeats):
    nTrans = nuke.nodes.Transform(name = "t" + str(i))
    nMerge = nuke.nodes.Merge2(name = "m" + str(i))
    nMerge.setInput(1, nTrans)

    
    if bfirstLoop:
        bfirstLoop = False
        nTrans.setInput(0, nDot)
        nMerge.setInput(0, nDot)
    else:
        nTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)
        
    nPrevMerge = nMerge

MNum = int(iRepeats) - 1

p = nuke.toNode("m" + str(MNum))

b.setInput(0, p)

























