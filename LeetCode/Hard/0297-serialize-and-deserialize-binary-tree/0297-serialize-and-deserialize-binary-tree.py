# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque([root])
        ans = ['#','x']
        while q:
            node = q.popleft()
            if(node):
                q.append(node.left)
                q.append(node.right)

                ans.append(str(node.val))
            else:
                ans.append('#')
            ans.append('x')

        return ''.join(ans) 

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        nodes = data.split('x')
        if nodes[1] == '#':
            return None

        root = TreeNode(int(nodes[1]))
        q=collections.deque([root])

        idx = 2
        while q:
            node = q.popleft()
            if not nodes[idx] == '#':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx+=1
            if not nodes[idx] == '#':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx+=1
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))