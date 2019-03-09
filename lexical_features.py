def get_punctuation_count(review):
    text = review['review']
    punctuation = {'!': 0, '?': 0, '"': 0, "'": 0}
    count = 0
    for l in text:
        if l in punctuation.keys():
            count += 1
            punctuation[l] += 1
    if count is not 0:
        for i in punctuation:
            punctuation[i] /= count
    return list(punctuation.values())


def get_punctuation_count_vector(reviews):
    counts = []
    for review in reviews:
        counts.append(get_punctuation_count(review))
    return counts
