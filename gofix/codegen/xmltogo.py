from xml.dom import minidom as dom
from pprint import pprint

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
types = {
    'UTCTIMESTAMP': "string",
    'UTCDATEONLY': "string",
    'COUNTRY': "string",
    'CHAR': "byte",
    'CURRENCY': "string",
    'LOCALMKTDATE': "string",
    'DATA': "[]byte",
    'NUMINGROUP': "int",
    'QTY': "float",
    'PERCENTAGE': "float",
    'AMT': "float",
    'STRING': "string",
    'EXCHANGE':"string",
    'PRICEOFFSET': "float",
    'UTCTIMEONLY':"string",
    'MULTIPLEVALUESTRING': "string",
    'MONTHYEAR': "string",
    'SEQNUM': "int",
    'PRICE': "float",
    'FLOAT': "float",
    'INT': "int64",
    'LENGTH': "int",
    'BOOLEAN': "bool"
}


def dict_append(d,k,v):
  if k not in d:
    d[k] = []
  d[k].append(v)
def dict_union(d,k,v):
  if k not in d:
    d[k] = set()
  d[k].union(v)
def dict_extend(d,k,v):
  if k not in d:
    d[k] = []
  d[k].extend(v)


# groups are messy - agglomerate all possible fields for each group name
# first, and then render them out at the end

groups = dict()

def renderit(c, groups=groups): 
  req = {'Y':'"required"','N':'"optional"'}
  field_line = lambda f,n=1: " ".join(["\t"]*n+[f['name'], f['name'],req[f['required']]])
  group_line = lambda f,n=1: " ".join(["\t"]*n+[f['name'], "[]"+f['name'],req[f['required']]])

  get_groups(c,groups)

  s = ""
  s += " ".join(["type",c["name"],"struct","{"]) +"\n"
  if '.field' in c:
    for f in c['.field']:
      s += field_line(f)+"\n"
  if '.group' in c:
    for g in c['.group']:
      g['name'] = g['name'][2:]
      s += group_line(g)+"\n"
  if '.component' in c:
    for c2 in c['.component']:
      s += field_line(c2)+"\n"
  s += "}"+"\n"
  return s

def get_groups(message, groups):
  if '.group' in message:
    for g in message['.group']:
      dict_append(groups, g['name'], g)
      get_groups(g, groups)

def flatten_group(groups, group):
  for g in groups:
    if '.component' in g: dict_extend(group, '.component', g['.component'])
    if '.field' in g: dict_extend(group, '.field', g['.field'])
    if '.group' in g: dict_extend(group, '.group', g['.group'])
  return group

print "package fix44"
print "// -------- fields ------------"
for f in tree[".fields"][0][".field"]:
  if ".value" in f:
    print " ".join(["type",f["name"],"int"])
    print  "const ("
    for a in f['.value']:
      print "\t" + " ".join([f["name"]+"_"+a['description'],f["name"],"= iota"])
    print ")"
  else:
    print " ".join(["type",f["name"],types[f["type"]]])

print "// -------- components -------------"

for c in tree[".components"][0][".component"]:
  print renderit(c, groups)

for m in tree['.messages'][0]['.message']:
  print renderit(m, groups)

for gname, g in groups.items():
  g2 = dict()
  flatten_group(g, g2)
  print gname
  pprint(g2)
#for c in tree['.components'][0]['.component']:
#  if '.group' in c:
#    for g in c['.group']:
#      dict_append(groups, g['name'], c['name'])
#for m in tree['.messages'][0]['.message']:
#  if '.group' in m:
#    for g in m['.group']:
#      dict_append(groups, g['name'], m['name'])
#

#print groups

