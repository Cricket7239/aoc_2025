#include <iostream>
#include <fstream>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>
#include <cctype>

std::vector<std::string> split(std::string str, char delimiter)
{
        // Using str in a string stream
        std::stringstream ss(str);
        std::vector<std::string> res;
        std::string token;
        while (getline(ss, token, delimiter)) {
                res.push_back(token);
        }
	res.erase(
    		std::remove_if(res.begin(), res.end(),[](std::string& s) { return s.empty(); }),
    		res.end()
	);
        return res;
}

int main(){
	std::string text;
        std::vector<std::string> lines, op_lines;
	std::vector<std::vector<std::string>> rows, op_rows;
        std::ifstream file("./input");

        while (getline(file, text)) {
                if (text.contains("+") || text.contains("+")) {
			op_lines.push_back(text);
			continue;
		}
                lines.push_back(text);
        }

	for(int i=0;i<lines.size();i++){
		rows.push_back(split(lines[i], char(' ')));
	}
	for(int i=0;i<op_lines.size();i++){
		op_rows.push_back(split(op_lines[i], char(' ')));
	}	
	for(auto &r : rows){
		for(auto &w: r){
			std::cout << w << "\n";
		}
	}
	long res = 0;
	for(int i=0;i<rows[0].size();i++){
		long long temp_res = 0;
		std::string op = op_rows[0][i];
		for(int j=0;j<rows.size();j++){
			std::cout << op << temp_res << std::endl;
			if(op == "*"){
				temp_res = (temp_res > 0) ? temp_res : 1;
				int temp = std::stoi(rows[j][i]);
				temp_res=temp_res*temp;	
			}else{
				int temp = std::stoi(rows[j][i]);
				temp_res+=temp;
			}
			
		}
		std::cout << "--" << temp_res << std::endl;
		res+=temp_res;
	}
	std::cout << res << std::endl;
	return 0;
}
