# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:54:47 2021

@author: iamsh
"""

class PostEval:
    
    def __init__(self, n):
        self.__n = n
        self.__l = [None]*n
        self.__top = -1
    
    def isEmpty(self):
        if self.__top == -1:
            return True
        return False
    
    def isFull(self):
        if self.__top == (self.__n)-1:
            return True
        return False
    
    def push(self, a):
        if self.isFull():
            return False
        else:
            self.__top += 1
            self.__l[self.__top] = a
    
    def pop(self):
        if self.isEmpty():
            return False
        else:
            p = self.__l[self.__top]
            self.__l[self.__top] = None
            self.__top -= 1
            return p
        
    def isOperand(self, ch):
        return (ch.isalpha() or ch.isnumeric())
    
    def isOperator(self, ch):
        op = ['+', '-', '*', '/', '^']
        return (ch in op)
    
    
    def evaluate(self, post):
        
        for x in post:
            if self.isOperand(x):
                self.push(int(x))
            
            elif self.isOperator(x):    
                b = self.pop()
                a = self.pop()
                if x == '+':
                    self.push(a+b)
                elif x == '-':
                    self.push(a-b)
                elif x == '*':
                    self.push(a*b)
                elif x == '/':
                    self.push(a//b)
                elif x == '^':
                    self.push(a**b)
            
        return self.pop()
    
inp = input("Enter postfix expression: ")
post = inp.split()
st = PostEval(len(post))
print("Postfix evaluation:", st.evaluate(post))