from collections import Counter
import re
import random

# HTML content provided
html_content = """

<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
	
	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
python_class_question.html
Displaying python_class_question.html.
"""

# Extract colors from HTML using regex
colors_match = re.findall(r'(?<=<td>)[\w, ]+(?=<\/td>)', html_content)

# Print colors_match for debugging
print("Colors Match:", colors_match)

# Convert matched colors to a flat list
colors = [color.strip().upper() for color_list in colors_match for color in color_list.split(',')]

# Check if colors list is empty
if not colors:
    print("No colors found. Please check the HTML content.")
    exit()

# 1. Which color of shirt is the mean color?
mean_color = max(set(colors), key=colors.count)

# 2. Which color is mostly worn throughout the week?
most_worn_color = Counter(colors).most_common(1)[0][0]

# 3. Which color is the median?
sorted_colors = sorted(colors)
median_color = sorted_colors[len(sorted_colors) // 2]

# 4. BONUS: Get the variance of the colors
color_counts = Counter(colors)
variance = sum((count - len(colors) / len(set(colors)))**2 for color, count in color_counts.items()) / len(set(colors))

# 5. BONUS: If a color is chosen at random, what is the probability that the color is red?
red_probability = color_counts.get('RED', 0) / len(colors)

# Display results
print("1. Mean Color:", mean_color)
print("2. Most Worn Color:", most_worn_color)
print("3. Median Color:", median_color)
print("4. Variance of Colors:", variance)
print("5. Probability of Choosing Red:", red_probability)

# 7. BONUS: Write a recursive searching algorithm to search for a number entered by the user in a list of numbers.
def recursive_search(lst, target, index=0):
    if index == len(lst):
        return -1  # Not found
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_number = int(input("Enter a number to search in the list: "))
result = recursive_search(numbers_list, target_number)
print("Index of", target_number, "in the list:", result)

# 8. Generate random 4 digits number of 0s and 1s and convert to base 10
random_binary_number = ''.join(random.choice(['0', '1']) for _ in range(4))
decimal_number = int(random_binary_number, 2)
print("Random Binary Number:", random_binary_number)
print("Equivalent Decimal Number:", decimal_number)

# 9. Sum the first 50 Fibonacci sequence
fibonacci_sequence = [0, 1]
for i in range(2, 50):
    fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

sum_fibonacci = sum(fibonacci_sequence)
print("Sum of the first 50 Fibonacci sequence:", sum_fibonacci)
