import logging
from transformers import AutoTokenizer, AutoModelForTokenClassification

from transformers import pipeline
from time import time


def call_logger(f):
    def log_write(*args):
        start = time()
        result = f()
        logging.debug(
            f"{__name__}.fn: {f.__name__}({args}). [{(time()-start)*1000:.2f}ms]"
        )
        return result

    return log_write


@call_logger
def find_named_entities():
    logging.debug("ner called")
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    example = "My name is Wolfgang and I live in Berlin"
    ner_results = nlp(example)
    print(ner_results)
