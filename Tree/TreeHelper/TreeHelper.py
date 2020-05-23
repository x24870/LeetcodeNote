from copy import deepcopy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeGenerator:
    @classmethod
    def remove_node_with_val_None(cls, root):
        if not root: return
        if root.left:
            if root.left.val == None:
                root.left = None
            else:
                cls.remove_node_with_val_None(root.left)

        if root.right:
            if root.right.val == None:
                root.right = None
            else:
                cls.remove_node_with_val_None(root.right)

        return root

    @classmethod
    def get_bin_tree(cls, input_lst):
        lst = deepcopy(input_lst)
        if not lst:
            print('List is empty, return Null')
            return None
        # Input is a list
        # Return a root of a binary tree
        root = TreeNode(lst.pop(0))
        cur_level_lst = [root]
        next_level_lst = []

        while lst:
            try:
                for node in cur_level_lst:
                    if node.val != None:
                        node.left = TreeNode(lst.pop(0))
                        node.right = TreeNode(lst.pop(0))
                        next_level_lst.append(node.left)
                        next_level_lst.append(node.right)
                    else:
                        node = None
                cur_level_lst = next_level_lst
                next_level_lst = []
            except IndexError:
                print('Out of index, please check your list')
                    
        return cls.remove_node_with_val_None(root)

class TreeHelper:
    @classmethod
    def get_height(cls, root):
        if not root: return 0
        return max(cls.get_height(root.left), cls.get_height(root.right)) + 1

    @classmethod
    def get_filled_tree(cls, root, height):
        if height <= 1: return
        if not root.left: root.left = TreeNode(None)
        if not root.right: root.right = TreeNode(None)
        cls.get_filled_tree(root.left, height-1)
        cls.get_filled_tree(root.right, height-1)

    @classmethod
    def print_tree(cls, root):
        NULL_NODE = " "
        # this function was modified form:
        # https://github.com/jdmcpeek/pretty-print-binary-tree/blob/c153183b28c73f0029131d68bb7d59757b0c5c63/tree.py#L62

        # get height of tree
        total_layers = cls.get_height(root)
        print('total_layers: ', total_layers)

        # copy root, and get filled tree
        tree = deepcopy(root)
        cls.get_filled_tree(tree, total_layers)

        # start a queue for BFS
        queue = []
        # add root to queue
        queue.insert(0, tree)

        # index for 'generation' or 'layer' of tree
        gen = 0
        # BFS main
        while queue:
            # copy queue
            copy = []
            while queue:
                copy.insert(0, queue.pop(0))


            first_item_in_layer = True
            edges_string = ""
            extra_spaces_next_node = False

            # modified BFS, layer by layer (gen by gen)
            while copy:
                node = copy.pop(0)

                # init spacing
                spaces_front = pow(2, total_layers - gen + 1) - 2
                spaces_mid   = pow(2, total_layers - gen + 2) - 2
                dash_count   = pow(2, total_layers - gen) - 2
                if dash_count < 0:
                    dash_count = 0
                spaces_mid = spaces_mid - (dash_count*2)
                spaces_front = spaces_front - dash_count
                init_padding = 2
                spaces_front += init_padding
                if first_item_in_layer:
                    edges_string += " " * init_padding

                # construct edges layer
                edge_sym = "/" if node.left and node.left.val != None else " "
                if first_item_in_layer:
                    edges_string += " " * int(pow(2, total_layers - gen) - 1) + edge_sym
                else:
                    edges_string += " " * int(pow(2, total_layers - gen + 1) + 1) + edge_sym

                edge_sym = "\\" if node.right and node.right.val != None else " "
                edges_string += " " * (pow(2, total_layers - gen + 1) - 3) + edge_sym

                # conditions for dashes
                if node.left and node.left.val == None:
                    dash_left = " "
                else:
                    dash_left = "_"

                if node.right and node.right.val==None:
                    dash_right = " "
                else:
                    dash_right = "_"

                # handle condition for extra spaces when node lengths don't match or are even:
                if extra_spaces_next_node:
                    extra_spaces = 1
                    extra_spaces_next_node = False
                else:
                    extra_spaces = 0

                # account for longer data
                data_length = len(str(node.val)) if node.val != None else len(NULL_NODE)
                if data_length > 1:
                    if data_length % 2 == 1: # odd
                        if dash_count > 0:
                            dash_count -= ((data_length - 1)/2)
                        else:
                            spaces_mid -= (data_length - 1)/2
                            spaces_front -= (data_length - 1)/2
                            if data_length is not 1: 
                                extra_spaces_next_node = True 
                    else: # even
                        if dash_count > 0:
                            dash_count -= ((data_length)/2) - 1
                            extra_spaces_next_node = True
                            # dash_count += 1
                        else:
                            spaces_mid -= (data_length - 1)
                            spaces_front -= (data_length - 1)

                # print node with/without dashes
                if first_item_in_layer:
                    val_str = str(node.val) if node.val != None else NULL_NODE
                    print( (" " * spaces_front) + (dash_left * int(dash_count)) + val_str + (dash_right * int(dash_count)),  end='' )
                    first_item_in_layer = False
                else:
                    val_str = str(node.val) if node.val != None else NULL_NODE
                    print( " " * (spaces_mid-extra_spaces+1) + (dash_left * int(dash_count)) + val_str + (dash_right * int(dash_count)), end='' )


                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)


            # print the fun squiggly lines
            if queue:
                print("\n" + edges_string)

            # increase layer index
            gen += 1

        print('\n')


if __name__ == '__main__':
    a = [1, 2, 3]
    print(a)
    root = TreeGenerator.get_bin_tree(a)
    TreeHelper.print_tree(root)


    a.append(2)
    a.append(None)
    a.append(None)
    a.append(1)
    root = TreeGenerator.get_bin_tree(a)
    TreeHelper.print_tree(root)

    b = [1, 2, 3, None, 4, None, 5]
    root = TreeGenerator.get_bin_tree(b)
    TreeHelper.print_tree(root)

    c = [2, None, 4, None, 6, None, 8, None, 10]
    root = TreeGenerator.get_bin_tree(c)
    TreeHelper.print_tree(root)