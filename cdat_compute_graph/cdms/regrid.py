from compute_graph import ComputeNode, register_computation

REGRID_NODE_TYPE = "regrid"
AVAILABLE_TOOLS = ["esmf", "regrid2", "libcf"]
ESMF_METHODS = ["linear", "conserve", "patch"]

@register_computation(REGRID_NODE_TYPE)
def compute_regrid(attributes):
    base_variable = attributes["base"]
    target_variable = attributes["target"]
    args = attributes.get("args", {})

    if "tool" in args and args["tool"] in AVAILABLE_TOOLS:
        if args["tool"] == "esmf" and args["method"] in ESMF_METHODS:
            return base_variable.regrid(target_variable.getGrid(), regridTool=args["tool"], regridMethod=args["method"])
        else:
            return base_variable.regrid(target_variable.getGrid(), regridTool=args["tool"])
    return base_variable.regrid(target_variable.getGrid())


class RegridFunction(ComputeNode):
    def __init__(self, base, target, **args):
        super(GeospatialFunction, self).__init__()
        self.node_type = GEOSPATIAL_NODE_TYPE
        self.node_params = {
            "base": "The variable that will be regrided",
            "target": "The variable that has the desired grid",
        }
        self.base = base
        self.target = target
        if args:
            self.args = args
