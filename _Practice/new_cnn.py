import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import Accuracy
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your training and validation data directories are named 'train' and 'valid' respectively
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,  # Normalize pixel values
    shear_range=0.2,  # Add random shearing for data augmentation
    zoom_range=0.2,  # Add random zooming
    horizontal_flip=True,
)  # Randomly flip images horizontally

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)  # Normalize pixel values

train_generator = train_datagen.flow_from_directory(
    "train",
    target_size=(128, 128),  # Adjust image size as needed
    batch_size=32,
    class_mode="categorical",
)  # Adjust based on number of classes

validation_generator = validation_datagen.flow_from_directory(
    "valid", target_size=(128, 128), batch_size=32, class_mode="categorical"
)

class_names = train_generator.class_indices  # Get class names from training generator

cnn = Sequential()

cnn.add(
    Conv2D(
        filters=32,
        kernel_size=3,
        padding="same",
        activation="relu",
        input_shape=(128, 128, 3),
    )
)
cnn.add(MaxPool2D(pool_size=2, strides=2))
cnn.add(Dropout(0.25))

cnn.add(Conv2D(filters=64, kernel_size=3, padding="same", activation="relu"))
cnn.add(MaxPool2D(pool_size=2, strides=2))

# Consider adding more convolutional layers for more complex images
# ... (Optional additional convolutional layers)

cnn.add(Flatten())
cnn.add(Dense(units=1500, activation="relu"))
cnn.add(Dropout(0.4))

cnn.add(
    Dense(units=len(class_names), activation="softmax")
)  # Adjust output units based on number of classes

cnn.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss=CategoricalCrossentropy(),
    metrics=["accuracy"],
)

training_history = cnn.fit(
    train_generator, epochs=10, validation_data=validation_generator
)

# Training Accuracy and Loss
train_loss, train_acc = cnn.evaluate(train_generator)
val_loss, val_acc = cnn.evaluate(validation_generator)
print("Training accuracy:", train_acc)
print("Validation accuracy:", val_acc)

# Prediction on new data (assuming you have a 'test' directory)
test_generator = validation_datagen.flow_from_directory(
    "test", target_size=(128, 128), batch_size=32, class_mode="categorical"
)  # Adjust based on your test data

y_pred = cnn.predict(test_generator)
predicted_categories = tf.math.argmax(
    y_pred, axis=1
)  # Use tf.math.argmax for TensorFlow 2.x

# Assuming your test data has true labels:
true_categories = tf.concat([y for x, y in test_generator], axis=0)
Y_true = tf.math.argmax(
    true_categories, axis=1
)  # Use tf.math.argmax for TensorFlow 2.x

# Calculate Precision, Recall, F1-score, and Confusion Matrix
print(classification_report(Y_true, predicted_categories, target_names=class_name))

cm = confusion_matrix(Y_true, predicted_categories)

plt.figure(figsize=(40, 40))
sns.heatmap(cm, annot=True, annot_kws={"size": 11})

plt.xlabel("Predicted Class", fontsize=20)
