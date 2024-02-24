# recitation-04

from collections import defaultdict


#### PART ONE ###

def run_map_reduce(map_f, reduce_f, docs):
    # done. do not change me.
    """    
    The main map reduce logic.
    
    Params:
      map_f......the mapping function
      reduce_f...the reduce function
      docs.......list of input records
    """
    # 1. call map_f on each element of docs and flatten the results
    # e.g., [('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1), ('sam', 1), ('is', 1), ('ham', 1)]
    pairs = flatten(list(map(map_f, docs)))
    # 2. group all pairs by their key
    # e.g., [('am', [1, 1]), ('ham', [1]), ('i', [1, 1]), ('is', [1]), ('sam', [1, 1])]
    groups = collect(pairs)
    # 3. reduce each group to the final answer
    # e.g., [('am', 2), ('ham', 1), ('i', 2), ('is', 1), ('sam', 2)]
    return [reduce_f(g) for g in groups]

def word_count_map(doc):
  return [(word, 1) for word in doc.split()]
    
    


def word_count_reduce(group):
  token, counts = group
  return (token, sum(counts))
    
    


def iterate(f, x, a):
    # done. do not change me.
    """
    Params:
      f.....function to apply
      x.....return when a is empty
      a.....input sequence
    """
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])
    
def flatten(sequences):
    # done. do not change me.
    return iterate(plus, [], sequences)

def collect(pairs):
    """
    # done. do not change me.
    Implements the collect function (see text Vol II Ch2)
    E.g.:
    >>> collect([('i', 1), ('am', 1), ('sam', 1), ('i', 1)])
    [('am', [1]), ('i', [1, 1]), ('sam', [1])]    
    """
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())


def plus(x, y):
    # done. do not change me.
    return x + y

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        return f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
    
    
    
    
### PART TWO ###

def sentiment_map(doc, pos_terms=set(['good', 'great', 'awesome', 'sockdolager']), neg_terms=set(['bad', 'terrible', 'waste', 'carbuncle', 'corrupted'])):
  tokens = doc.split()
  return [('positive', 1) if token in pos_terms else ('negative', 1) for    token in tokens if token in pos_terms or token in neg_terms]

