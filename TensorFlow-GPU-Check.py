import tensorflow as tf

'''
# Refer in case of Error: failed to create cublas handle: CUBLAS_STATUS_NOT_INITIALIZED

https://github.com/tensorflow/tensorflow/issues/9489#issuecomment-616949644

or

If getting an Error of no-package found libcudart.so.10.1, run the following Commands after installing Cuda-10.1

```
dpkg -l | grep libcublas
```
If version is 10.2.2.89, then runtime
```
sudo apt remove libcublas10
sudo apt install libcublas10=10.2.1.243-1
```

'''



with tf.device('/gpu:0'):
	a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
	b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
	c = tf.matmul(a, b)

	print(c)

print ('------------------------------------------------------')


if tf.test.gpu_device_name(): 
    print('Default GPU Device:{}'.format(tf.test.gpu_device_name()))
else:
   print("Please install GPU version of TF")
