#include <iostream>
#include <fstream>
#include <vector>
#include <ranges>
#include <bits/stdc++.h>

std::vector<std::string> split(std::string str, char delimiter)
{
  // Using str in a string stream
    std::stringstream ss(str);
    std::vector<std::string> res;
    std::string token;
    while (getline(ss, token, delimiter)) {
        res.push_back(token);
    }
    return res;
}

int main() {

        std::string text;
        std::vector<std::string> ranges, ids;
        std::ifstream file("./input");

        while (getline(file, text)) {
                if (text == "") break;
                ranges.push_back(text);
        }
        while (getline(file, text)) {
                ids.push_back(text);
        }

        std::vector<std::vector<long long>> v;  // stores {start, end}

        for (int i = 0; i < ranges.size(); i++) {
                auto parts = split(ranges[i], '-');
                long long start = std::stoll(parts[0]);
                long long end   = std::stoll(parts[1]);
                v.push_back({start, end});
        }

        int fresh_counter = 0;

        for (int j = 0; j < ids.size(); j++) {
                long long id = std::stoll(ids[j]);
                bool is_valid = false;

                for (int i = 0; i < v.size(); i++) {
                        if (id >= v[i][0] && id <= v[i][1]) {
                                is_valid = true;
                                break;
                        }
                }

                if (is_valid) fresh_counter++;  // count fresh IDs
        }

        std::cout << fresh_counter << std::endl;
        return 0;
}

