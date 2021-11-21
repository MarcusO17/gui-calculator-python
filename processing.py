from enum import Enum, auto
from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
sHand = logging.StreamHandler()
sHand.setLevel(logging.DEBUG)
logger.addHandler(sHand)

class Operators(Enum):
    """Types of operators"""

    ADD = auto()
    MINUS = auto()
    MUL = auto()
    DIVIDE = auto()

#Performs addition on the inputs
def add(a: float,b: float) -> float:
    return a + b

#Subtracts the inputs
def subtract(a: float,b: float) -> float:
    return b - a

#Multiplies the inputs
def multiply(a: float,b: float) -> float: 
    return a * b

#Divides the inputs
def divide(a: float,b: float) -> float: 
    return b / a

#Resolves a postfix expression into the answer
def expResolver(exp: List[str]) -> float:
    operation = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    stack = []
    operator = ('+','-','*','/')
    for token in exp:
        if token.isnumeric():
            stack.append(float(token))
            logger.debug(stack)
        elif token in operator:
            logger.debug(token)
            stack.append(operation[token](stack.pop(),stack.pop()))
            logger.debug(stack)
    return stack.pop()

def precedence(op: str) -> int:
    if op == '-':
        return 1
    elif op == '+':
        return 1
    elif op == '*':
        return 2
    elif op == '/':
        return 2
    elif op == '(':
        return 3
    elif op == ')':
        return 3

#Used to convert the expression into postfix notation
def expConverter(exp: str) -> List[str]:
    addOp = ('+','-')
    mulOp = ('*','/')
    brackets = ('(',')')
    tokens = tokenise(exp)
    logger.debug(tokens)
    outStack = []
    opStack = []
    for token in tokens:
        logger.debug(f'opStack {opStack}')
        logger.debug(f'token {token}')
        logger.debug(f'outStack {outStack}\n')
        if token.isnumeric():
            outStack.append(token)
            continue
        if token in brackets:
            if token == '(':
                opStack.append(token)
                continue
            #right bracket encountered
            else:
                top = opStack[len(opStack)-1]
                while not top == '(':
                    outStack.append(opStack.pop())
                    if opStack:
                        top = opStack[len(opStack)-1]
                    else:
                        break
                opStack.pop()
                continue
        if token in addOp or token in mulOp:
            #logger.debug(opStack)
            if not opStack:
                opStack.append(token)
                continue
            top = opStack[len(opStack)-1]
            #token has higher precedence than top
            #logger.debug(f'top of opStack {top}')
            if precedence(top) >= precedence(token) and not top == '(':
                while precedence(top) >= precedence(token):
                    outStack.append(opStack.pop())
                    if opStack:
                        if opStack[len(opStack)-1] == '(':
                            break
                        else:
                            top = opStack[len(opStack)-1]
                    else:
                        break
                opStack.append(token)
                continue
            #token has lower or same precedence as top
            else:
                opStack.append(token)
                continue
    while opStack:
        if opStack[len(opStack)-1] == '(':
            opStack.pop()
        else:
            outStack.append(opStack.pop())
    return outStack

#Takes an expression and tokenizes it
def tokenise(expr: str) -> List[str]:
    operator = ('+','-','*','/','(',')')
    output = []
    temp = ''
    exp = conversion(expr)
    for char in exp:
        if char.isnumeric():
            temp += char
            continue
        elif char in operator:
            if not temp:
                output.append(char)
            else:
                output.append(temp)
                temp = ''
                output.append(char)
    if temp:
        output.append(temp)
    return output

def conversion(expr:str) -> str:
    output = expr.replace('×','*')
    output = output.replace('x','*')
    output = output.replace('÷','/')
    return output

def compute(expr:str) -> float:
    return expResolver(expConverter(expr))

if __name__ == '__main__':
    #logger.debug(precedence('*'))
    logger.debug(compute('(444×4+4/16)*234+1'))