import nuke

thisNode = nuke.thisGroup()

Copies1 = thisNode[copy1].value()

Copies2 = thisNode[copy2].value()

cDot = nuke.nodes.Dot()

cFirstLoop = True

for i in range(Copies1):
    cTrans = nuke.nodes.Transform(name = "t" + str(i), translate = 20 20)
    cMerge = nuke.nodes.Merge2(name = "m" + str(i))
    cMerge.setInput(1,cTrans)

    if cFirstLoop:
        cFirstLoop = False
        cTrans.setInput(0, cDot)
        cMerge.setInput(0, cDot)
    else:
        cTrans.setInput(0, cprevMerge)
        cMerge.setInput(0, cprevMerge)

    cprevMerge = cMerge

#####

iRepeats = 10
bfirstLoop = True

nDot = nuke.nodes.Dot()

for i in range(iRepeats):
    nTrans = nuke.nodes.Transform(name = "t" + str(i), translate = "20 20")
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
    
#####


import nuke

thisNode = nuke.thisGroup()

thisNode.begin()
    
copy1 = nuke.toNode('PROXY_MAIN').knob('copy1').getvalue()

copy2 = nuke.toNode('PROXY_MAIN').knob('copy2').getvalue()

cDot = nuke.nodes.Dot()

cFirstLoop = True

for i in range(copy1):
    cTrans = nuke.nodes.Transform(name = "t" + str(i))
    cMerge = nuke.nodes.Merge2(name = "m" + str(i))
    cMerge.setInput(1,cTrans)

    if cFirstLoop:
        cFirstLoop = False
        cTrans.setInput(0, cDot)
        cMerge.setInput(0, cDot)
    else:
        cTrans.setInput(0, cprevMerge)
        cMerge.setInput(0, cprevMerge)

    cprevMerge = cMerge





