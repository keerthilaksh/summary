import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    
    
    word_freq = {}
    for word in doc:
        if word.text.lower() not in punctuation and word.text.lower() not in stopwords:
            if word.text not in word_freq:
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    
    
    max_freq = max(word_freq.values())
    for word in word_freq:
        word_freq[word] = word_freq[word] / max_freq
    
    
    sent_tokens = list(doc.sents)
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq:
                if sent not in sent_scores:
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
    

    from heapq import nlargest
    select_len = int(len(sent_tokens) * 0.4)
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    final_summary = ' '.join([word.text for word in summary])
    
    original_length = len(rawdocs.split(' '))
    summary_length = len(final_summary.split(' '))

    return summary, original_length, summary_length


