#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os
from abc import abstractmethod


class My_Counter():
    def __init__(self):
        pass
        self.python_counter = Python_Counter()
        self.c_cpp_counter = C_Cpp_Counter()
        self.java_counter = Java_Counter()
        self.txt_counter = Txt_Counter()

    def count_lines(self, file):
        #print("DEBUG file: {}".format(file))
        if file.endswith('.py'):
            return self.python_counter.count_line(file)

        elif file.endswith('.cpp') or file.endswith('.c'):
            return self.c_cpp_counter.count_line(file)

        elif file.endswith('.java'):
            return self.java_counter.count_line(file)

        elif file.endswith('.txt'):
            return self.txt_counter.count_line(file)

        elif file.endswith('.exe') or file.endswith('.o') or\
        file.endswith('.pyc'):
            return 'N/A'

        else:
            return self.txt_counter.count_line(file)

###########Class My_Counter()##########################


class Counter():
    '''
    Just an interface class
    '''

    @abstractmethod
    def count_line(self, file):
        '''
        implement this method
        '''

class Python_Counter(Counter):
    def __init__(self):
        pass

    def count_line(self, file):

        total_line = 0
        blank_line = 0
        note_line = 0

        start_note = False

        with open(file, 'r') as f:
            #for line in f.readlines():
            for line in f:

                total_line += 1

                #blank lines
                if not line.split():
                    blank_line += 1
                    continue

                #noted lines:
                if start_note:
                    note_line += 1
                    if line.strip().startswith("'''") or\
                    line.strip().startswith("\"\"\""):
                        start_note = False

                    if (line.strip().endswith("'''") or\
                        line.strip().endswith("\"\"\"")) and\
                        (line.strip()) > 3:
                        start_note = False
                else:
                    if line.strip().startswith("'''") or\
                    line.strip().startswith("\"\"\""):
                        start_note = True
                        note_line += 1

                    if (line.strip().endswith("'''") or\
                        line.strip().endswith("\"\"\"")) and\
                        len(line.strip()) > 3:
                        start_note = False


                    elif line.strip().startswith('#'):
                        note_line += 1
                    else:
                        continue

        print("python, total_line: {}, blank_line: {}, note_line: {}".format(total_line, blank_line, note_line))
        return total_line - blank_line - note_line


class C_Cpp_Counter(Counter):
    def __init__(self):
        pass

    def count_line(self, file):

        total_line = 0
        blank_line = 0
        note_line = 0

        start_note = False

        with open(file, 'r') as f:
            for line in f:

                total_line += 1

                #blank lines
                if not line.split():
                    blank_line += 1
                    continue

                #noted lines:
                if start_note:
                    note_line += 1
                    if line.strip().endswith("*/"):
                        start_note = False
                else:
                    if line.strip().startswith("/*"):
                        start_note = True
                        note_line += 1

                    if line.strip().endswith("*/"):
                        start_note = False

                    elif line.strip().startswith('//'):
                        note_line += 1
                    else:
                        continue

        print("c/c++, total_line: {}, blank_line: {}, note_line: {}".format(total_line, blank_line, note_line))
        return total_line - blank_line - note_line


class Java_Counter(Counter):
    def __init__(self):
        pass

    def count_line(self, file):

        total_line = 0
        blank_line = 0
        note_line = 0

        start_note = False

        with open(file, 'r') as f:
            for line in f:

                total_line += 1

                #blank lines
                if not line.split():
                    blank_line += 1
                    continue

                #noted lines:
                if start_note:
                    note_line += 1
                    if line.strip().endswith("*/"):
                        start_note = False
                else:
                    if line.strip().startswith("/*") or\
                    line.strip().startswith("/**"):
                        start_note = True
                        note_line += 1

                    if line.strip().endswith("*/"):
                        start_note = False

                    elif line.strip().startswith('//'):
                        note_line += 1
                    else:
                        continue

        print("java, total_line: {}, blank_line: {}, note_line: {}".format(total_line, blank_line, note_line))
        return total_line - blank_line - note_line

class Txt_Counter(Counter):
    def __init__(self):
        pass

    def count_line(self, file):

        total_line = 0
        blank_line = 0

        with open(file, 'r') as f:
            for line in f:

                total_line += 1

                #blank lines
                if not line.split():
                    blank_line += 1
                    continue
        print("plain text, total_line: {}, blank_line: {}".format(total_line, blank_line))
        return total_line - blank_line



if __name__ == '__main__':

    file = r'D:\My_Project\Code_Jam\2018_codejam\2018_codejam_auto-judge3.0\exe\error_Felix_py3_1.py'
    file = r'C:\Users\tarzonz\Desktop\1aa.py'

    file = r'D:\My_Project\Code_Jam\2018_codejam\2018_codejam_auto-judge3.0\exe\ShirleyZhao_win64_q1.cpp'

    my_counter = My_Counter()
    lines = my_counter.count_lines(file)

    print("file effective lines = {}".format(lines))
    print("Done.")
 