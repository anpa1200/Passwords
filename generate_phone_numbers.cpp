/**
 * Israeli phone number list generator (C++).
 * Generates numbers for common Israeli mobile/VoIP/landline prefixes.
 * For authorized security/testing use only.
 *
 * Build: make
 * Usage: ./generate_phone_numbers [output_file]
 */

#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

namespace {

const std::vector<std::string> kPrefixes = {"050", "052", "053", "054", "055",
                                             "058", "072", "076", "077"};
const int kDigitsAfterPrefix = 7;
const int kMaxNumber = 10000000;  // 10^7

}  // namespace

bool generateAndSavePhoneNumbers(const std::string& file_name) {
    std::ofstream file(file_name, std::ios::out | std::ios::trunc);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open " << file_name << std::endl;
        return false;
    }

    for (const auto& prefix : kPrefixes) {
        for (int i = 0; i < kMaxNumber; ++i) {
            file << prefix << std::setfill('0') << std::setw(kDigitsAfterPrefix)
                 << i << '\n';
        }
    }

    std::cout << "Saved to " << file_name << std::endl;
    return true;
}

int main(int argc, char* argv[]) {
    std::string output = "israeli_phone_numbers.txt";
    if (argc >= 2) {
        output = argv[1];
    }
    return generateAndSavePhoneNumbers(output) ? 0 : 1;
}
