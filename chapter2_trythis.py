import spacy
from spacy.symbols import ORTH, LEMMA
nlp = spacy.load('en_core_web_sm')
nlp.get_pipe("attribute_ruler").add([[{"TEXT": "Frisco"}]], {"LEMMA": "San Francisco"})
doc = nlp(u'I have flown to LA. Now I am flying to Frisco.')
for sent in doc.sents:
    print([w.lemma_ for w in sent if (w.dep_ == 'ROOT' and w.tag_ == 'VBG') or (w.dep_ == 'pobj' and w.tag_ == 'NNP')])
