#include <iostream>
#include <fstream>
#include <vector>
#include <ranges>
#include <bits/stdc++.h>
#include <set>
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

	std::vector<std::vector<long long>> v;
        for (int i = 0; i < ranges.size(); i++) {
                auto parts = split(ranges[i], '-');
                long long start = std::stoll(parts[0]);
                long long end   = std::stoll(parts[1]);
		v.push_back({start, end});
        }
	
	std::sort(v.begin(), v.end());
	std::vector<std::pair<long long, long long>> merged;
	for(auto &r : v){
		if(merged.empty() || merged.back().second < r[0]){
			merged.push_back(std::make_pair(r[0], r[1]));
		}else{
			long long temp = static_cast<long long>(r[1]);
			merged.back().second = std::max(merged.back().second,temp );
		}
	}

	std::cout << merged.size() << "\n";
	long long total = 0;
    	for (auto &r : merged) {
        	total += r.second - r.first + 1;
    	}

        std::cout << total << std::endl;
        return 0;
}

