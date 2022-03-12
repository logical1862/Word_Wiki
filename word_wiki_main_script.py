##Word wiki (search word, give list of closest words to search, 1st auto selected to show 
# *worddata: 1. definition 2. synonym 3. antonym 
# *wikidata: preview and link to wikipedia entry [if one exists tied to searcg, or list])


from cgitb import html
import wikipedia
import word_wiki_classes


input_string = 'banana'

search_instance = word_wiki_classes.word_data

search_instance.input_string = input_string

word_definition = search_instance.definition(search_instance)
word_synonym = search_instance.synonym(search_instance)
word_antonym = search_instance.antonym(search_instance)





input1 = wikipedia.search(input_string, results = 1, suggestion = True)
input2 = input1[0:1]



wiki_inst = word_wiki_classes.wiki_data()
wiki_inst.get_wiki_data(input_string=input2)

excerpt_limit = wiki_inst.wiki_excerpt[:300]

wiki_link = wiki_inst.wiki_URL
    
