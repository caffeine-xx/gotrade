out = ["package fix44;"]
types = {
    'UTCTIMESTAMP': "string",
    'UTCDATEONLY': "string",
    'COUNTRY': "string",
    'CHAR': "string",
    'CURRENCY': "string",
    'LOCALMKTDATE': "string",
    'DATA': "bytes",
    'NUMINGROUP': "uint32",
    'QTY': "float",
    'PERCENTAGE': "float",
    'AMT': "float",
    'STRING': "string",
    'EXCHANGE':"string",
    'PRICEOFFSET': "float",
    'UTCTIMEONLY':"string",
    'MULTIPLEVALUESTRING': "string",
    'MONTHYEAR': "string",
    'SEQNUM': "uint32",
    'PRICE': "float",
    'FLOAT': "float",
    'INT': "int64",
    'LENGTH': "uint32",
    'BOOLEAN': "bool"
}
fields = {}
enums = {}
required = {"Y": "required", "N": "optional"}
def render_field_line(i,f,prefix=""):
    field = fields[f["name"]]
    req = required[str(f["required"])]
    typ = field["ptype"]
    return prefix + " ".join([req,typ,f["name"]]) + " = " + str(i) + ";\n"

def render_group_line(i,g,prefix=""):
    typ = g["name"]+"Group"
    name = g["name"]
    return prefix +  "repeated " + " ".join([typ,name]) + " = " + str(i) + ";\n"

def render_component_line(i,c,prefix=""):
    typ = c["name"]+"Component"
    req = required[str(c["required"])]
    return prefix + " ".join([req,typ,c["name"]]) + " = " + str(i) + ";\n"

def render_message(c,prefix="",suffix=""):
    s = prefix + "message " + c["name"] + suffix + " {\n"
    i = 1
    if ".field" in c:
        for f in c[".field"]:
            s = s + render_field_line(i,f,prefix+"\t"); i = i + 1
    if ".group" in c:
        for g in c[".group"]:
            s = s + render_field_line(i,g,prefix+"\t"); i = i + 1
            g["name"] = g["name"][2:]
            s = s + render_message(g,prefix+"\t","Group")
            s = s + render_group_line(i,g,prefix+"\t"); i = i + 1
    if ".component" in c:
        for c2 in c[".component"]:
            s = s + render_component_line(i,c2,prefix+"\t"); i = i + 1
    s = s + prefix + "}\n"
    return s

#def render_toplevel(f):
#        s = "message "+f["name"] + " {\n"
#        s = s + "\tenum " + f["name"] + "Enum {\n"
#        for i,e in enumerate(f[".value"]):
#            s = s + "\t\t"+e["description"]+" = "+str(i)+";\n"
#        s = s + "\t}\n"
#        s = s + "\trequired "+f["name"]+"Enum value = 1;\n"
#        s = s + "}\n"
#        return s

def render_field_def(f):
        s = "message "+f["name"] + " {\n"
        s = s + "\tenum " + f["name"] + "Enum {\n"
        for i,e in enumerate(f[".value"]):
            s = s + "\t\t"+e["description"]+" = "+str(i)+";\n"
        s = s + "\t}\n"
        s = s + "\trequired " +f["name"] + "Enum value = 1;\n"
        s = s + "}\n"
        return s

