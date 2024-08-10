# Cahuilla Morphological Parser

This parser takes in a deverbal noun and returns the definition along with its morphological information. Deverbal nouns are typically comprised of a root verb and a suffix that transform the verb into this new noun meaning. This parser will return the root verb, its gloss, and the transitivity of that verb along with the nominalizer suffix, its gloss, and the class 1 relationship of that suffix. For example, for the word ***kʷáʔisniʔil̃***:

```json
[
    {
        "definition": the writing,
        "root": kʷáʔisni,
        "root_gloss": to write,
        "transitivity": transitive,
        "nominalizer": ʔil̃,
        "nominalizer_gloss": NMLZ.ABST,
        "class1relationship": verbal abstract noun
    }
]
```
The API can be called directly using a POST request. The endpoint is ```http://localhost:5000/parse```. The POST request must contain a JSON body with the "word" key that you want to parse. For example:

```json
{"word":"kʷáʔisniʔil̃"}
```


To access this parser, follow the steps below:

### 1. Clone repository
Once cloned, navigate to Cahuilla-Morphological-Parser directory in your terminal.

### 2. Install dependencies
Run the following in the command line:
```pip install --upgrade pip```
```pip install -r requirements.txt```

### 3. Run application
To run the application, run the following line in your terminal: ```python3 -m web.app```

### 4. Send curl request
Once the application is up and running, in a new terminal run this curl command:
```curl -X POST http://localhost:5000/parse -H "Content-Type: application/json" -d '{"word": "kʷáʔisniʔil̃"}'```

The response will give you a json of the morphological components, as seen above:
{"definition": "the writing", "root": "kʷáʔisni", "root_gloss": "to write", "transitivity": "TRANSITIVE", "nominalizer": "ʔil̃", "nominalizer_gloss": "NMLZ.ABST", "class1relationship": "VERBAL_ABSTRACT_NOUN"}