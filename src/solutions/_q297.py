class Codec:
    def serialize(self, root):
        def dfs(node):
            if node:
                ret.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else: ret.append('#')
        ret = []
        dfs(root)
        return ','.join(ret)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split(','))
        return dfs()
