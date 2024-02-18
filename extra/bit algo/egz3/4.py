from zad4testy import runtests

def balance( T ):
    set_weight(T)
    min_diff=[float('inf')]
    min_id=[-1]
    find_best(T,min_diff,min_id,T.subtree_weight)
    return min_id[0]

def set_weight(T):
    for i in range(len(T.edges)):
        T.subtree_weight+=T.weights[i]
        T.subtree_weight+=set_weight(T.edges[i])
    return T.subtree_weight

def find_best(T,min_diff,min_id,total):
    for i in range(len(T.edges)):
        curr_diff=abs((total-T.weights[i]-T.edges[i].subtree_weight)-(T.edges[i].subtree_weight))
        if curr_diff<min_diff[0]:
            min_diff[0]=curr_diff
            min_id[0]=T.ids[i]
        find_best(T.edges[i],min_diff,min_id,total)

#testy
runtests( balance )
