from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

def get_feature_vector(features_list):
    feature_vector = list(map(list, zip(*features_list)))
    return feature_vector


def get_classifier(sarc_train, reg_train):
    clf = svm.SVC()

    X = sarc_train + reg_train
    Y = [1]*len(sarc_train) + [0]*len(reg_train)
    clf.fit(X, Y)
    return clf


def test_classifier(clf, sarc_test, reg_test):
    sarc_count = sum(clf.predict(sarc_test))
    reg_count = sum(clf.predict(reg_test))
    reg_count = len(reg_test)-reg_count

    sarc_count = float(sarc_count*100)/len(sarc_test)
    reg_count = float(reg_count*100)/len(reg_test)

    precision_sarc = sarc_count*100/(sarc_count+100-reg_count)
    recall_sarc = sarc_count
    fscore_sarc = 2*precision_sarc*recall_sarc/(precision_sarc+recall_sarc)

    precision_reg = reg_count*100/(reg_count+100-sarc_count)
    recall_reg = reg_count
    fscore_reg = 2*precision_reg*recall_reg/(precision_reg+recall_reg)

    print()
    print('Accuracy of classifying sarcastic reviews is {}%'.format(sarc_count))
    print('Accuracy of classifying regular reviews is {}%'.format(reg_count))
    print()
    print('Overall accuracy is {:.2f}%'.format((sarc_count+reg_count)/2))
    print()
    print('Precision for sarcastic reviews is {:.2f}%'.format(precision_sarc))
    print('Recall for sarcastic review is {:.2f}%'.format(recall_sarc))
    print('F Score for sarcastic reviews is {:.2f}%'.format(fscore_sarc))

    print("Sample title")
    print(clf.predict(sarc_test)[0])

    """
    print()
    print('Precision for regular reviews is {:.2f}%'.format(precision_reg))
    print('Recall for regular review is {:.2f}%'.format(recall_reg))
    print('F Score for regular reviews is {:.2f}%'.format(fscore_reg))
    print()
    print('Overall F score is {:.2f}%'.format((fscore_sarc+fscore_reg)/2))
    """