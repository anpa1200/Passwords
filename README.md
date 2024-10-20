# Personal Pass Generator

## Description
The Personal Pass Generator (PPG) is an advanced tool designed for security professionals and ethical hackers to create extensive, personalized lists of potential passwords. This tool is especially useful for conducting penetration tests or security assessments where custom or brute-force attacks might be necessary.

### Key Features:
- **Extensive Password Lists**: PPG can generate password lists that are unusually large—ranging from 1GB to over 30GB—tailored to specific security testing scenarios.
- **Customization Options**: Users can specify various parameters including the inclusion of symbols, alphanumeric characters, and more, allowing for highly customized password sets that are adapted to the target environment or system characteristics.
- **Efficiency and Scalability**: The tool is optimized for efficient generation of large datasets while allowing users to scale the output based on their storage and processing capabilities.

### How It Works:
PPG employs a combination of standard and advanced cryptographic principles, utilizing permutations and combinations of characters from predefined sets (including special characters, numbers, and letters). This approach ensures that the generated passwords are both random and comprehensive, covering a wide range of possible password combinations that might be used by an individual or organization.

### Applications:
- **Security Testing**: Ideal for penetration testers and red teams needing custom password lists to test the resilience of systems to password cracking.
- **Research and Development**: Useful for researchers studying password security and the effectiveness of password policies.
- **Training and Workshops**: Can be used in educational settings to demonstrate the importance of strong password policies and the potential vulnerabilities of weak passwords.

## Requirements
- Python 3.x

## Usage
To use the Personal Pass Generator, simply run the script in your Python environment:

# Critical Information on Resource Usage
### When utilizing the Personal Pass Generator (PPG) with all functions enabled and with a complete set of input information, the process can be extremely resource-intensive. Generating comprehensive password lists based on extensive input can
### result in very large data volumes, potentially occupying up to 4 TB of disk space. Moreover, the generation process can be significantly time-consuming due to the complexity and size of the data being processed.

## Recommendation for Efficient Use:
To optimize the performance and manage the disk space efficiently, it is recommended to limit the input data to between 2 to 5 entries. This approach balances the comprehensiveness of the password lists with practical resource usage, making the tool more manageable and effective for typical penetration testing scenarios.

By focusing on a smaller set of highly relevant inputs, you can still achieve substantial password list coverage without overwhelming your system's storage and processing capabilities.



## Author
Andrey Pautov - 1200km@gmail.com
License
This project is licensed see the LICENSE.md file for details.
