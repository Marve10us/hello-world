class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] in nums[i:]:
                m = []
                yo = nums[i+1:]
                for n in range(len(yo)):
                    if yo[n] == nums[i]:
                        m.append(n+i+1)
                
                for j in m:
                    abs_diff = abs(j - i) #j是第一个重复的
                    if abs_diff <= k:
                        return True
                    
        return False

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().containsNearbyDuplicate(nums, k)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
