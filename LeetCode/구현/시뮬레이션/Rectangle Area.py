class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int,
                          E: int, F: int, G: int, H: int) -> int:

        # 하나의 직사각형 넓이 계산
        def rect_area(x1, y1, x2, y2):
            return max(0, x2 - x1) * max(0, y2 - y1)

        # 두 구간의 1차원 겹침 길이 계산
        def overlap_length(a1, a2, b1, b2):
            return max(0, min(a2, b2) - max(a1, b1))

        # 각 직사각형의 넓이
        area1 = rect_area(A, B, C, D)
        area2 = rect_area(E, F, G, H)

        # X축, Y축에서 겹치는 길이를 구한다
        overlap_w = overlap_length(A, C, E, G)
        overlap_h = overlap_length(B, D, F, H)

        # 겹치는 전체 넓이
        overlap = overlap_w * overlap_h

        # 전체 넓이 = 각 넓이 합 - 겹침
        return area1 + area2 - overlap
