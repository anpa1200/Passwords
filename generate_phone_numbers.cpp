#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip> // For std::setfill and std::setw

void generateAndSavePhoneNumbers(const std::string& fileName = "israeli_phone_numbers.txt") {
    // List of common prefixes used by mobile, VoIP, and landline operators in Israel
    std::vector<std::string> prefixes = {"050", "052", "053", "054", "055", "058", "072", "076", "077"};

    // Open the file in write mode to store the phone numbers
    std::ofstream file(fileName, std::ios::out | std::ios::trunc);

    if (!file.is_open()) {
        std::cerr << "Failed to open the file: " << fileName << std::endl;
        return;
    }

    // Iterate over each prefix in the list
    for (const auto& prefix : prefixes) {
        // Generate and write all possible phone numbers for the current prefix
        for (int i = 0; i < 10000000; ++i) { // 7-digit numbers range from 0000000 to 9999999
            file << prefix << std::setfill('0') << std::setw(7) << i << '\n'; // Efficiently format numbers
        }
    }

    std::cout << "All numbers have been saved to " << fileName << std::endl;
    file.close();
}

int main() {
    // Generate and save all phone numbers to a text file
    generateAndSavePhoneNumbers();
    return 0;
}
