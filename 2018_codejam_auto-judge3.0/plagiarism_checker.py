#!/usr/bin/env python
# -*- coding=utf-8 -*-


import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from itertools import combinations
from time import sleep

class Plagiarism_Checker():
    '''
    Use FuzzyWuzzy which instantializes Levenshtein Distance algorithm to 
    detect if two code files are similarity.
    '''
    def __init__(self):
        self.file_type = ['python','c','cpp','java','txt']
        self.ratio_boundary = 60
        self.report = []
        print("ration_boundary = {}".format(self.ratio_boundary))

    def two_two_combine(self, file_list):
        '''
        Like the name, every two files get into a pair
        '''
        #Too many elements there and sublime ide crash once display them all
        #return  list(combinations(file_list,2))
        return  combinations(file_list,2)


    def check_folder(self, path):
        '''
        Check files in this folder if there is plagiarism
        And list out the ranked file names.
        '''
        all_group = self.classify_files_by_type(path)
        print("DEBUG all_group: {}".format(all_group))
        self.report = []

        sim_ration = None
        for group in all_group:
            if len(group) > 1:
                combined_list =  self.two_two_combine(group)
                for pair in combined_list:
                    sim_ratio = self.check_plagiarism(os.path.join(path,pair[0]),\
                        os.path.join(path,pair[1]))
                    sub_re = (pair[0], pair[1], sim_ratio)
                    self.report.append(sub_re)
                    #print("{:<40} {:<40} {:<20}".format(*sub_re))
                    #sleep(0.2)

        #print("DEBUG report: {}".format(report))                
        return [x for x in self.report if x[2] >= self.ratio_boundary]


    def get_top_sim(self, n):
        return sorted(self.report, key=lambda x:x[2], reverse=True)[:n]


    def classify_files_by_type(self, path):
        '''
        Put files into different groups according to their types
        '''
        if not os.path.exists(path):
            return None

        all_group = []
        python_list = []
        c_cpp_list = []
        java_list = []
        text_list = []

        for item in os.listdir(path):
            file_path = os.path.join(path, item)
            if os.path.isfile(file_path):
                if item.endswith('.py'):
                    python_list.append(item)
                elif item.endswith('.java'):
                    java_list.append(item)
                elif item.endswith('.c') or item.endswith('.cpp'):
                    c_cpp_list.append(item)
                elif item.endswith('.txt'):
                    text_list.append(item)
                elif item.endswith('.exe') or '.' not in item:
                    continue
                else:
                    continue
                    #text_list.append(item)


        all_group.append(python_list)
        all_group.append(c_cpp_list)
        all_group.append(java_list)
        all_group.append(text_list)

        return all_group


    def check_plagiarism(self, file_a, file_b):

        str_a = None
        str_b = None
        sim_ratio = None
        try:
            with open(file_a, 'r') as fa:
             str_a = fa.read()

            with open(file_b, 'r') as fb:
             str_b = fb.read()
        except Exception as e:
            print("error read file, {}".format(e))
            return False

        sim_ratio = self.get_similarity_ratio(str_a, str_b)
        #print("DEBUG ratio = {}".format(sim_ratio))

        return sim_ratio


    def check_file(self, file_a, file_b):

        sim_ratio = self.check_plagiarism(file_a, file_b)
        if sim_ratio > self.ratio_boundary:
            return True
        else:
            return False


    def get_similarity_ratio(self, str_a, str_b):
            return fuzz.ratio(str_a, str_b)


    def rank_file_by_ratio(self):
        '''
        List and rank the highest to lowest similar ratio file pairs
        '''
        pass

###########Class Plagiarism_Checker()##########################


if __name__ == '__main__':

    file_a = r'D:\My_Project\Code_Jam\2018_codejam\2018_7\Q1\exe\SherryRen_q1(3.4).py'
    file_b = r'D:\My_Project\Code_Jam\2018_codejam\2018_7\Q1\exe\tracy Lou_py3_win64_q1.py'
    file_b = r'D:\My_Project\Code_Jam\2018_codejam\2018_7\Q1\exe\SherryRen_Copy.py'
    path = r'D:\My_Project\Code_Jam\2018_codejam\2018_7\Q1\exe'
    path = r'D:\My_Project\Code_Jam\2018_codejam\2018_7\Q2\exe'

    pc = Plagiarism_Checker()
    ''' 
    if pc.check_file(file_a, file_b):
        print("DEBUG These two file are simaliar!")
    else:
        print("Debug No problem.")
    '''


    sim_pairs = pc.check_folder(path)
    print("sim_paris = {}".format(sim_pairs))
    print(pc.get_top_sim(10))

    print("Done.")
 