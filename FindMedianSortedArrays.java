class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i = 0;
        int j = 0; 
        int[] sum = new int[nums1.length + nums2.length];
        int k = 0;
        for(k = 0; k < nums1.length + nums2.length; k++) {
            if(i == nums1.length && j < nums2.length) {
                sum[k] = nums2[j++];
            }else if(j == nums2.length && i < nums1.length) {
                sum[k] = nums1[i++];
            }else if (nums1[i] <= nums2[j]) {
                sum[k] = nums1[i++];
            }else if (nums1[i] > nums2[j]) {
                sum[k] = nums2[j++];
            }
        }
        if (k % 2 == 0) {
            return (double) (sum[k/2 -1] + sum[k/2]) / 2;
        } else {
            return sum[k/2];
        }
    }
}