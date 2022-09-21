# Integer_to_Roman-
It will convert any positive integer to Roman Numerals. 

Roman numerals are represented by seven different letters: I, V, X, L, C, D, and M which represent the numbers 1, 5, 10, 50, 100, 500, and 1,000 respectively. To include exceptions into consideration, we include some more numbers into fundamental roman numerals i.e. 4, 9, 40, 90, 400, and 900 which is symbolized by IV, IX, XL, XC, CD, CM. 

## Code approach
Divide the input number with the integer equivalent of 12 roman numerals in descending order.
If the division is feasible i.e. quotient is not zero then it means the roman numerical equivalent of the divisor constitutes the resultant roman number.
Output the Roman equivalent of the divisor as many times the quotient value.
Update the input integer value to the remainder of the division.
Repeat the above steps for all 12 fundamental roman numerals as the divisor (If the integer is not zero).
