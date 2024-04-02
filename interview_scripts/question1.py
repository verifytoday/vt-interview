"""
Write a Python function compress_string that takes a string as input
and returns a compressed version of the string using the counts of repeated characters.

The function should only compress the string if it results in a shorter length than the original.
Use the format character followed by the count of that character
to represent a compressed segment.
If a character appears only once, it should be left as is.


Example Inputs and Outputs:
Input: "aabcccccaaa"
Output: "a2b1c5a3"

Input: "abcdef"
Output: "abcdef"


Explanation:
For "aabcccccaaa", instead of returning "a2bc5a3", it returns "a2b1c5a3" because each character
count should be included even if it's 1.
For "abcdef", the compressed string would be longer than the original,
so it returns the original string.


Extra:
How does your solution handle strings with mixed case letters or non-alphabetic characters?
Can your solution be optimized for space or time complexity?
How would you modify your solution to handle large input strings efficiently?

"""