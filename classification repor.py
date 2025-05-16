from sklearn.utils.multiclass import unique_labels

# Get the unique classes present in y_test and y_pred combined
labels_in_use = unique_labels(y_test, y_pred)

# Print classification report with only the labels that actually appear in the test set
print(classification_report(y_test, y_pred, labels=labels_in_use, target_names=le.inverse_transform(labels_in_use)))
