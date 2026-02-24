class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records: return None
        
    records.sort(key=lambda x: x.record_id)

    if records[-1].record_id != len(records) - 1 or records[0].record_id != 0:
        raise ValueError('Record id is invalid or out of order.')

    nodes = [None] * len(records)
    
    for record in records:
        if record.record_id < record.parent_id:
            raise ValueError('Node parent_id should be smaller than it\'s record_id.')
        
        node = Node(record.record_id)
        nodes[record.record_id] = node
        
        if record.record_id == record.parent_id:
            if record.record_id != 0:
                raise ValueError('Only root should have equal record and parent id.')
            root = node
        else:
            parent_node = nodes[record.parent_id]
            parent_node.children.append(node)

    return root
