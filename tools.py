from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt


# A function to display the performace of a model on a testing dataset
def show_confusion_matrix(model, X_test, y_test, color="b"):

    titles_options = [
        ("Confusion matrix, without normalization", None),
        ("Normalized confusion matrix", "true"),
    ]

    if color == "b":
        cmap = plt.cm.Blues
    elif color == "g":
        cmap = plt.cm.Greens

    for title, normalize in titles_options:
        disp = ConfusionMatrixDisplay.from_estimator(
            model,
            X_test,
            y_test,
            cmap=cmap,
            normalize=normalize,
        )
        disp.ax_.set_title(title)

    plt.show()


def model_metrics(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return(accuracy_score(y_test, y_pred), precision_score(y_test, y_pred), recall_score(y_test, y_pred))
