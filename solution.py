from math import sqrt
from typing import List, Optional, Tuple


class Node:
    width = 0
    
    def __init__(self, frm: int, to: int, subsulution: Tuple[Optional["Node"] , Optional["Node"]]):
        self.frm = frm
        self.to = to
        self.subsulution = subsulution
        self.length = [0.0, 0.0]
        
        length = self._calc(frm - to)
        
        for i in  range(2):
            if self.subsulution[i] is None:
                self.length[i] = length
            else:
                self.length[i] = length + max(*self.subsulution[i].length)

    def _calc(self, len: int) -> float:
        return sqrt(len**2 + Node.width**2)


class Solution:
    def __init__(self, list: List[int], width: int):
        self.list = list
        self.width = width

    def calculate_max_len(self):
        Node.width = self.width
        outmn, outmx = self._cal_rec(0)

        mx = 0
        for i in [*outmn, *outmx]:
            for j in i.length:
                if mx < j:
                    mx = j

        return mx

    def _cal_rec(self, index):
        ls = len(self.list) - 1
        if index == ls - 1:
            return ((
                Node(1, 1, (None, None)),
                Node(1, self.list[ls], (None, None)),
            ), (
                Node(self.list[ls-1], 1, (None, None)),
                Node(self.list[ls-1], self.list[ls], (None, None)),
            ))
        else:
            for1, form = self._cal_rec(index + 1)
            out = ((
                Node(1, 1, for1),
                Node(1, self.list[index+1], form),
            ), (
                Node(self.list[index], 1, for1),
                Node(self.list[index], self.list[index+1], form),
            ))
            return out



