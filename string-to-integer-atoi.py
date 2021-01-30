    def myAtoi(self, s: str) -> int:
        potential_num = s.split()
        if not potential_num:
            return 0
        num_string = potential_num[0]
        pos_or_neg = 1
        max_int = 2 ** 31 - 1
        max_int_negative = - 2 ** 31
        result = 0
        
        for i in range(len(num_string)):
            if i == 0 and num_string[i] in ['+', '-']:
                if num_string[i] == '-':
                    pos_or_neg = -1
                continue
            
            if num_string[i] not in '0123456789':
                return result
            
            result = result * 10 + pos_or_neg * int(num_string[i])
            if pos_or_neg == 1 and result >= max_int:
                return max_int
            if pos_or_neg == -1 and result <= max_int_negative:
                return max_int_negative
        
        return result