# Passwords toolkit - build and run
# C++ phone number generator (optional)

CXX     ?= g++
CXXFLAGS = -Wall -Wextra -std=c++17 -O2
TARGET   = generate_phone_numbers

.PHONY: all clean cpp help

all: cpp

help:
	@echo "Targets:"
	@echo "  make cpp   - build C++ phone number generator ($(TARGET))"
	@echo "  make clean - remove build artifacts"

cpp: $(TARGET)

$(TARGET): generate_phone_numbers.cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) generate_phone_numbers.cpp

clean:
	rm -f $(TARGET) *.o
