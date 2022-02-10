def locate_cards (cards,query):
    pass

#result = locate_cards(1,2)
#print(result)

test = {
'input': {  
    'cards': [13,11,10,7],
    'query': 7
},
'output':3
}
#print(test['input']['cards'])
print(locate_cards(test['input']['cards']) == test['output'])