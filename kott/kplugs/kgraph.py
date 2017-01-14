from kott.kplugbase import KPlugBase


class Node(object):
    label = None  # FIX: can be a property!
    properties = None
    relations = []

    def __init__(self, label, properties):
        self.label = label
        self.properties = properties
        self.relations = []

    def add_relation(self, relation):
        self.relations.append(relation)


class Relation(object):
    label = None
    properties = None
    related_to = None

    def __init__(self, label, properties, child):
        self.label = label
        self.properties = properties
        self.related_to = child


class Graph(object):
    nodes = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)


# n1 = Node("Person", {"name": "Mostafa", "age": 30})
# n1_1 = Node("Person", {"name": "Mostafa", "age": 30})
# n2 = Node("Person", {"name": "Sina", "age": 26, "crashed": False})
# n3 = Node("Person", {"name": "Samy", "age": 28})

# r1 = Relation("KNOWS", None, n2) # Mostafa KNOWS Sina
# r2 = Relation("KNOWS", {"since": 2014}, n1) # Sina KNOWS Mostafa
# r3 = Relation("KNOWS", {"since": 2010, "sport": "hockey"}, n1_1) # another Mostafa, known to Sina
# r4 = Relation("KNOWS", {"since": 1987}, n1) # knows itself since birth

# n1.add_relation(Relation("KNOWS", None, n2))
# n1.add_relation(Relation("KNOWS", {"since": 1987}, n1))
# n2.add_relation(Relation("KNOWS", {"since": 2014}, n1))
# n2.add_relation(Relation("KNOWS", {"since": 2010, "sport": "hockey"}, n1_1))

# g = Graph()
# g.add_node(n1)
# g.add_node(n2)
# g.add_node(n1_1)
# g.add_node(n3)

# for n in g.nodes:
#     print n.label + " " + str(n.properties) + " " + str( [r.label + " " + r.related_to.properties["name"] for r in n.relations]) + "\n"


class KGraph(KPlugBase):
    _priority_ = 2
    __graph__ = {}
    _keywords_ = ["node_label", "relation_label"]

    def on_set(self, key, value, **kwargs):
        # TODO: KLog
        # print ("Setting tag:" + kwargs["tag"] +
        #        " for key:" + str(key) + ", value: " + str(value))
        if kwargs["tag"] in self.__tag__:
            self.__tag__[kwargs["tag"]].append(key)
        else:
            self.__tag__[kwargs["tag"]] = [key]

        return value

    def on_find_visit(self, key, value, **kwargs):
        if kwargs["tag"] in self.__tag__:
            if key in self.__tag__[kwargs["tag"]]:
                # TODO: KLog
                # print ("Found tag:" + kwargs["tag"] +
                #        " on key:" + str(key) + ", value: " + str(value))
                return True
        return False
