
import os
from dotenv import load_dotenv
import basilica

load_dotenv()

BASILICA_API_KEY = os.getenv('BASILICA_API_KEY', default='OOPS')

with basilica.Connection(BASILICA_API_KEY) as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])

print(list(embeddings)) # [[0.8556405305862427, ...], ...]

# sentences = [
#     "This is a sentence!",
#     "This is a similar sentence!",
#     "I don't think this sentence is very similar at all..."
# ]

# with basilica.Connection(BASILICA_API_KEY) as c:
#     embeddings = list(c.embed_sentences(sentences))