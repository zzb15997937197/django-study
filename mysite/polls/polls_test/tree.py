class TreeNode:

    def __init__(self, data_id=None, val=None, floor=None):
        self.id = data_id
        self.data = val
        self.floor = floor
        self.parent = None
        self.childs = []

    # 添加孩子
    def add_child(self, node):
        node.parent = self
        self.childs.append(node)

    # 遍历孩子
    def travel_chid(self):
        return [{"id": x.id, "val": x.data} for x in self.childs]

    # 获取父亲节点
    def get_parent(self, node):
        return self.parent
