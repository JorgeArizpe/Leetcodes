class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> seen_chars;
        int start = 0;
        int max_len = 0;

        for (int end = 0; end < s.length(); ++end) {
            while (seen_chars.find(s[end]) != seen_chars.end()) {
                seen_chars.erase(s[start]);
                ++start;
            }
            seen_chars.insert(s[end]);
            max_len = std::max(max_len, end - start + 1);
        }

        return max_len;
    }
};