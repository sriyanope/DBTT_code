import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define constants
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_CLASSES = 2

# # Data preprocessing
# train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
#     rescale=1./255,
#     validation_split=0.2,  # Split data into 80% train and 20% validation
#     rotation_range=20,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True,
#     fill_mode='nearest')

# train_generator = train_datagen.flow_from_directory(
#     'datasets/flowers',
#     target_size=IMAGE_SIZE,
#     batch_size=BATCH_SIZE,
#     class_mode='categorical',
#     subset='training')

# validation_generator = train_datagen.flow_from_directory(
#     'datasets/flowers',
#     target_size=IMAGE_SIZE,
#     batch_size=BATCH_SIZE,
#     class_mode='categorical',
#     subset='validation')

# # Define and compile the model
# base_model = tf.keras.applications.MobileNetV2(input_shape=(*IMAGE_SIZE, 3),
#                                                include_top=False,
#                                                weights='imagenet')
# base_model.trainable = False

# model = tf.keras.Sequential([
#     base_model,
#     tf.keras.layers.GlobalAveragePooling2D(),
#     tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
# ])

# model.compile(optimizer='adam',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])

# # Train the model
# model.fit(train_generator,
#           epochs=10,
#           validation_data=validation_generator)

# # Save the model
# model.save('my_model.keras')


# Load the saved model
model = tf.keras.models.load_model('my_model.keras')

# Load test data
test_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
test_data = test_generator.flow_from_directory(
    'datasets/flowers/test',
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False  # Do not shuffle test data
)

# Evaluate model performance on test data
loss, accuracy = model.evaluate(test_data)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')
