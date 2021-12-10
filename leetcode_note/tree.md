## 二叉树

### 1. 基础知识

**满二叉树：**叶子节点在同一层且铺满。

**完全二叉树： ** 只有最后一层没有铺满，且叶子节点集中在左边。

**二叉搜索树：** 左子树值均小于根节点，右子树均大于根节点。

**平衡二叉搜索树：**左右子树高度差不超过1的二叉搜索树。

### 2. 二叉树的遍历

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
    queue = [root]
    while queue:
        tmp_node = queue.pop(0)
        process(tmp_node)
        if tmp_node.left is not None: queue.append(tmp_node.left)
        if tmp_node.right is not None: queue.append(tmp_node.right)
```

如果我们需要层的信息，比如说需要知道当前是第几层 例：111. 二叉树的最小深度

```python
def travel(root:Node):
    queue = [root]
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



