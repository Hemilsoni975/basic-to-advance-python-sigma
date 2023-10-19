# to use regular expression import 're'
import re

text = """Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph  
       is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and 
       coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of 
       sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not 
        determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly 
       journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences 
       that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what
       happens in the rest of the paragraph"""

pattern = re.compile(r'Length')
matches = pattern.finditer(text)
for match in matches:
    print(match)
    print(text[430:437])  # slicing

print("_______________METHODS OF META CHARACTER____________________")

# pattern = re.compile(r'.length')  # it represents any characrter
# pattern = re.compile(r'^Paragraph')  # starts with
# pattern = re.compile(r'aph$')  # ends with
# pattern = re.compile(r'ea*')  #zero or more occurance
# pattern = re.compile(r'.ea+') # one or more occurence
# pattern = re.compile(r'.er{1}')  # exactly specified  number of occurance
# pattern = re.compile(r'(er){1}') # capture and group
# pattern = re.compile(r'er{1} | t') # either or



matches = pattern.finditer(text)
for match in matches:
    print(match)

print("____________special sequences_________________")


text = """Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph  
       is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and 
       coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of 
       sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not 
        determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly 
       journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences 
       that support one main idea. In this handout 98765-43221, we will refer to this as the “controlling idea,” because it controls what
       happens in the rest of the paragraph"""

pattern = re.compile(r'Length')

# pattern = re.compile(r'\AParagraph')
# pattern = re.compile(r'\bParagraph')
# pattern = re.compile(r'rest\b')
# pattern = re.compile(r'\Baph')
# pattern = re.compile(r'rest\B')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\srest')
# pattern = re.compile(r'\Srest')
# pattern = re.compile(r'\wrest')
# pattern = re.compile(r'\Wrest')
# pattern = re.compile(r'\Zrest')
pattern = re.compile(r'\d{5}-\d{5}')




matches = pattern.finditer(text)
for match in matches:
    print(match)
