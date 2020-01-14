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

iRepeats = 20
bfirstLoop = True

# Main Transform for Copy1
w = nuke.toNode('Trans_COPY1')

# Last Merge connected to this
b = nuke.toNode('Blur4')

# Dot would be connected to this and allows toggle between original and modified source 
s = nuke.toNode('Switch1')

nDot = nuke.nodes.Dot()
nDot.setInput(0, s)

for i in range(iRepeats):
    CTrans = nuke.nodes.Transform(name = "t" + str(i))
    CTrans.knob('translate').setExpression('Trans_COPY1.translate')
    CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
    CTrans.knob('scale').setExpression('Trans_COPY1.scale')
    CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
    CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
    CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
    CTrans.knob('center').setExpression('Trans_COPY1.center')
    CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
    CTrans.knob('filter').setExpression('Trans_COPY1.filter')
    nMerge = nuke.nodes.Merge2(name = "m" + str(i))
    nMerge.knob('also_merge').setValue('all')
    nMerge.setInput(1, CTrans)
    
    if bfirstLoop:
        bfirstLoop = False
        CTrans.setInput(0, nDot)
        nMerge.setInput(0, nDot)
    else:
        CTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)

    nPrevMerge = nMerge

MNum = int(iRepeats) - 1

p = nuke.toNode("m" + str(MNum))

b.setInput(0, p)


####


nuke.toNode('PROXY_MAIN').knob('knobChanged').setValue('
n = nuke.thisNode()
k = nuke.thisKnob()
if k.name()=="copy1":
    C = nuke.toNode('PROXY_MAIN').knob('copy1').getValue()
    
    iRepeats = int(C)
    bfirstLoop = True
    
    # Main Transform for Copy1
    w = nuke.toNode('Trans_COPY1')
    
    # Last Merge connected to this
    b = nuke.toNode('Blur1')
    
    # Dot would be connected to this and allows toggle between original and modified source 
    s = nuke.toNode('Switch1')
    
    nDot = nuke.nodes.Dot()
    nDot.setInput(0, s)
    
    for i in range(iRepeats):
        CTrans = nuke.nodes.Transform(name = "t" + str(i))
        CTrans.knob('translate').setExpression('Trans_COPY1.translate')
        CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
        CTrans.knob('scale').setExpression('Trans_COPY1.scale')
        CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
        CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
        CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
        CTrans.knob('center').setExpression('Trans_COPY1.center')
        CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
        CTrans.knob('filter').setExpression('Trans_COPY1.filter')
        nMerge = nuke.nodes.Merge2(name = "m" + str(i))
        nMerge.knob('also_merge').setValue('all')
        nMerge.setInput(1, CTrans)
        
        if bfirstLoop:
            bfirstLoop = False
            CTrans.setInput(0, nDot)
            nMerge.setInput(0, nDot)
        else:
            CTrans.setInput(0, nPrevMerge)
            nMerge.setInput(0, nPrevMerge)
    
        nPrevMerge = nMerge
    
    MNum = int(iRepeats) - 1
    
    p = nuke.toNode("m" + str(MNum))
    
    b.setInput(0, p)
else:
    pass')


#####


nuke.toNode('PROXY_MAIN').knob('knobChanged').setValue('n = nuke.thisNode()\nk = nuke.thisKnob()\nif k.name()=="copy1":\n C = nuke.toNode('PROXY_MAIN').knob('copy1').getValue()\n iRepeats = int(C)\n bfirstLoop = True\n # Main Transform for Copy1\n w = nuke.toNode('Trans_COPY1')\n # Last Merge connected to this\n b = nuke.toNode('Blur1')\n # Dot would be connected to this and allows toggle between original and modified source \n s = nuke.toNode('Switch1')\n nDot = nuke.nodes.Dot()\n nDot.setInput(0, s)\n for i in range(iRepeats):\n  CTrans = nuke.nodes.Transform(name = "t" + str(i))\n  CTrans.knob('translate').setExpression('Trans_COPY1.translate')\n  CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')\n  CTrans.knob('scale').setExpression('Trans_COPY1.scale')\n  CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')\n  CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')\n  CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')\n  CTrans.knob('center').setExpression('Trans_COPY1.center')\n  CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')\n  CTrans.knob('filter').setExpression('Trans_COPY1.filter')\n  nMerge = nuke.nodes.Merge2(name = "m" + str(i))\n  nMerge.knob('also_merge').setValue('all')\n  nMerge.setInput(1, CTrans)\n  if bfirstLoop:\n   bfirstLoop = False\n   CTrans.setInput(0, nDot)\n   nMerge.setInput(0, nDot)\n  else:\n   CTrans.setInput(0, nPrevMerge)\n   nMerge.setInput(0, nPrevMerge)\n  nPrevMerge = nMerge\n MNum = int(iRepeats) - 1\n p = nuke.toNode("m" + str(MNum))\n b.setInput(0, p)\nelif:\n pass')


####
                                                       
                                                       nuke.selectedNode().knob('knobChanged').setValue(
'm = nuke.thisNode()
kc = nuke.thisKnob()

if kc.name() in ["copy1"]:
    s = nuke.toNode('Switch1')
    o = nuke.toNode('COPIES1_end')
    cDot = nuke.nodes.Dot()
    cDot.setInput(0, s)

    for n in nuke.allNodes():
        if "static" not in n['label'].getValue():
            nuke.delete(n)

    slices = int(m['copy1'].value())
    step = int(1)
    for x in range(1, slices + step, step):
        CTrans = nuke.nodes.Transform(name = "t" + str(i))
        CTrans.setInput(0, cDot)
        CTrans.knob('translate').setExpression('Trans_COPY1.translate')
        CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
        CTrans.knob('scale').setExpression('Trans_COPY1.scale')
        CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
        CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
        CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
        CTrans.knob('center').setExpression('Trans_COPY1.center')
        CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
        CTrans.knob('filter').setExpression('Trans_COPY1.filter')

        m1 = nuke.nodes.Merge()
        m1.setInput(1, cDot)
        m1.setInput(0, CTrans)
        m1.knob('also_merge').setValue('all')


        if x < slices:
            m2 = nuke.nodes.Merge()
            m2.setInput(1, CTrans)
            m2.setInput(0, m1)
            m2.knob('also_merge').setValue('all')

        cDot = m1
        CTrans = m2

    o.setInput(0, i)')






