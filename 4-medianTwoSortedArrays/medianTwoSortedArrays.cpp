class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size() + nums2.size();
        vector<double> final(n);
        for (int i = 0; i < n; i++)
        {
            if (nums1.empty() || (!nums2.empty() && nums1.front() > nums2.front()))
            {
                final[i] = nums2.front();
                nums2.erase(nums2.begin());
            }
            else
            {
                final[i] = nums1.front();
                nums1.erase(nums1.begin());
            }
        }
        int size = final.size();
        if (size % 2 == 0)
        {
            return (final[size/2] + final[(size/2) - 1])/2.0;
        }
        else
        {
            return final[size/2];
        }
    }
};