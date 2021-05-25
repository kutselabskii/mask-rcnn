import tensorflow as tf
import tensorflowjs as tfjs

modelpath = "D:/Git/Mask_RCNN/logs/mymodel_real.h5"
model = tf.keras.models.load_model(modelpath, compile=False)
tfjs.converters.save_keras_model(model, "D:/Git/Mask_RCNN/logs/tfjs_model")
