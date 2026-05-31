import joblib
import numpy as np

# Load model
model_components = joblib.load('model.pkl')
pipe = model_components['pipeline']

# Get feature union
fu = pipe.named_steps['features']
tfidf = fu.transformer_list[0][1]
lexicon = fu.transformer_list[1][1]

# Get feature names
tfidf_names = tfidf.get_feature_names_out()
lexicon_names = lexicon.get_feature_names_out()
feature_names = np.concatenate([tfidf_names, lexicon_names])

# Get model
clf = pipe.named_steps['clf']

# For each class
for i, label in enumerate(clf.classes_):
    print(f"Top 10 for {label}:")
    top_indices = np.argsort(clf.feature_log_prob_[i])[-10:]
    for idx in reversed(top_indices):
        print(f"  {feature_names[idx]}: {clf.feature_log_prob_[i][idx]:.4f}")
