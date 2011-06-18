from xml.dom import minidom as dom
from pprint import pprint

import go
from go import *
parser =  go

#import protobuf
#from protobuf import *
#parser =  protobuf



# ---- load xml ----
filename = "FIX44.xml"
xmltree = dom.parse(open(filename,"r")).childNodes[0]

# ----- parse xml ----

def xml2dict(xmltree):
    tree = dict(zip(map(str,xmltree.attributes.keys()),map(lambda x: str(x.value),xmltree.attributes.values())))
    if len(xmltree.childNodes)>0:
        for child in xmltree.childNodes:
            if child.nodeType == child.ELEMENT_NODE:
                name = "."+child.nodeName
                childtree = xml2dict(child)
                if name in tree:
                    if isinstance(tree[name],list):
                        tree[name].append(childtree)
                    else:
                        tree[name] = [tree[name]]+[childtree]
                else:
                    tree[name]=[childtree]
            else: 
                pass
    return tree

tree = xml2dict(xmltree)

# ---- generate protobuf ----

required = {"Y": "required", "N": "optional"}

out = parser.out
fields = parser.fields
enums = parser.enums
types = parser.types

# check for duplicate enums
tvalues = dict()
def dict_append(d,k,v):
  if k not in d:
    d[k] = []
  d[k].append(v)

for f in tree[".fields"][0][".field"]:
  if ".value" in f and f['type']=="STRING":
    for a in f['.value']:
      dict_append(tvalues, a['description'], (f['type'],f['name']))

for val, ts in tvalues.items():
  if len(set(ts)) != 1:
    print val, ts

# preload fields
#for f in tree[".fields"][0][".field"]:
#    if ".value" in f:
#        enums[f["name"]]=f
#    f["ptype"] = types[f["type"]]
#    fields[f["name"]] = f
#
#for f in tree[".fields"][0][".field"]:
#    if ".value" in f:
#        s = render_field_def(f)
#        out.append(s)
#
#for c in tree[".components"][0][".component"]:
#    s = render_message(c,suffix="Component")
#    out.append(s)
#
#for m in tree[".messages"][0][".message"]:
#    s = render_message(m)
#    out.append(s)
#
#print "\n".join(out)
