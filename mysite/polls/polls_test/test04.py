'''
读取文件
'''
import json
from polls.polls_test.tree import TreeNode

f = open("C:\\Users\\yinfa\\Desktop\\good_test.txt")
list_data = []
line = f.readline()
count = 0
while line:
    count += 1
    print(line)
    list_data.append({"id": count, "t": line})
    line = f.readline()

f.close()

trees = []
print(list_data)
root = TreeNode()


def gen_child(root, node):
    # 添加子节点
    if root.data in node.data and node.data[0:len(root.data)] == root.data:
        root.add_child(node)
        return node
    else:
        print("找到父节点做为根节点,并且父节点时一定存在的")
        parent = root.parent
        if parent.data in node.data and parent.data[0:len(parent.data)] == node.data:
            return node
        else:
            while True:
                p_root = root.parent
                if p_root.data in node.data and node.data[0:len(p_root.data)] == p_root.data:
                    return p_root
                root = p_root


'''
递归的方法实现，一次遍历，根据节点的层次来判断应该加在哪个节点下
                        1 
                 101    102   103  104
            10101 10102  ...
      1010101  1010102


1. 通过先根遍历的方式建造一棵树。遍历的顺序为中、左、右
2. 每颗树都是单独构造的，构造完一颗树后，再去构造另一颗

'''
trees_root_datas = []
for i in list_data:
    data = i["t"].strip()
    data_length = len(data)
    node = TreeNode(i["id"], data, (data_length + 1) / 2)
    print("id:", node.id, "data:", node.data, "floor:", node.floor)
    if data_length == 1:
        # 怎么将树的每一层数据进行汇总
        root = node
        trees.append(root)
    else:
        root = gen_child(root, node)

print("树为:", trees)
# 遍历所有的树
dict_datas = []


def travel_tree(node_date, childs):
    if len(childs) > 0:
        datas = [{"id": x.id, "val": x.data, "childs": x.childs} for x in childs]
        node_date["data"] = [{"id": x["id"], "val": x["val"]} for x in datas]
        for k in datas:
            k_childs = k["childs"]
            k = {"id": k["id"], "val": k["val"]}
            travel_tree(k, k_childs)
    for j in childs:
        j_childs = j.childs
        j = {"id": j.id, "val": j.data}
        travel_tree(j, j_childs)


print("得到结果为:")
print([{"id": x.id, "val": x.data} for x in dict_datas])
