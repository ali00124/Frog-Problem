# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

        if parent:
            self.parent.children.append(self)


def print_tree(current_node, childattr='children', nameattr='name', indent='', last='updown'):

    if hasattr(current_node, nameattr):
        name = lambda node: getattr(node, nameattr)
    else:
        name = lambda node: str(node)

    children = lambda node: getattr(node, childattr)
    nb_children = lambda node: sum(nb_children(child) for child in children(node)) + 1
    size_branch = {child: nb_children(child) for child in children(current_node)}

    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(children(current_node), key=lambda node: nb_children(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())

    """ Printing of "up" branch. """
    for child in up:
        next_last = 'up' if up.index(child) is 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', ' ' * len(name(current_node)))
        print_tree(child, childattr, nameattr, next_indent, next_last)

    """ Printing of current node. """
    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up: end_shape = '┤'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, name(current_node), end_shape))

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', ' ' * len(name(current_node)))
        print_tree(child, childattr, nameattr, next_indent, next_last)

"""
Created on Thu Feb 15 22:14:31 2018
@author: ali
"""

"""Get list of next possible states"""
def getNext(root):
    root = __builtins__.list(root)
    next = []
    index = root.index('0')
    tmp = root[:]
    try:
        if (tmp[index+1] == '2'):
            tmp[index] = '2'
            tmp[index+1] = '0'
            str = ''.join(tmp)
            next.append(str)
    except:
        None
    try:
        tmp = root[:]
        if (tmp[index+2] == '2'):
            tmp[index] = '2'
            tmp[index+2] = '0'
            str = ''.join(tmp)
            next.append(str)
    except:
        None
    try:
        tmp = root[:]
        if (index-1 >= 0 and tmp[index-1] == '1'):
            tmp[index] = '1'
            tmp[index-1] = '0'
            str = ''.join(tmp)
            next.append(str)
    except:
        None
    try:
        tmp = root[:]
        if (index-2 >= 0 and tmp[index-2] == '1'):
            tmp[index] = '1'
            tmp[index-2] = '0'
            str = ''.join(tmp)
            next.append(str)
    except:
        None
    return next

s = [1, 1, 1, 0, 2, 2, 2]


def validsteps(totalsteps):
    steps = []
    for index, frog in enumerate(totalsteps):
        j = 0
        m = index
        if (frog == 1):
            j = index + 2
            m = m + 1
        elif (frog == 2):
            j = index - 2
            m = m - 1
        else:
            j = 0

        if (frog == 0):
            continue
        if (not ((j < 0) or (j >= len(totalsteps)))):
            if (totalsteps[j] == 0):
                t = list(totalsteps)
                t[index] = 0
                t[j] = frog
                steps.append(t)
        if (not ((m < 0) or (m >= len(totalsteps)))):
            if (totalsteps[m] == 0):
                t = list(totalsteps)
                t[index] = 0
                t[m] = frog
                steps.append(t)
    return steps


def solAll(current, target):
    next = []
    k = -1
    a2 = 0
    for a in current:
        k = k + 1
        n = validsteps(a[-1])
        # print("\t")
        if (a2 != len(a) - 1):
            print("\n------------ depth " + str(len(a) - 1) + "------------------")
            a2 = len(a) - 1
        print("\n" + str(a[len(a) - 1]) + " at depth: " + str(len(a) - 1) + " node: " + str(
            k) + "\nhas the following valid steps:")
        print(n)
        for q in n:
            # print(" jhh   ")
            t = list(a)
            t.append(q)
            if (q == target):
                print("sdsd")
                return t
            next.append(t)

    return next


def win(start):
    # print(start)
    temp = [[start]]
    # print (temp)
    # print("her")
    # print(temp)
    end = list(start)
    end.reverse()
    # print(end)
    # print("uuu")
    while (temp[-1] != end):
        # print(temp[-1])
        # print("uuu77")
        temp = solAll(temp, end)
        # print(temp)
        # print("\n-----------------------------------------------------")
    return temp


print(win(s))

"""Main"""    

root = Node("1110222")
stack = ['1110222']
stackNodes = [root]
while len(stack)!=0:
    node = stack.pop()
    prevNode = stackNodes.pop()
    tmp = getNext(node)
    stack = stack + tmp
    for nodes in tmp:
        stackNodes.append(Node(nodes,prevNode))

print_tree(root)