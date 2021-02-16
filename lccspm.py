"""
Lccspm

Created on Thu Oct  8 19:16:41 2020

@author: ADEYEMO, Victor Elijah.
"""

import csv
import pandas as pd



class Mining:
    def __init__(self, name):
        self.name = name
        self.data = None
        self.sequenceDB = None
    
    def load_data(self, path = ''):
        
        self.data = pd.read_csv(path, encoding = "ISO-8859-1")
        self.sequenceDB= self.data.iloc[0:,1].tolist()
        self.sdblength = len(self.sequenceDB)
        
        self.maxlength = 0
        for sequence in self.sequenceDB:
            self._maxl = len(sequence)
            if self._maxl > self.maxlength:
                self.maxlength = self._maxl
        
        

    def get_maxLength(self):
        return self.maxlength
    
    def get_SDB(self):
        return self.sequenceDB
    
    def get_SDBlength(self):
        #self.sdblength = len(self.sequenceDB)
        return self.sdblength
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_length(self):
        return self.length
    
    def set_length(self, length):
        self.length = length

    def uniqueItems(self):
        
        self.GeneratedCandidates = {}
        
        for i in range(self.sdblength):
            start = 0
            end = 1
                
            while(end <= len(self.sequenceDB[i])):
                self.GeneratedCandidates.update({self.sequenceDB[i][start:end]:None})
                start+=1
                end+=1
        
        return list(self.GeneratedCandidates.keys())
    
    def mine(self):
        
        self.GeneratedCandidates = {}
        
        for x in range(self.length):
            for i in range(self.sdblength-1):
                start = 0
                end = x+1
                
                while(end <= len(self.sequenceDB[i])):
                    self.GeneratedCandidates.update({self.sequenceDB[i][start:end]:None})
                    start+=1
                    end+=1
        return self.GeneratedCandidates
    
        
    def setl_mine(self, length):
        self.length = length
        
        if self.length == self.maxlength:
            self.length = self.length -2
        
        self.GeneratedCandidates = []
        
        for x in range(self.length):
            for i in range(self.sdblength-1):
                start = 0
                end = x+1
                
                while(end <= len(self.sequenceDB[i])):
                    self.GeneratedCandidates.append(self.sequenceDB[i][start:end])
                    start+=1
                    end+=1
        return self.GeneratedCandidates



class Pruning:
    def __init__(self, name, object):
        self.name = name
        self.sequenceDB = object.sequenceDB
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def setsupportpruning(self, mined, support):
        self.mined = mined
        self.support = support

        self.SupportList = {}
        
        for sub in self.mined:
            score = len([i for i in self.sequenceDB if sub in i])
            if score >= self.support:
                self.SupportList.update({sub:score})
        
        return self.SupportList
    
    def prune(self, mined):
        self.mined = mined
        
        self.SupportList = {}

        for sub in self.mined.keys():
            score = len([i for i in self.sequenceDB if sub in i])
            if score >= self.support:
                self.SupportList.update({sub:score})

        return self.SupportList
    
    def get_support(self):
        return self.support
    
    def set_support(self, support):
        self.support = support




class Closed:
    def __init__(self, name):
        self.name = name
    
    def closed(self, pruned):
        self.pruned = pruned
        
        self.nonclosed = set()
        
        for subsequence, support in self.pruned.items():
            for width in range(1, len(subsequence)):
                for begin in range(len(subsequence) + 1 - width):
                    _subsequence = subsequence[begin:begin + width]
                    non = (_subsequence, support)
                    self.nonclosed.add(non)
        
        self.closedcontiguous = dict(self.pruned.items() - self.nonclosed)
        return self.closedcontiguous, self.nonclosed
    
    def csv(self, file, filename):
        self.filename = filename
        self.file = file
        
        self.Dfile = pd.DataFrame(list(self.file.items()), columns = ['Subsequences','Support'])
        self.Dfile = self.Dfile.sort_values('Support', ascending=False)
        self.Dfile.to_csv(filename, index=False)





