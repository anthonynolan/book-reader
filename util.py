import logging
from transformers import AutoTokenizer, AutoModelForTokenClassification

from transformers import pipeline


def call_logger(f):
    def log_write(*args):
        print(f"{f.__name__} was called with {args}")
        return f()

    return log_write


def find_named_entities():
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    example = "My name is Wolfgang and I live in Berlin"
    ner_results = nlp(example)
    print(ner_results)
