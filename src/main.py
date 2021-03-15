from importlib import import_module
import glob
import re
import json
import pathlib
import os

from solutions.leetcode import ListNode, TreeNode

class Metadata:
    def __init__(self, metaFile, testcaseFile, outputFile):
        super().__init__()
        self.outputFile = outputFile
        self.metaFile = metaFile
        self.metadata = json.load(open(metaFile))
        testcase = json.load(open(testcaseFile))
        for id in testcase:
            if id in self.metadata:
                self.metadata[id]['exampleTestcases'] += '\n' + testcase[id]['exampleTestcases']

    
    def getExampleTestcases(self, problemId: str):
        testcases = self.metadata[problemId]['exampleTestcases']
        params = []
        paramTypes = [param['type'] for param in self.metadata[problemId]['params']]
        for i, paramString in enumerate(testcases.split('\n')):
            if i % len(paramTypes) == 0: params.append([])
            paramType = paramTypes[i % len(paramTypes)]
            params[-1].append(self.__parse(paramType, paramString))
        return params
    
    def setExampleResult(self, problemId: str, result):
        resultType = self.metadata[problemId]['return']['type']
        self.metadata[problemId]['exampleResult'] = '\n'.join([self.__stringify(resultType, r) for r in result])

    def execute(self, problemId: str, klass):
        params = self.getExampleTestcases(problemId)
        results = []
        solution = klass()
        funcNames = [k for k in dir(solution) if not k.startswith('_')]
        if len(funcNames) > 1 or len(funcNames) == 0:
            return # throw error
        for param in params:
            ret = getattr(solution, funcNames[0])(*param)
            returnType = self.metadata[problemId]['return']['type']
            if 'output' in self.metadata[problemId]: # 这种题目是直接修改入参作为题目输出的
                outputMeta = self.metadata[problemId]['output']
                outputSize = None
                if 'size' in outputMeta:
                    if outputMeta['size'] == 'ret': outputSize = ret
                    else: raise Exception('不支持')
                paramIndex = outputMeta['paramindex']
                outputType = self.metadata[problemId]['params'][paramIndex]['type']
                if outputSize:
                    outputStr = self.__stringify(outputType, param[paramIndex][:outputSize])
                else:
                    outputStr = self.__stringify(outputType, param[paramIndex])
            else:
                outputStr = self.__stringify(returnType, ret)
            results.append(outputStr)
        self.metadata[problemId]['exampleResult'] = '\n'.join(results)
    
    def save(self):
        json.dump(self.metadata, open(self.outputFile, 'w'), indent=2)

    def __parse(self, type: str, s: str):
        if type == 'integer':
            return int(s)
        elif type == 'integer[]':
            if s == '[]': return []
            return [int(e) for e in s[1:-1].split(',')]
        elif type == 'string':
            return s[1:-1]
        elif type == 'string[]':
            return [e[1:-1] for e in s[1:-1].split(',')]
        elif type == 'boolean':
            return s == 'true'
        elif re.match(r'list<(.+)>', type):
            innerType = re.match(r'list<(.+)>', type)[1]
            return [self.__parse(innerType, e) for e in s[1:-1].split(',')]
        elif type == 'ListNode':
            if s == '[]': return None
            p = dummy = ListNode()
            for v in s[1:-1].split(','):
                p.next = ListNode(int(v))
                p = p.next
            return dummy.next
        elif type == 'TreeNode':
            if s == '[]': return None
            nodes = [TreeNode(int(e)) if e != 'null' else None for e in s[1:-1].split(',')]
            root = nodes[0]
            queue = [root]
            idx = 1
            while queue:
                node = queue.pop(0)
                if idx < len(nodes):
                    node.left = nodes[idx]
                    idx += 1
                if idx < len(nodes):
                    node.right = nodes[idx]
                    idx += 1
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            return root
        raise Exception(type + "不支持")

    def __stringify(self, type: str, v):
        if type == 'integer':
            return str(v)
        elif type == 'integer[]':
            return '[' + ','.join([str(e) for e in v]) + ']'
        elif type == 'string':
            return '"' + v + '"'
        elif type == 'string[]':
            return '[' + ['"' + e + '"' for e in v].join(',') + ']'
        elif type == 'boolean':
            return 'true' if v else 'false'
        elif re.match(r'list<(.+)>', type):
            innerType = re.match(r'list<(.+)>', type)[1]
            return '[' + ','.join([self.__stringify(innerType, e) for e in v]) + ']'
        elif type == 'ListNode':
            res = []
            p = v
            while p:
                res.append(str(p.val))
                p = p.next
            return '[' + ','.join(res) + ']'
        elif type == 'TreeNode':
            res = []
            queue = []
            notNoneCnt = 0
            if v:
                queue.append(v)
                notNoneCnt = 1
            while notNoneCnt:
                node = queue.pop(0)
                if node:
                    notNoneCnt -= 1
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    if node.left: notNoneCnt += 1
                    if node.right: notNoneCnt += 1
                else:
                    res.append(None)
            return '[' + ','.join(['null' if e is None else str(e) for e in res]) + ']'
        raise Exception(type + "不支持")

if __name__ == '__main__':
    pathOfCurrentFile = pathlib.Path(__file__).parent.absolute()
    metadata = Metadata(os.path.join(pathOfCurrentFile, './metadata.json'), os.path.join(pathOfCurrentFile, './testcases.json'), os.path.join(pathOfCurrentFile, '../dist/data.json'))

    filenames = glob.glob(os.path.join(pathOfCurrentFile, 'solutions/q*.py'))
    for filename in filenames:
        problemId = re.search(r'q(\d+).py', filename)[1]
        moduleName = 'solutions.q' + problemId
        print(problemId + '...')
        Solution = import_module(moduleName).Solution
        metadata.execute(problemId, Solution)
        print(problemId + '###')
        metadata.save()
