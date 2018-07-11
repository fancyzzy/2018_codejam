#!/usr/bin/env python3
# Q2, Share Candy
# Solution:
# 1, res = 0. if ascending order, the value += 1, res += value.
# if comes to a less or equal item then ascending order conituing, value = 1, res += value
# 2, if encounter consetive more thant two items in desceding order, then the first descending 
# value of the item should be compensated with len_descrease - value and other descending items' value 
# shoule equal to the descending counting sequence number.

class Solution():
    def share_candy(self, ratings):

        res = 0
        decrease_len = 0

        item = None
        value = 0
        prior_item = None
        prior_value = 0

        first_decrease_value = 0

        DEBUG_LIST = []

        #print(ratingsL)
        for item in ratings:
            #print("DEBUG prior_item: {}, item: {}".format(prior_item, item))
            #the beginning one
            if value == 0:
                value = 1
                res += value
                DEBUG_LIST.append(value)
                #print("1 DEBUG_LIST:{}".format(DEBUG_LIST))
            else:
                if item < prior_item:
                    #record the value of the first descending item
                    if decrease_len == 0:
                        first_decrease_value = prior_value
                        decrease_len = 2
                    else:
                        decrease_len += 1
                    value = 1

                else:
                    if item > prior_item:
                        value = prior_value + 1
                    if item == prior_item:
                        value = 1

                    if decrease_len != 0:
                        #compensate for the first descending item:
                        compen_value = decrease_len - first_decrease_value
                        if compen_value > 0:
                            res += compen_value 
                            #print("before compen, DEBUG_LIST:{}".format(DEBUG_LIST))
                            DEBUG_LIST[-1] += compen_value
                            #print("4, after compensate, DEBUG_LIST: {}".format(DEBUG_LIST))
                        #add the descending counting sequence number for those descending item
                        #5,4,3,2,1 -> 4,3,2,1 counting sequence = 1+2+3+4 from d_len=5, (1+ d_len - 1)*(d_len-1)//2
                        res += decrease_len *(decrease_len-1)//2
                        prior_value = 1
                        DEBUG_LIST.extend([x for x in range(decrease_len-1,0,-1)])
                        #print("3 DEBUG_LIST:{}".format(DEBUG_LIST))
                        decrease_len = 0


                    res += value
                    DEBUG_LIST.append(value)
                    #print("2 DEBUG_LIST:{}".format(DEBUG_LIST))
            prior_item = item
            prior_value = value


        #The last descending one not invlove in above for circle:
        if decrease_len > 0:
            #compensate for the first descending item:
            compen_value = decrease_len - first_decrease_value
            if compen_value > 0:
                res += compen_value 
                #print("9 before compen, DEBUG_LIST:{}".format(DEBUG_LIST))
                DEBUG_LIST[-1] += compen_value
                #print("10, after compensate, DEBUG_LIST: {}".format(DEBUG_LIST))
            #add the descending counting sequence number for those descending item
            #5,4,3,2,1 -> 4,3,2,1 counting sequence = 1+2+3+4 from d_len=5, (1+ d_len - 1)*(d_len-1)//2
            res += decrease_len *(decrease_len-1)//2
            prior_value = 1
            DEBUG_LIST.extend([x for x in range(decrease_len-1,0,-1)])
            #print("11 DEBUG_LIST:{}".format(DEBUG_LIST))
            decrease_len = 0



        #print("DEBUG LIST: {}".format(DEBUG_LIST))

        return res
##########class Solution()################


if __name__ == '__main__':

    #L = "1 3 7 5 4 3 1 3 8 6 5 4 1 12"

    L = input()
    L = [int(x) for x in L.split()]
    sol = Solution()
    res = sol.share_candy(L)
    print(res)

