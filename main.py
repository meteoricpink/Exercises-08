# Exercise 8

import spacy

def write_to_file(text, output_file_path):
    if os.path.exists(output_file_path):
        raise RuntimeError("Output file already exists!")

    with open(output_file_path, 'w') as file:
        file.write(text)


def count_stopwords(input_file_path):
    nlp = spacy.load("en_core_web_sm")
    stopwords = nlp.Defaults.stop_words

    with open(input_file_path, 'r') as file:
        text = file.read()

    doc = nlp(text)
    count = sum(1 for token in doc if token.text.lower() in stopwords)

    return count


def remove_stopwords(input_file_path, output_file_path):
    nlp = spacy.load("en_core_web_sm")
    stopwords = nlp.Defaults.stop_words

    with open(input_file_path, 'r') as input_file:
        text = input_file.read()

    doc = nlp(text)
    filtered_text = " ".join(token.text for token in doc if token.text.lower() not in stopwords)

    with open(output_file_path, 'w') as output_file:
        output_file.write(filtered_text)


def tokenize_text(input_file_path, output_file_path):
    nlp = spacy.load("en_core_web_sm")

    with open(input_file_path, 'r') as input_file:
        text = input_file.read()

    doc = nlp(text)

    with open(output_file_path, 'w') as output_file:
        for token in doc:
            output_file.write(f"{token.text}\t{token.lemma_}\t{token.pos_}\n")


def save_visualization(input_file_path, output_file_path):
    nlp = spacy.load("en_core_web_sm")

    with open(input_file_path, 'r') as input_file:
        text = input_file.read()

    doc = nlp(text)
    svg = displacy.render(doc, style="dep", jupyter=False)

    with open(output_file_path, 'w') as output_file:
        output_file.write(svg)