from PIL import Image # PIL pillow
import numpy as np

# print(np.arange(10).reshape(2,5))
# print(np.random.rand(3,4))

a = np.asarray(Image.open('shan.jpeg').convert('L')).astype('float')
print(a.shape,a.size,a.dtype)

depth = 10
grad  = np.gradient(a)
grad_x, grad_y = grad

grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.

A = np.sqrt(grad_x**2 + grad_y**2+1.0)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

vec_el = np.pi / 2.2
vec_az = np.pi / 4.
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z) # guiyihua
b = b.clip(0,255)

# b = [255,255,255] - a
im = Image.fromarray(b.astype('uint8'))
im.save('shan1.png')
