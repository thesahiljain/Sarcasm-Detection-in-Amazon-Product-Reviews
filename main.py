import dataset
import sentiment_features
import lexical_features
import pos_features
import classification


def flatten(matrix):
    return list(map(list, zip(*matrix)))

# Loading dataset
sarc_train, sarc_test, reg_train, reg_test = dataset.load_dataset()

# Sentiment features
print('Preparing sentiment score vectors')
sarc_train_sent = sentiment_features.get_sentiment_score_list(sarc_train)
sarc_test_sent = sentiment_features.get_sentiment_score_list(sarc_test)
reg_train_sent = sentiment_features.get_sentiment_score_list(reg_train)
reg_test_sent = sentiment_features.get_sentiment_score_list(reg_test)

print('Preparing Rating contrast vectors')
sarc_train_rating, _ = sentiment_features.get_rating_contrast(sarc_train, sarc_train_sent)
sarc_test_rating, _ = sentiment_features.get_rating_contrast(sarc_test, sarc_test_sent)
reg_train_rating, _ = sentiment_features.get_rating_contrast(reg_train, reg_train_sent)
reg_test_rating, _ = sentiment_features.get_rating_contrast(reg_test, reg_test_sent)

print('Sentiment features added\n')

# Lexical features
print('Preparing punctuation count feature')
sarc_train_punctuations = flatten(lexical_features.get_punctuation_count_vector(sarc_train))
sarc_test_punctuations = flatten(lexical_features.get_punctuation_count_vector(sarc_test))
reg_train_punctuations = flatten(lexical_features.get_punctuation_count_vector(reg_train))
reg_test_punctuations = flatten(lexical_features.get_punctuation_count_vector(reg_test))

print('Lexical features added\n')

# POS features
print('Preparing pos tag ratio vectors')
sarc_train_pos_ratios = flatten(pos_features.get_tag_ratio_vector(sarc_train))
sarc_test_pos_ratios = flatten(pos_features.get_tag_ratio_vector(sarc_test))
reg_train_pos_ratios = flatten(pos_features.get_tag_ratio_vector(reg_train))
reg_test_pos_ratios = flatten(pos_features.get_tag_ratio_vector(reg_test))

print('Parts of speech features added')

# Classification
print()
print('Preparing feature vectors of individual dataset')
sarc_train_features = classification.get_feature_vector([sarc_train_sent, sarc_train_rating]
                                                        +sarc_train_punctuations+sarc_train_pos_ratios)
sarc_test_features = classification.get_feature_vector([sarc_test_sent, sarc_test_rating]
                                                       +sarc_test_punctuations+sarc_test_pos_ratios)
reg_train_features = classification.get_feature_vector([reg_train_sent, reg_train_rating]
                                                       +reg_train_punctuations+reg_train_pos_ratios)
reg_test_features = classification.get_feature_vector([reg_test_sent, reg_test_rating]
                                                      +reg_test_punctuations+reg_test_pos_ratios)

print('Training and testing classifier')
classifier = classification.get_classifier(sarc_train_features, reg_train_features)
classification.test_classifier(classifier, sarc_test_features, reg_test_features)
# End of code
print('The end!')

review = {'rating': 1.0, 'review': 'I recently purchased this speaker and I want to tell you that it is totally worth the 1000 bucks!!! The voice is so clear and lound that I can hear voices even from other galaxies!'}