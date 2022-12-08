import joblib
from klass import Animal

mouse = Animal('Mouse')
joblib.dump(mouse, '../mouse.pkl')