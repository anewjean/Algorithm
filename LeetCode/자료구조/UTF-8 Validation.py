class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        n = len(data)
        
        while i < n:
            byte = data[i]
            
            # 1) 시작 바이트를 보고 UTF-8 문자의 전체 길이 결정
            if byte <= 0x7F:                 # 0xxxxxxx (1바이트 문자)
                length = 1
            elif 0xC0 <= byte <= 0xDF:       # 110xxxxx (2바이트 시작)
                length = 2
            elif 0xE0 <= byte <= 0xEF:       # 1110xxxx (3바이트 시작)
                length = 3
            elif 0xF0 <= byte <= 0xF7:       # 11110xxx (4바이트 시작)
                length = 4
            else:
                # 잘못된 UTF-8 시작 바이트
                return False

            # 2) 문자의 전체 길이가 data 범위를 넘어가면 x
            if i + length > n:
                return False
            
            # 3) 이어지는 바이트들이 모두 10xxxxxx (128~191) 범위인지 확인
            for j in range(i + 1, i + length):
                if not (0x80 <= data[j] <= 0xBF):
                    return False
            
            # 4) 현재 문자의 전체 바이트만큼 건너뛰고 다음 문자 확인
            i += length
        
        return True
