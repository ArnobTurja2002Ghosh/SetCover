from sys import argv
from read import ISET
from SETTREE import SETTree
def two_arguments():
    print("python", argv[0], argv[1])

    b1 = ISET(argv[1])
    a = SETTree()
    b = b1.subset_list()
    j=0
    for i in b:
        j+=1
        a.insert_set(j, i)
    print("Input description:")
    b1.input_description()
    if(a.optimal1(a.search_sets2(a.search_set2(b1.universe(), a._root))) != "No optimal solution"):
        print("Optimal value =", len(a.optimal1(a.search_sets2(a.search_set2(b1.universe(), a._root)))[0]))
        #print(a.optimal1(a.search_sets2(a.search_set2(b1.universe(), a._root))))
        for i in range(0, len(a.optimal1(a.search_sets2(a.search_set2(b1.universe(), a._root))))):
            print(i+1,"\t >>", a.optimal1(a.search_sets2(a.search_set2(b1.universe(), a._root)))[i])
        print(len(a.optimal1(a.search_sets2(a.search_set2(b1.universe(), a._root)))), "optimal solution(s)")
    elif(a.optimal1(a.search_sets2(a.search_set2(b1.universe(), a._root))) == "No optimal solution"):
        print(">> No solutions")
def one_argument():
    print("python", argv[0])
    print("format: system <set-file>")
    print("For more information, please read README.txt")
def main():
    if(len(argv) != 2):
        one_argument()
    elif(len(argv) == 2):
        two_arguments()
main()