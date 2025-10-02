def reverse(text, left, right):
    if left >= right:
        return text
    # Convert string to list since strings are immutable
    text_list = list(text)
    # Swap characters
    text_list[left], text_list[right] = text_list[right], text_list[left]
    # Convert back to string and continue recursion
    return reverse(''.join(text_list), left + 1, right - 1)

def check_palindrome(text):
    temp = text
    reversed_text = reverse(temp, 0, len(text) - 1)
    return reversed_text == text

text = input("Enter a string: ")
if check_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")