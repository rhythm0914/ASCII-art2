# ASCII Art with Colored Text using `pyfiglet`

This Python script generates and prints ASCII art with colored text using the `pyfiglet` library. The script demonstrates how to apply color formatting to text rendered as ASCII art.
# ASCII Art with Colored Text using `pyfiglet`

This Python script demonstrates how to create and print ASCII art with colored text using the `pyfiglet` library.

## Installation

To use this script, you need to install the `pyfiglet` library. You can install it using pip. Run the following command:

```bash
pip install pyfiglet

## Code Overview

1. **Importing Libraries**:
   - The script imports the `Figlet` class from the `pyfiglet` library to create ASCII art.

2. **Color Formatting**:
   - ANSI escape codes are used to color the text:
     - `\033[34m` sets the text color to blue.
     - `\033[0m` resets the text color to the terminal's default.

3. **Generating ASCII Art**:
   - A `Figlet` object is created with the 'small' font.
   - The text "RYAN JOSEPH" is converted to ASCII art.

4. **Output**:
   - The ASCII art is printed in blue using the defined color formatting.

### Code

```python
from pyfiglet import Figlet

# Define ANSI escape codes for blue color and reset
blue = '\033[34m'
reset = '\033[0m'

# Initialize Figlet with a specific font
figlet = Figlet(font='small')

# Define the text to convert to ASCII art
text = "RYAN JOSEPH"

# Generate ASCII art
ascii_art = figlet.renderText(text)

# Print the ASCII art in blue color
print(f"{blue}{ascii_art}{reset}")
