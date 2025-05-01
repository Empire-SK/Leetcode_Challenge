int returnToBoundaryCount(int *nums, int numsSize)
{
    int position = 0;
    int boundarycount = 0;

    for (int i = 0; i < numsSize; i++)
    {
        position += nums[i];

        if (position == 0)
        {
            boundarycount++;
        }
    }
    return boundarycount;
}