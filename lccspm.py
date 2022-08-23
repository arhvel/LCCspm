"""
Lccspm

"""
Created on Mon Aug 22 13:23:14 2022

@author: adeyem01
"""

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
        
        self.sdbmaxlength = 0
        for sequence in self.sequenceDB:
            self._maxl = len(sequence)
            if self._maxl > self.sdbmaxlength:
                self.sdbmaxlength = self._maxl
        
        self.summation = 0
        for sequence in self.sequenceDB:
            self.length = len(sequence)
            self.summation+=self.length    
            
        self.sdbavglength = round(self.summation/self.sdblength)
            
    def get_SDBAvglength(self):
        return self.sdbavglength

    def get_SDBLength(self):
        return self.summation
        
    def get_SDBmaxLength(self):
        return self.sdbmaxlength
    
    def get_SDB(self):
        return self.sequenceDB
    
    def get_SDBsize(self):
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
     
        
    def setl_mine(self, length, rel_support):
        self.length = length
        self.Rel_support = rel_support
        
        self.Abs_score = round(((self.Rel_support/100)* self.sdblength))
        #self.lastSeq = round((self.sdblength - self.Abs_score) + 1)
        
        #self.SDB = self.sequenceDB[:self.lastSeq]
        #self.SDBlen = len(self.SDB)
                
        if self.length == self.sdbmaxlength:
            self.length = self.length -2
        
        self.GeneratedCandidates = {}
        
        for x in range(self.length):
            for i in range(self.Abs_score):
                start = 0
                end = x+1
                
                while(end <= len(self.sequenceDB[i])):
                    self.GeneratedCandidates.update({self.sequenceDB[i][start:end]:None})
                    start+=1
                    end+=1
        return self.GeneratedCandidates

    def size(self, file):
        self.siz = len(file)
        
        return self.siz
    
    def avglength(self, file):
        
        self.siz = len(file)
        
        if(self.siz == 0):
            self.average = self.siz
        
        else:
            self.summedlength = 0
            for sequence in file.keys():
                self.length = len(sequence)
                self.summedlength+=self.length
            
            self.average = round(self.summedlength/self.siz)
        
        return self.average
    
    def totallength(self, file):
        self.data = file
        self.summedlength = 0
        for sequence in self.data:
            self.length = len(sequence)
            self.summedlength+=self.length  
        
        return self.summedlength

    def maxlength(self, file):
        self.data = file.keys()
        self.maxleng = 0
        for sequence in self.data:
            self._fmaxl = len(sequence)
            if self._fmaxl > self.maxleng:
                self.maxleng = self._fmaxl
        
        return self.maxleng


class Pruning:
    def __init__(self, name, object):
        self.name = name
        self.sequenceDB = object.sequenceDB
        self.sdblength = object.sdblength
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def setsupportpruning(self, mined, rel_support):
        self.mined = mined
        self.Rel_support = rel_support

        self.SupportList = {}
        self.Abs_score = ((self.Rel_support/100)* self.sdblength)
        
        for sub in self.mined.keys():
            
            self.score = len([i for i in self.sequenceDB if sub in i])
            
            if self.score >= self.Abs_score:
                self.SupportList.update({sub:self.score})
        
        return self.SupportList

    
    #def prune(self, mined):
        #self.mined = mined
        
        #self.SupportList = {}

        #for sub in self.mined.keys():
            #score = len([i for i in self.sequenceDB if sub in i])
            #if score >= self.support:
                #self.SupportList.update({sub:score})

        #return self.SupportList
    
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
        
        closedcontiguous = dict(self.pruned.items() - self.nonclosed)
        return closedcontiguous
    
    def csv(self, file, filename):
        self.filename = filename
        self.file = file
        
        self.Dfile = pd.DataFrame(list(self.file.items()), columns = ['Subsequences','Support'])
        self.Dfile = self.Dfile.sort_values('Support', ascending=False)
        self.Dfile.to_csv(filename, index=False)
