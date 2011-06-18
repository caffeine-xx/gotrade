fields = {}
enums = {}
required = {"Y": "required", "N": "optional"}
out = ["package fix44;"]
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

def render_field_line(i,f,prefix=""):
    field = fields[f["name"]]
    typ = field["ptype"]
    return prefix + " ".join([f["name"],typ]) + "\n"

def render_group_line(i,g,prefix=""):
    typ = g["name"]+"Group"
    name = g["name"]
    return prefix +  name + " []" + typ + "\n"

def render_component_line(i,c,prefix=""):
    typ = c["name"]+"Component"
    req = required[str(c["required"])]
    return prefix + " ".join([typ,c["name"]]) + "\n"

def render_message(c,prefix="",suffix="", prefun=False):
    i=0
    if ".group" in c:
        for g in c[".group"]:
            g["name"] = g["name"][2:]
            s = s + render_message(g,prefix,"Group")
    
    s = prefix + "type " + c["name"] + suffix + " struct {\n"
    if ".field" in c:
        for f in c[".field"]:
            s = s + render_field_line(i,f,prefix+"\t")
    if ".group" in c:
        for g in c[".group"]:
            s = s + render_field_line(i,g,prefix+"\t")
            g["name"] = g["name"][2:]
            s = s + render_message(g,prefix+"\t","Group")
            s = s + render_group_line(i,g,prefix+"\t")
    if ".component" in c:
        for c2 in c[".component"]:
            s = s + render_component_line(i,c2,prefix+"\t")
    s = s + prefix + "}\n"
    return s

def render_field_def(f):
        s = "const (\n"
        for i,e in enumerate(f[".value"]):
            s = s + "\t"+e["description"]+" = iota\n"
        s = s + ")\n"
        s = s + "type "+f["name"] + " struct {\n"
        s = s + "\tValue int\n"
        s = s + "}"
        return s

