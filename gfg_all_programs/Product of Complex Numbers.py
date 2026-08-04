# Given two arrays A[] and B[] of real and imaginary part of 5 complex numbers, 
# find the product of these five Complex numbers 
# The array A[] contains the real part and B[] contains the imaginary part. 
# So, if A[0] is 5 and B[0] is 4, the complex numbers is (5 + 4i).

class Solution:
    def complexProduct(self, A, B):
        """
        A[i] -> real part of ith complex number
        B[i] -> imaginary part of ith complex number
        We need to multiply 5 complex numbers:
        (A[0] + B[0]i) * (A[1] + B[1]i) * ... * (A[4] + B[4]i)
        """

        # Initialize result as 1 + 0i (identity for multiplication)
        real = 1
        imag = 0

        # Multiply all 5 complex numbers one by one
        for i in range(5):
            # Formula:
            # (a + bi)(c + di) = (ac - bd) + (ad + bc)i

            new_real = real * A[i] - imag * B[i]   # real part
            new_imag = real * B[i] + imag * A[i]   # imaginary part

            # Update result
            real = new_real
            imag = new_imag

        # Return final real and imaginary parts
        return [real, imag]