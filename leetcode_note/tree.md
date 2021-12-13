## 二叉树

### 1. 基础知识

**满二叉树: **叶子节点在同一层且铺满。

**完全二叉树: ** 只有最后一层没有铺满，且叶子节点集中在左边。

**二叉搜索树: ** 左子树值均小于根节点，右子树均大于根节点。

**平衡二叉搜索树: **左右子树高度差不超过1的二叉搜索树。

### 2. 二叉树的遍历（代码模板）

**深度优先**
  -前、中、后序遍历**(递归)**

```python
def travel(root:Node):
    if root is None:
        # process
        return
    
    ## 前序遍历
    process(root) # 这里对节点进行处理
    travel(root.left)
    travel(root.right)
    
    ## 中序遍历
    travel(root.left)
    process(root) # 这里对节点进行处理
    travel(root.right)
    
    ## 后序遍历
    travel(root.left)
    travel(root.right)
    process(root) # 这里对节点进行处理
```

-前序遍历**(非递归)**

```python
def travel(root:Node):
    stack = [root]
    while len(stack) > 0:
        tmp_node = stack.pop(-1)
        ## 前序遍历
        process(tmp_node) ## 处理节点
        if tmp_node.right is not None: stack.append(tmp_node.right)
        if tmp_node.left is not None: stack.append(tmp_node.left)
        
```

 -中序遍历**(非递归)**

```python
def travel(root:Node):
    stack = []
    cur_node = root
    while cur_node is not None and len(stack) != 0:
        if cur_node is not None:
            stack.append(cur_node) # 相当于先放根节点，再放左节点
            cur_node = cur_node.left
        else:
            cur_node = stack.pop(-1)  # 取出最后一个
            
            process(cur_node)
            
            cur_node = cur_node.right
```

 -后序遍历**(非递归)**

​    相当于将前序遍历左右交换，然后将输出反转。

-前、中、后序遍历**(非递归、标记法)**

```python
def travel(root:Node):
    stack = [root]
    while len(stack) > 0:
        tmp_node = stack.pop(-1)
        
        ## 前序遍历
        if tmp_node is not None:
            if tmp_node.right is not None: stack.append(tmp_node.right)
           	if tmp_node.left is not None: stack.append(tmp_node.left)
            stack.append(tmp_node)
            stack.append(None) # 标记，遇到None，读取下一个
        else:
            tmp_node = stack.pop(-1)
            process(tmp_node)
        
        ## 中序遍历
        if tmp_node is not None:
            if tmp_node.right is not None: stack.append(tmp_node.right)
            stack.append(tmp_node)
            stack.append(None) # 标记，遇到None，读取下一个
           	if tmp_node.left is not None: stack.append(tmp_node.left)
        else:
            tmp_node = stack.pop(-1)
            process(tmp_node)
            
        ## 前序遍历
        if tmp_node is not None:
            stack.append(tmp_node)
            stack.append(None) # 标记，遇到None，读取下一个
            if tmp_node.right is not None: stack.append(tmp_node.right)
           	if tmp_node.left is not None: stack.append(tmp_node.left)
        else:
            tmp_node = stack.pop(-1)
            process(tmp_node)
    
```

**广度优先**

 -层序遍历

```python
def travel(root:Node):
    queue = []
    if root is not None:
        queue.append(root)
    while queue:
        tmp_node = queue.pop(0)
        process(tmp_node)
        if tmp_node.left is not None: queue.append(tmp_node.left)
        if tmp_node.right is not None: queue.append(tmp_node.right)
```

如果我们需要层的信息，比如说需要知道当前是第几层 例：111. 二叉树的最小深度

```python
def travel(root:Node):
    queue = []
    if root is not None:
        queue.append(root)
    cur_level = 0
    while queue:
        cur_level_length = len(queue) # 当前层节点数
        for _ in range(cur_level_length):
            tmp_node = queue.pop(0)
            process(tmp_node, cur_level)
            if tmp_node.left is not None: queue.append(tmp_node.left)
            if tmp_node.right is not None: queue.append(tmp_node.right)
       	cur_level += 1
```

### 3. 二叉树的构造（代码模板）

**前、中** 或 **后、中** 可以唯一确定二叉树，需要用中序遍历来确定左右子树。

**中序、后序: ** 后序的最后一位必为根节点，中序以根节点分左右子树，递归创建

```python
def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        inorderRootIndex = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:inorderRootIndex], postorder[:inorderRootIndex])
        root.right = self.buildTree(inorder[inorderRootIndex+1:], postorder[inorderRootIndex:-1])
        return root
```





### 4. 部分例题

**共同祖先-236**

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is p or root is q or root is None:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l is not None and r is not None: 
            return root
        elif l is not None:
            return l
        return r
```

**修剪二叉搜索树-669**

```python
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        if root is None: return None
        if root.val < low: return self.trimBST(root.right, low, high)
        if root.val > high: return self.trimBST(root.left, low, high)

        if root.val <= high: root.right = self.trimBST(root.right, low, high)
        if root.val >= low: root.left = self.trimBST(root.left, low, high)

        return root
```

删除二叉搜索树的某个节点-450

```python
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            ## 非递归
        # if root is None:
        #     return None

        # searchedNode = root
        # fatherNode = None
        # from_root = 0
        # while searchedNode.val != key:
        #     if searchedNode.val < key:
        #         fatherNode = searchedNode
        #         from_root = 2
        #         searchedNode = searchedNode.right
        #     elif searchedNode.val > key:
        #         fatherNode = searchedNode
        #         from_root = 1
        #         searchedNode = searchedNode.left
        #     if searchedNode is None:
        #         return root

        # left = searchedNode.left
        # right = searchedNode.right

        # if right is None:
        #     if from_root == 0:
        #         return left
        #     elif from_root == 1:
        #         fatherNode.left = left
        #     else:
        #         fatherNode.right = left
        #     return root
        # else:
        #     minRightNode = right
        #     rightFather = searchedNode
        #     if minRightNode.left is None:
        #         searchedVal = minRightNode.val
        #         # print('shanchu')
        #         right = minRightNode.right
        #     else:
        #         while True:
        #             if minRightNode.left is not None:
        #                 rightFather = minRightNode
        #                 minRightNode = minRightNode.left
        #             else:
        #                 searchedVal = minRightNode.val
        #                 rightFather.left = minRightNode.right
        #                 break
        #     if from_root == 0:
        #         newNode = TreeNode(searchedVal)
        #         newNode.left = left
        #         newNode.right = right
        #         minRightNode = None
        #         return newNode
        #     elif from_root == 1:
        #         newNode = TreeNode(searchedVal)
        #         newNode.left = left
        #         newNode.right = right
        #         fatherNode.left = newNode
        #         minRightNode = None
        #     else:
        #         newNode = TreeNode(searchedVal)
        #         newNode.left = left
        #         newNode.right = right
        #         fatherNode.right = newNode
        #         minRightNode = None
        #     return root
            ## 递归
        if root is None:
            return None
        
        if root.val == key:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                cur_node = root.right
                while cur_node.left is not None:
                    cur_node = cur_node.left
                cur_node.left = root.left
                return root.right
        if root.val < key: root.right = self.deleteNode(root.right, key)
        elif root.val > key: root.left = self.deleteNode(root.left, key)
        return root

```

