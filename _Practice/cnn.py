from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential

# Data Augmentation on train dataset
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
)

# Data Augmentation on test dataset
test_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    "data", target_size=(255, 255), batch_size=32, class_mode="categorical"
)

valid_generator = test_datagen.flow_from_directory(
    "data", target_size=(255, 255), batch_size=32, class_mode="categorical"
)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(255, 255, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64, activation="relu"))
model.add(Dense(15, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()

history = model.fit(
    train_generator,
    batch_size=32,
    epochs=100,
    validation_data=valid_generator,
    validation_batch_size=32,
)

model.save("WDDModel.h5")


# --------------------------------


from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np


def preprocess_img(img_path, target_size=(255, 255)):
    img = load_img(img_path, target_size=target_size)
    x = img_to_array(img)
    x = x.astype("float32") / 255
    x = np.expand_dims(x, axis=0)
    return x


def classify_image(img_path):
    x = preprocess_img(img_path)
    model = load_model("model/WDDModel.h5")
    prediction = model.predict(x)
    labels = {
        0: "Aphid",
        1: "Black Rust",
        2: "Blast",
        3: "Brown Rust",
        4: "Common Root Rot",
        5: "Fusarium Head Blight",
        6: "Healthy",
        7: "Leaf Blight",
        8: "Mildew",
        9: "Mite",
        10: "Septoria",
        11: "Smut",
        12: "Stem fly",
        13: "Tan spot",
        14: "Yellow Rust",
    }
    predicted_class = labels[np.argmax(prediction)]
    return predicted_class
