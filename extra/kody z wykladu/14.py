from BST_and_RB_tree import *

#drzewo BST z operacjami oraz
#drzewo czerwono-czarne //p. s. no tego to akurat nie ma
#implementacja w zaimportowanym pliku
#--------------------------------------------#
#przykładowe hashowania
def hash_function1(data,size): #uniwersalne
    pass

#rozwiązywanie konfliktów w hashowaniu
#v1 - metoda listowa


#v2 - adresowanie otwarte


#testy
root=BSTNode(12)
insert(root,14); insert(root,6); insert(root,18)
insert(root,8); insert(root,6); insert(root,13)
insert(root,14); insert(root,4); insert(root,18)
print(min_n(root).key)
print(max_n(root).key)
insert(root,3); insert(root,5); insert(root,7)
insert(root,10); insert(root,12.5); insert(root,13.5)
insert(root,16); insert(root,19)
print(succ(search(root,10)).key)
print(succ(search(root,6)).key)
print(pred(search(root,16)).key)
print(pred(search(root,12.5)).key)
remove(root,4)
n=search(root,5)
print(n.left.key,n.right,n.parent.key)
