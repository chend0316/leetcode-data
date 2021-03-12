from importlib import import_module
import glob
import re
import json
import pathlib
import os

class Metadata:
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.metadata = json.load(open(filename))
    
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
    
    def save(self):
        json.dump(self.metadata, open(self.filename, 'w'), indent=2)

    def __parse(self, type: str, s):
        if type == 'integer':
            return int(s)
        elif type == 'integer[]':
            if s == '[]': return []
            return [int(e) for e in s[1:-1].split(',')]
        elif type == 'string':
            return s[1:-1]
        elif re.match(r'list<(.+)>', type):
            innerType = re.match(r'list<(.+)>', type)[1]
            return [self.__parse(innerType, e) for e in s[1:-1].split(',')]

    def __stringify(self, type: str, v):
        if type == 'integer':
            return str(v)
        elif type == 'integer[]':
            return '[' + ','.join([str(e) for e in v]) + ']'
        elif type == 'string':
            return '"' + v + '"'
        elif re.match(r'list<(.+)>', type):
            innerType = re.match(r'list<(.+)>', type)[1]
            return '[' + ','.join([self.__stringify(innerType, e) for e in v]) + ']'


if __name__ == '__main__':
    pathOfCurrentFile = pathlib.Path(__file__).parent.absolute()
    metadata = Metadata(os.path.join(pathOfCurrentFile, '../dist/metadata.json'))

    def execute(klass, params):
        solution = klass()
        funcNames = [k for k in dir(solution) if not k.startswith('_')]
        if len(funcNames) > 1 or len(funcNames) == 0:
            return # throw error
        return getattr(solution, funcNames[0])(*params)

    filenames = glob.glob(os.path.join(pathOfCurrentFile, 'solutions/q*.py'))
    for filename in filenames:
        problemId = re.search(r'q(\d+).py', filename)[1]
        moduleName = 'solutions.q' + problemId
        print(problemId + '...')
        Solution = import_module(moduleName).Solution
        results = []
        for param in metadata.getExampleTestcases(problemId):
            res = execute(Solution, param)
            results.append(res)
            # print('input: ')
            # print(param)
            # print('output: ')
            # print(res)
        print(problemId + '###')
        metadata.setExampleResult(problemId, results)
        metadata.save()