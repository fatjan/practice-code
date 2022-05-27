const maxValue = (nums) => {
    // todo
    let largest = nums[0];
    for (let i in nums) {
        if (largest < nums[i]) {
        largest = nums[i];
        }
    }
    return largest;
};
  
console.log(maxValue([1,3,4,2,6,9,11,19,14,29,12]));
