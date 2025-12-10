#include <iostream>
#include <fstream>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>
#include <cctype>

std::vector<std::string> split(std::string std, char delimiter)
{
        // Using std in a string stream
        std::stringstream ss(std);
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
        std::vector<std::string> lines, op_row;
	std::vector<std::vector<std::string>> cols;
        std::ifstream file("./input");
	long long res = 0;

        while (getline(file, text)) {
                if (text.contains("+") || text.contains("+")) {
			op_row = split(text, ' ');
			continue;
		}
                lines.push_back(text);
        }
	
	int pos=0, temp_pos=0;
	for(int j=0;j<lines[0].size();j++){
		bool space_col=true;
		std::vector<std::string> col;
		for(int k=0;k<lines.size();k++){
			if(lines[k][j] != ' ' && j != lines[0].size()-1) 
				space_col=false;
		}
		temp_pos = pos;
		for(int k=0;k<lines.size() && space_col;k++){
			col.push_back(lines[k].substr(pos, j-pos +1));
			temp_pos = j+1;
		}
		pos = temp_pos;
		if(space_col) 
			cols.push_back(col);
	}
	
	for(auto &r : cols){
		for(auto &w: r){
			std::cout << w << "|\n";
		}
	}
	std::cout << cols.size() << '-' << std::endl;
	for(int i=0;i<cols.size();i++){
		std::string op = op_row[i];
		long temp = 0;
		for(int j=0;j<cols[i][0].size();j++){
			std::string num = "";
			for(int k=0;k<cols[0].size();k++){
				if(cols[i][k][j] != ' ')
					num.push_back(cols[i][k][j]);
			}
			std::cout << num <<std::endl;
			if(num.empty()) continue;
			if(op == "*"){
				temp=(temp) ? temp : 1;
				temp=temp*std::stoi(num);
			}else{
				temp += std::stoi(num);
			}
		}
		res += temp;
	}

	std::cout << res << std::endl;
	return 0;
}
