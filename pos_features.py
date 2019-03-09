from textblob import TextBlob


def get_tag_ratio(review):
    tags = TextBlob(review['review']).tags
    count = {'NN': 0, 'NNP': 0, 'NNS': 0, 'NNPS': 0, 'VB': 0, 'VBD': 0, 'VBG': 0, 'VBN': 0, 'VBP': 0, 'VBZ': 0,
             'JJ': 0, 'JJR': 0, 'JJS': 0, 'CC': 0, 'CD': 0, 'DT': 0, 'EX': 0, 'FW': 0, 'IN': 0,
             'LS': 0, 'MD': 0, 'PDT': 0, 'POS': 0, 'PRP': 0, 'PRP$': 0, 'RB': 0, 'RBR': 0, 'RBS': 0, 'RP': 0,
             'TO': 0, 'UH': 0, 'WDT': 0, 'WP': 0, 'WP$': 0, 'WRB': 0}
    for t in tags:
        tag = str(t[1])
        if tag in count.keys():
            count[tag] += 1
    size = len(tags)

    ratio = []
    for t in count.values():
        ratio.append(t/size)
    return ratio


def get_tag_ratio_2(review):
    noun_tags = ['NN', 'NNP', 'NNS', 'NNPS']
    verb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    adjective_tags = ['JJ', 'JJR', 'JJS']
    adverb_tags = ['RB', 'RBR', 'RBS', 'RP']
    ratios = [0.0, 0.0, 0.0]
    tags = TextBlob(review['review']).tags
    for t in tags:
        tag = str(t[1])
        if tag in verb_tags:
            ratios[0] += 1
        elif tag in adjective_tags:
            ratios[1] += 1
        elif tag in adverb_tags:
            ratios[2] += 1
    for i in range(3):
        ratios[i] /= len(tags)
    return ratios


def get_tag_ratio_vector(reviews):
    ratios = []
    for review in reviews:
        ratios.append(get_tag_ratio_2(review))
    return ratios
