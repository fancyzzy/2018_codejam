#!/usr/bin/env python3


class solution():

    def leastInterval(tasks, n):

    	task_dict = {x:tasks.count(x) for x in tasks}
    	steps = 0 

    	while 1:

    		most_item = max(task_dict, key=lambda x: task_dict[x])
    		most_num = task_dict[most_item]
    		steps += most_num

    		dissolve_num = (most_num-1) * n
    		steps += dissolve_num

    		task_dict[most_item] = 0


    		#fill the dissovled number
    		while dissolve_num > 0:
	    		second_most = max(task_dict, key=lambda x: task_dict[x])
	    		second_num = task_dict[second_most]

    			#1 the same
    			if second_num == most_num:
    				if dissolve_num >= second_num - 1:
    					task_dict[second_most] = 0
    					dissolve_num -= (second_num - 1)
	    				steps += 1
    				else:
    					print("DEBUG should not happen")
    					task_dict[most_item] = second_num - dissolve_num
    					dissolve_num = 0
    					break

    			#2 less
    			elif second_num < most_num:	
    				if dissolve_num >= second_num:
    					task_dict[second_most] = 0
    					dissolve_num -= second_num
    				else:
    					print("DEBUG should never happen")










        return steps








if __name__ == '__main__':
    pass
