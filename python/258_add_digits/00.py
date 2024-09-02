class Solution:
    def addDigits(self, num: int) -> int:
        
        def sum_digits(new_num):
            sum = 0
            for i in range(1, len(str(new_num)))[::-1]:
                digit = new_num % (10 ** i)
                new_num = new_num // (10 ** i)
                sum += digit
            sum += new_num
            return sum

        reduced_digits = num
        while reduced_digits > 9:
            reduced_digits = sum_digits(reduced_digits)

        return reduced_digits
