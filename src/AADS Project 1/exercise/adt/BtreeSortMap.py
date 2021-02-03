from TdP_collections.hash_table.sorted_table_map import SortedTableMap

class BtreeSortMap(SortedTableMap):

    def set_at_index(self, index, value):
        self._table[index]._value = value

    def get_index(self, key):
        return self._find_index(key, 0, len(self._table) - 1)

    def get_at_index(self, index):
        if index < len(self):
            item = self._table[index]
            return item._key, item._value
        else:
            return None
