from TdP_collections.tree.tree import Tree
from exercise.adt.b_node import BTreeNode


class BTree(Tree):
    class Position(Tree.Position):
        def __init__(self, T, node):
            self._T = T
            self._node = node

        def element(self):
            return self._node

        def container(self):
            return self._T

        def map(self):
            return self._node.get_map()

        def children(self):
            return self._node.get_children()

    def _make_position(self, node):
        if node is None:
            return None
        else:
            return self.Position(self, node)

    def _validate(self, pos):
        if not isinstance(pos, self.Position):
            raise TypeError("pos is not a Position type.")

        if pos.container() is not self:
            raise ValueError("pos does not belong to this container.")
        return pos.element()

    __slots__ = '_root', '_b', '_size'

    def __init__(self, root=None, b=6):
        self._root = root
        self._b = b
        self._size = 0

    def root(self):
        return self._make_position(self._root)

    def num_children(self, p):
        return len(p.children())

    def children(self, p):
        for i in p.children():
            yield self._make_position(i)

    def b_dimension(self):
        return self._b

    def __len__(self):
        return self._size

    def search(self, key, pos):
        node = self._validate(pos)
        if self.is_empty():
            return None
        index = node.get_index(key)
        temp = node.get_at_index(index)
        if self.is_leaf(pos):
            if temp is not None:
                if temp[0] == key:
                    return temp[1]
                else:
                    return None
            if temp is None:
                return None
        children = node.get_children()
        if temp is not None:
            if temp[0] == key:
                return temp[1]
        return self.search(key, self._make_position(children[index]))

    def _insert_recursive(self, key, value, position):
        node = self._validate(position)

        if self.is_leaf(position):
            node.insert_element(key, value)
        else:
            index = node.get_index(key)
            result = node.get_at_index(index)
            if result is not None:
                if result[0] == key:
                    node.set_at_index(index, value)
                    return None
            children = node.get_children()
            returned_position = self._insert_recursive(key, value, self._make_position(children[index]))
            if returned_position is not None:
                returned_node = self._validate(returned_position)
                key, value = returned_node.get_at_index(0)
                node.insert_element(key, value)
                returned_node.delete_element(key)
                node.set_child(returned_node)
        if len(node) is self._b:
            return self._split(position)
        else:
            return None

    def insert(self, key, value):
        if self.is_empty():
            self._root = BTreeNode()
        root_position = self.root()

        result_position = self._insert_recursive(key, value, root_position)
        self._size += 1
        if result_position is not None:
            new_root = BTreeNode()
            left_node = self._validate(root_position)
            right_node = self._validate(result_position)
            first_element = right_node.get_at_index(0)
            new_root.insert_element(first_element[0], first_element[1])
            right_node.delete_element(first_element[0])
            new_root.set_child(right_node)
            new_root.set_child(left_node)
            self._root = new_root

    def _split(self, position_to_split):
        node_to_split = self._validate(position_to_split)
        new_node = BTreeNode()
        index_middle = int(self._b / 2)

        for i in range(index_middle, len(node_to_split)):
            key, value = node_to_split.get_at_index(i)
            new_node.insert_element(key, value)
        for i in range(len(node_to_split) - 1, index_middle - 1, -1):
            key, value = node_to_split.get_at_index(i)
            node_to_split.delete_element(key)
        children = position_to_split.children()
        for i in range(index_middle + 1, len(children)):
            child = children[i]
            new_node.set_child(child)
        for i in range(len(children) - 1, index_middle, -1):
            node_to_split.pop_child(i)
        return self._make_position(new_node)

    def delete(self, key, start_position=None):
        if self.is_empty():
            return False
        if start_position is None:
            start_position = self.root()
        pos, parent, element_index, position_index = self._search_for_delete(key, start_position, None, None)
        if pos is not None:
            node = self._validate(pos)
            if len(node) > int((self._b-1) / 2) or parent is None:
                if self.is_leaf(pos):
                    node.delete_element(key)
                    return True
                else:
                    children = node.get_children()
                    children_pos = self._make_position(children[element_index+1])
                    successor = self._find_successor(children_pos)
                    node.delete_element(key)
                    node.insert_element(successor[0], successor[1])
                    self.delete(successor[0], children_pos)
                    return True
            else:
                parent_node = self._validate(parent)
                return self._manage_underflow(pos, parent_node, key, position_index)
        else:
            return False

    def _find_successor(self, position):
        node = self._validate(position)
        if self.is_leaf(position):
            return node.get_at_index(0)
        else:
            children = node.get_children()
            children_pos = self._make_position(children[0])
            return self._find_successor(children_pos)

    def _search_for_delete(self, key, pos, parent, pos_index):
        node = self._validate(pos)
        if self.is_empty():
            return None, None, None, None
        element_index = node.get_index(key)
        temp = node.get_at_index(element_index)
        if self.is_leaf(pos):
            if temp is not None:
                if temp[0] == key:
                    return pos, parent, element_index, pos_index
                else:
                    return None, None, None, None
            else:
                return None, None, None, None
        children = node.get_children()
        if temp is not None:
            if temp[0] == key:
                return pos, parent, element_index, pos_index
        return self._search_for_delete(key, self._make_position(children[element_index]), pos, element_index)


    def _manage_underflow(self, position, parent_node, key, position_index):
        left_position = position_index-1
        position_node = self._validate(position)
        if left_position >= 0:
            brother_node = parent_node.get_children()[left_position]
            if len(brother_node) > int((self._b-1) / 2):
                k_second = brother_node.get_at_index(len(brother_node)-1)
                self._transfer(position,parent_node,k_second,left_position)
                brother_node.delete_element(k_second[0])
                position_node.delete_element(key)
                return True
        right_position = position_index+1
        if right_position < len(parent_node.get_children()):
            brother_node = parent_node.get_children()[right_position]
            if len(brother_node) > int((self._b-1) / 2):
                k_second = brother_node.get_at_index(0)
                self._transfer(position,parent_node,k_second,position_index)
                brother_node.delete_element(k_second[0])
                position_node.delete_element(key)
                return True
        if left_position >= 0:
            brother_node = parent_node.get_children()[left_position]
            self._fusion(parent_node, left_position, brother_node, position_node)
            brother_node.delete_element(key)

        else:
            brother_node = parent_node.get_children()[right_position]
            self._fusion(parent_node, position_index, position_node, brother_node)
            position_node.delete_element(key)
        return True

    def _transfer(self, position, parent_node, k_second, left_child_index):
        k_parent = parent_node.get_at_index(left_child_index)
        position_node = self._validate(position)
        position_node.insert_element(k_parent[0], k_parent[1])
        parent_node.delete_element(k_parent[0])
        parent_node.insert_element(k_second[0], k_second[1])

    def _fusion(self, parent_node, i, child_left, child_right):
        for index in range(0, len(child_right)):
            item = child_right.get_at_index(index)
            child_left.insert_element(item[0], item[1])
        children_of_child_right = child_right.get_children()
        for index in range(0, len(children_of_child_right)):
            child_left.set_child(children_of_child_right[index])
        item_parent = parent_node.get_at_index(i)
        child_left.insert_element(item_parent[0], item_parent[1])
        parent_node.delete_element(item_parent[0])
        parent_node.pop_child(i + 1)

    def print_structure_tree(self, position = None, level=0):
        if position is None:
            position = self.root()
        node = self._validate(position)
        print("Node(s) at level: ", level)
        print("     Keys:", node.list_keys())
        position = self._make_position(node)
        for child in position.children():
            self.print_structure_tree(self._make_position(child), level + 1)

    def print_tree(self):
        i = 0
        for p in self.breadthfirst():
            if not self.is_leaf(p):
                p.element().print_branch(i)
                i += 1
