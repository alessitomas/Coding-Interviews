class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


# 4    3    2    1 
# 3 -> 2 -> 5 -> 1 -> None


# 1
# 3 -> None

def nth_to_last(head: Node, k: int) -> Node:
    if head is None:
        return None
    
    aux_head = head
    
    for _ in range(k-1):
        if aux_head is None:
            return None
        aux_head = aux_head.next

    cur = head

    while aux_head.next is not None:
        aux_head = aux_head.next
        cur = cur.next 

    return cur
    

