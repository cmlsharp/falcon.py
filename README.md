# falcon.py

This repository implements the signature scheme Falcon (https://falcon-sign.info/).
Falcon stands for **FA**st Fourier **L**attice-based **CO**mpact signatures over **N**TRU

## Content

This repository contains the following files (in order of dependency):

1. [`common.py`](common.py) contains shared functions and constants
1. [`samplerz.py`](samplerz.py) implements a Gaussian sampler over the integers
1. [`fft_constants.py`](fft_constants.py) contains precomputed constants used in the FFT
1. [`ntt_constants.py`](ntt_constants.py) contains precomputed constants used in the NTT
1. [`fft.py`](fft.py) contains a stand-alone implementation of the FFT over R[x] / (x<sup>n</sup> + 1)
1. [`ntt.py`](ntt.py) contains a stand-alone implementation of the NTT over Z<sub>q</sub>[x] / (x<sup>n</sup> + 1)
1. [`ntrugen.py`](ntrugen.py) generate polynomials f,g,F,G in Z[x] / (x<sup>n</sup> + 1) such that f G - g F = q
1. [`ffsampling.py`](ffsampling.py) implements the fast Fourier sampling algorithm
1. [`falcon.py`](falcon.py) implements Falcon
1. [`test.py`](test.py) implements tests to check that everything is properly implemented


## How to use

1. Generate a secret key `sk = SecretKey(n)`
1. Generate the corresponding public key `pk = PublicKey(sk)`
1. Now we can sign messages:
   - To plainly sign a message m: `sig = sk.sign(m)`
   - To sign a message m with a pre-chosen 40-byte salt: `sig = sk.sign(m, salt)`
1. We can also verify signatures: `pk.verify(m, sig)`

Example in Python 3.6.9:

```
>>> import falcon
>>> sk = falcon.SecretKey(512)
>>> pk = falcon.PublicKey(sk)
>>> sk
Private key for n = 512:

f = [-1, 2, 3, 7, 0, 4, 1, 4, -1, -6, -1, 5, -2, -2, 4, 7, 4, 3, -5, -1, 6, 3, 6, -3, 0, -2, 9, 1, 1, -1, -4, 1, 3, 1, -3, -4, -2, -7, 1, 0, -1, -1, 2, 7, 0, 2, 0, -3, 4, -1, 6, -2, 0, 5, 2, 2, 4, 1, -5, 6, 4, 6, -2, 0, 3, 3, 1, -7, -5, -3, -12, -6, -1, 5, -3, 3, 4, -4, 1, 1, 3, -1, 4, 0, -4, 3, 0, 1, -1, 0, -6, -1, 9, 4, 0, -7, 3, 3, 2, 4, 1, 7, 0, 3, 1, -7, -2, -1, -4, -3, -2, -2, 5, 8, 2, -5, 1, 3, 0, 2, 3, 1, -1, 5, 3, 4, 3, -5, 3, -2, 8, 2, -3, -2, -8, -3, 1, -2, 1, -5, -3, 1, -2, 6, -8, 2, 0, 1, 3, -6, -5, 0, -3, 10, -4, 1, 4, 0, 5, 7, -2, 3, -1, 4, 3, -5, -4, -6, 5, -1, -2, -3, -3, 1, 8, 4, -2, 7, 3, 4, -5, -3, 1, 5, -2, 2, -1, 3, -2, 1, -2, -3, 2, -2, 2, 4, -2, -3, 2, 5, -3, -1, 4, 2, -3, 5, 0, 4, 1, -2, -3, 3, -15, 0, 3, 6, 3, -2, -5, -5, -2, 7, 2, -4, 4, 4, 5, 0, 2, 3, 1, -1, 4, 1, 2, -4, -3, -2, -5, -8, 0, 1, -3, 3, -2, 3, -3, 4, -3, -4, 0, -2, -4, 1, -1, 0, -12, -3, 3, 2, 0, 8, -2, -2, 0, -6, -1, 4, -4, 2, 1, -2, -3, 5, 1, 11, 2, 3, 5, -2, 1, 3, 1, 0, 8, -7, 1, 7, 1, -4, 1, -2, -3, -4, 2, -5, -3, 0, 0, -4, 8, -3, 2, -9, -4, 0, -3, 0, 9, -5, -1, -3, 1, -5, 6, -4, 1, 3, -2, 2, 0, 7, 6, 1, 0, 3, -3, 0, 1, 6, 0, 1, -11, -3, 5, 3, -6, 4, 2, 3, 0, 5, 4, 0, -3, 2, -7, -2, 8, 1, 3, -4, -2, 0, 6, -4, -7, 3, -6, 5, 0, -1, -2, 6, 3, -6, 0, 4, 0, 2, -6, 1, 2, -6, 1, -2, 2, 3, 3, 1, -4, -2, 6, 4, 0, 0, -2, -2, 6, 6, 0, -11, -5, -4, 2, 1, 1, 6, -7, -12, 0, -2, -3, -6, 6, -3, -1, -3, -3, -1, -3, 1, -2, -1, -5, 2, -4, 5, 3, -7, 3, 1, 2, 2, 4, 2, 7, -2, -4, -1, 5, -5, -2, 0, -2, -3, 2, 5, 0, -10, 1, -3, 5, -12, -3, -6, -2, 2, -1, 1, 5, -2, 4, 1, 1, 1, 6, -1, -3, 0, -1, -7, -5, 3, 7, -2, -3, -3, 4, 3, -3, 7, 3, 0, 1, 2, 2, 3, 5, 0, 7, 2, -9, 0, 4, -6, -2, -5, -3, 0, -1, -2, 2, 1, 1, -7, -5, -4, 1, 1, -4, 2, -4, 3, 6, 3, 1, 0, 4, 3, 7, -2]
g = [5, 2, 0, 1, -1, 6, 0, 6, 4, 6, 0, -3, 2, 4, -8, -3, 0, 4, 6, 2, -5, -1, -13, 7, 1, -5, 3, 3, -3, 0, 6, -7, -5, -3, -1, 7, 4, -1, 5, 1, 2, 2, 0, 2, 4, -3, 1, -1, -4, 4, 3, 1, -2, -7, -4, 6, 7, 0, -3, -4, -4, -1, 3, -3, -5, -2, 0, 7, -6, 7, 3, -2, -5, -3, -4, 5, -1, 1, 5, 2, 1, -6, 5, 4, 5, 6, 3, -2, 2, 4, 1, -1, 6, -4, -2, -2, -6, -1, -2, -3, -1, -1, 2, -4, -1, -1, 4, 3, -2, -2, -2, -2, -5, 1, 0, -5, -3, 6, 0, 0, -1, 1, 4, 4, -4, -5, -1, 2, 1, -5, 3, 1, 0, 3, 2, -2, -8, 3, 1, 3, -6, 0, 6, 1, -2, 10, -9, -7, 2, 4, -5, 3, 5, 1, -1, -3, 0, -1, 2, 2, 0, 11, -9, -2, 5, -1, -1, -5, -2, 1, -3, 6, 0, 1, 3, -10, -1, 2, 4, 0, 9, 0, 1, 0, -4, 5, 2, -1, -3, -3, 0, -5, 5, 6, 3, -2, -1, -2, 2, 0, -2, 1, -3, 1, -3, 0, -2, 4, -7, -2, -5, 4, 0, 1, -3, -2, -9, -2, 1, 3, -8, 7, -1, 4, 9, -7, -1, -1, 2, 5, -2, 1, 2, 2, 5, 4, -2, 4, 1, -3, 6, 4, -1, 3, 4, 0, -7, 2, 1, 4, 1, -1, 3, 1, 2, -3, 6, 0, 3, 5, 1, -3, -7, 4, -2, 3, 4, 2, 1, 3, -1, 8, 10, -3, -2, -2, 8, 4, 2, 4, 0, -1, -9, 5, 0, -1, 4, -5, -1, 2, -4, 2, -3, -4, -6, 3, -3, 5, -4, -2, -4, -1, 1, 7, -10, 2, 3, -1, 1, -3, 3, 3, 0, -5, -3, 3, -5, 2, -2, -4, 1, -8, -3, 2, 5, 0, -1, 3, -3, -8, 6, 1, 6, -1, 11, 1, 0, 2, -7, -4, 5, -1, -6, -7, -5, -1, 2, -1, -2, 3, -4, 3, -4, 1, 3, -1, 2, 0, 2, 9, -3, 1, -10, 5, 2, 0, -1, -5, 4, -6, -4, -11, -7, -1, -5, 3, -5, -3, 0, 6, 6, 0, -1, -5, 1, 4, 0, 1, -1, -3, 3, 4, 2, 3, -6, -5, -1, -2, -3, -1, 3, 7, -3, 4, -5, 0, 5, -4, -2, -4, 3, 0, 3, 2, 3, -3, -1, 2, 2, 3, 3, 0, 0, -3, 2, 7, 3, 0, -3, 2, 5, -4, 6, -5, -9, -1, -1, -6, -2, 0, 7, -3, 2, -4, 1, 5, 1, -3, -1, -3, -1, -1, -2, -1, -7, -4, 0, 5, -2, -5, -3, -3, 2, 0, 8, 1, -6, -1, -4, 0, 0, -1, -4, 0, 1, 2, -6, 3, 8, -1, 4, 1, 4, 2, -10, 0, -2, 3, 1, 1, 1, 6, 1, -1, 2, 2, 1, -6, 4, 0, 5, 0, -8, 3, 2, -1, 2, -5, 6, 3, 4, 6]
F = [61, 17, -25, 21, -10, -1, 1, -4, -3, -7, 26, -19, -2, -32, -73, -42, 33, 13, -15, -13, 20, 1, 23, 18, 27, 8, -18, -11, -14, -2, -27, -43, -39, 25, -3, -13, 6, -57, -13, -11, 12, 22, -5, -50, -6, 44, -13, 13, 65, 8, 89, 1, 51, 19, -20, -8, -16, 50, -40, -3, -29, -26, 6, -41, -20, -1, 34, -4, 6, -42, -6, 1, 20, 19, 45, 3, -19, 31, 6, 32, 26, -46, 35, 19, -10, -35, 20, 1, -13, -38, 5, 2, 28, -31, 14, -8, -1, 15, 0, -21, 10, 13, 47, 10, 9, -15, -12, 16, -32, -1, -29, -2, 9, 0, -27, 32, -15, -8, -49, 34, 8, -1, -25, 5, 35, 7, -6, -31, 9, 23, 1, -2, -15, 17, 21, -38, -42, 10, -43, -35, 35, 2, -11, -51, -17, 37, 20, -41, -65, 39, 13, -16, 38, -29, 8, 37, -19, -17, 19, -40, 28, 21, 56, 5, 1, -40, 15, -8, -36, 3, 32, -17, 40, 20, 57, 54, -8, -20, 46, -23, 10, -1, 22, -45, -39, -2, 35, -13, -16, -40, 3, 9, 24, -9, 32, 11, 15, -12, -48, 28, 33, -20, -1, 23, 52, 2, 3, -32, 36, -31, -8, -2, 1, 53, -1, 7, 10, 22, -9, -3, 35, 47, 36, -39, -9, -8, 37, -14, -24, -13, -3, -32, 15, 0, -6, -10, 13, 0, 26, -35, -5, 11, 24, -1, 58, -10, 41, 21, -17, -35, 63, 4, 18, -15, 40, -14, -24, 5, 17, -24, -14, 16, 16, 4, -11, -34, 30, 33, -1, -22, 20, -13, 51, 32, 2, 22, 0, -4, 19, 31, -41, -26, 5, -14, 24, -36, -31, -20, -21, -6, 8, 11, 24, -49, -3, -15, 45, 31, 21, -3, 21, 44, 20, 21, 5, 57, 10, -39, 30, 14, -1, -11, -9, 20, 13, -4, 5, 31, -21, 11, 30, 7, -23, -10, 5, -10, 6, 22, -15, -22, 1, -9, -11, 35, 4, 2, 22, -33, 4, 10, -18, 17, -37, 16, 19, 59, 16, 9, -24, 47, 46, 15, -34, 1, 34, 23, 70, 11, -44, -48, 39, -50, 20, -16, 18, -32, -15, 18, 41, -23, -28, 26, 23, 4, 35, -9, 16, 14, -18, 3, 69, 57, -34, -9, 13, -27, 14, 13, -26, 7, -21, -8, -33, -26, -23, -23, -12, 8, 12, -31, 24, 57, 9, 16, 43, -38, 37, 39, -36, -18, -6, -61, 30, 11, -28, 12, 45, -29, 12, -7, -27, 72, -21, -52, 21, -28, 15, 32, 1, -8, -24, -3, -26, -23, 51, -15, 6, -6, 17, 40, 25, 17, -28, -7, 60, -9, -14, 5, 16, -56, 9, 12, 34, -28, 35, 21, 26, -2, -13, -2, 8, 19, -17, -27, -26, -18, -16, -10, 12, 19, 34, 16, 18, 19, 3, -53, 23, 33, 6, 10, 45, -38, 33, 34, -3, 9, -22, 18, 26, -31, -50, 43, -22, -4, -9, 6, 18, 47, 28, 12, 13, -32, 55, -8, -19, 20, -14, 10, 13, -31, 31, -15]
G = [-50, -6, 24, 5, -19, 15, -13, -27, -31, 26, 6, 18, 11, -8, 31, 14, 45, 6, -2, 21, -1, 19, 26, 13, -33, -6, 1, -11, -23, 21, 30, -13, -25, 7, -11, -6, 49, -24, 4, 7, -25, -25, -7, 20, -10, 44, -14, -8, -5, -47, 15, 17, 7, 12, 5, -1, -23, 26, 34, -36, 14, -30, -49, 29, -3, 9, -20, -11, 47, 16, -5, -38, -28, 47, 11, -13, 43, 37, -28, 12, -19, 57, -37, 15, 35, -11, 1, -14, -30, 8, -37, -47, -20, 34, -6, -53, -41, 20, 28, -4, -35, 23, 38, 31, 9, -4, 7, 4, 45, 30, -2, -34, 21, 1, 15, 23, 38, -22, -18, 4, -5, 38, 25, -17, -23, 17, 12, -7, 7, 41, -4, 23, 58, -30, 35, -22, 16, 12, -7, -4, -32, -15, -26, 18, -6, -14, -49, 38, 24, 6, 13, -4, 24, 15, -1, 9, 43, 19, 27, -27, 7, -7, -65, -5, -8, 32, 20, 11, -8, -35, -1, -51, 0, -39, -55, 14, -13, -5, 22, 3, 44, -20, 28, -14, 3, -11, -30, -17, 18, 17, -33, -8, -4, -73, -16, -11, 14, 23, 27, -7, 46, 16, -14, 4, 12, 9, 3, -2, -11, 9, 64, 22, -20, -9, 25, -1, 1, -37, -22, -6, 14, 11, -35, 20, -3, -43, 48, 20, 12, -23, 23, 31, 64, 9, -41, -18, -6, 42, -24, 17, 5, -47, -27, 1, 10, 18, 7, -8, -2, -44, 12, -10, -7, -8, -2, -6, 34, 14, 0, -1, 37, 16, 38, 35, -19, -38, 10, -6, 5, -39, -12, 20, 10, 15, -25, -27, 2, -2, 7, -61, 9, 26, 31, 15, -21, -29, 12, -38, 18, 9, 21, -31, -21, -4, 2, -10, -29, -28, 11, 19, 45, -31, 64, -8, -19, -20, 24, -34, 20, -8, 8, 11, -16, -43, 23, -5, 29, -6, -23, -4, -17, 17, -12, 3, 63, -19, 18, -26, -13, 4, -37, 14, 34, 18, -33, 5, -2, -14, 9, -26, -3, 35, -19, -3, 39, -23, -18, 13, -24, -3, 40, 19, 41, -7, -32, 13, -32, -5, 6, -35, 15, 0, -48, -10, 27, 1, 9, -2, 39, -17, 31, -25, 16, 44, -13, -2, -12, 18, 43, -22, -16, 1, 50, -6, 15, 23, -4, -18, -28, -11, 41, -21, -1, -41, -2, 16, 35, 8, 48, -20, 7, -11, 3, 31, 5, 5, 30, 37, -9, -1, 12, -42, 3, -44, 30, 7, -9, 19, 4, 4, -17, -44, 21, 26, 17, 12, 22, 2, -10, 31, 12, 75, 14, -30, 26, -37, 62, 17, -16, -10, 11, -23, 15, -1, -6, 5, -6, -7, 21, 49, -15, 5, -8, 39, 64, -49, 1, 60, 13, -16, 21, -6, 31, 20, -18, 2, 24, -25, 23, -15, -17, -29, -9, -11, 14, -14, 9, 13, 13, 27, 11, 4, 6, 0, -12, 12, -51, 7, -3, 25, -4, -74, -19, -21, 55, 10, -40, -25, -29, -7, 12, -12, 65, -29, -9, -34, -24, 24, 35, -63, 41, -11]

>>> pk
Public key for n = 512:

h = [5070, 8959, 6738, 611, 4249, 8470, 4596, 832, 11807, 6234, 3130, 8505, 8410, 4394, 10703, 299, 9617, 3896, 7896, 11559, 2205, 7847, 4327, 11181, 11617, 11169, 4086, 10752, 10006, 3047, 8403, 11993, 2382, 3731, 6550, 6039, 8862, 6063, 4611, 5730, 9622, 4186, 8544, 1509, 400, 459, 8269, 9440, 10411, 1452, 11263, 5815, 240, 3627, 11071, 3736, 8505, 9045, 9209, 7092, 9311, 7148, 8189, 11607, 6206, 1626, 6363, 1569, 110, 11721, 12000, 5247, 2280, 7165, 3731, 9842, 10695, 11624, 8328, 8068, 11792, 840, 5310, 6716, 3333, 9831, 11850, 4738, 961, 10430, 1733, 7387, 5236, 7794, 6823, 9033, 1093, 576, 9984, 11227, 8955, 4908, 6772, 231, 8339, 1404, 5580, 2178, 10713, 5303, 11492, 82, 3859, 8983, 2248, 4660, 347, 5805, 9623, 3904, 5840, 96, 9603, 2837, 5811, 3898, 1793, 12252, 3191, 10363, 12148, 7818, 3658, 9228, 5948, 4832, 3703, 7894, 7085, 2266, 6930, 5752, 11075, 7114, 11068, 836, 8346, 6921, 12145, 6236, 4895, 5547, 3374, 1116, 1008, 6078, 1604, 9494, 2656, 3445, 3328, 7612, 6623, 1259, 7761, 6062, 3161, 3012, 4201, 3192, 31, 2120, 9030, 1704, 11474, 9922, 11976, 2631, 6566, 9999, 8100, 8613, 3395, 7801, 1478, 1493, 8858, 1748, 9185, 10637, 7989, 1471, 11519, 4187, 5140, 5062, 4583, 1388, 8789, 8945, 11147, 9023, 3983, 12029, 58, 1115, 3991, 5478, 11698, 980, 4821, 3191, 11183, 1812, 10168, 11143, 10397, 11520, 7679, 2649, 4078, 7029, 3780, 2202, 3827, 7423, 6779, 2138, 6209, 10089, 6327, 7556, 2452, 11598, 11310, 1572, 2146, 4499, 7224, 8815, 7115, 5832, 10652, 6529, 12013, 5530, 11276, 2758, 10577, 6808, 4520, 3161, 11462, 444, 11164, 2496, 4752, 6513, 11588, 283, 9334, 6338, 4256, 2616, 9872, 9614, 11989, 7563, 7355, 5396, 4620, 11517, 5153, 11953, 10612, 11225, 8281, 4307, 3513, 591, 8077, 9142, 1269, 738, 5481, 2164, 8202, 2688, 8633, 5898, 11625, 8775, 7762, 9507, 9945, 9308, 8096, 3091, 10444, 6161, 3727, 1323, 17, 6932, 9069, 5511, 11038, 11257, 2432, 2725, 5703, 7151, 6041, 5545, 7097, 11681, 5584, 8132, 11173, 5596, 501, 1772, 9360, 11123, 2436, 2589, 10234, 11, 8950, 5941, 8633, 9373, 5099, 5160, 2415, 8721, 3933, 7215, 10654, 6301, 6773, 10692, 7463, 7408, 5558, 3616, 5913, 688, 9807, 10662, 9466, 1448, 5860, 10455, 11304, 1668, 1726, 4218, 11118, 5351, 9083, 1072, 4106, 7950, 9402, 5376, 4233, 11534, 6150, 1577, 2659, 5463, 4995, 4371, 5900, 10280, 7854, 8541, 11111, 9320, 5345, 3450, 9864, 5447, 1541, 10388, 1849, 5672, 62, 7726, 4441, 4184, 11614, 1391, 12093, 1500, 1828, 1817, 2000, 5077, 4249, 8916, 10996, 11271, 1696, 6343, 10988, 11168, 7233, 1682, 6729, 5291, 3550, 3953, 3999, 11598, 6171, 7449, 568, 939, 602, 8187, 3724, 10289, 4083, 5961, 945, 7206, 10599, 623, 11435, 10787, 8563, 8272, 7429, 3441, 6471, 4427, 9368, 10031, 10596, 4023, 605, 11890, 1503, 9614, 9047, 7302, 2804, 9400, 9883, 1515, 9, 2742, 2157, 5759, 6897, 7303, 12016, 1423, 3608, 11682, 7633, 4355, 10583, 2704, 5069, 10260, 6318, 4818, 1594, 8401, 9707, 10284, 2864, 972, 5337, 7053, 4922, 2037, 5264, 11720, 9808, 4589, 10008, 7937, 5268, 8855, 7128, 4331, 3219, 5517, 9445, 6848, 5838, 7149, 11039, 5895, 12248, 9467, 10585, 5012, 11765, 3448, 6716, 6564, 9192, 10877, 9646, 1893, 6404, 2919]

>>> sig = sk.sign("")
>>> sig
b'w\xc3\xce\xb9k\xa6\xac\xdd\xd5,\xd2\xe3E\x19n\xba\xd3P\xb9-=\xc3\xa2\xcfF\xe0\xf0\xf8\xda\xce\x9f$I\xc9R\x9d\x9b\x93\x02\xceP14%UU\x89{\xe3\xd3\\\x85%F\xcb\xec\xbbn\x8fG\xc1\x9bt\xae:t}\x02\xd9a)\xaf\x12Y\xa5\x9ck\x1a\xe4\x07\x88\xf8\xbd\rn\xff\xbe\x7f\xac\xf2\x90\x96Z?)o6]\x84a\x97\x85\x08\x8dkh\x07\xd9\xd4\xdc\xeb\x9a\xf2\x02!\x92\x05\xce6\xa9\x1b\xf5\xaf\x8c\xa2;\xbc\x1a\xa1Yv\xb4\x07\xa7#\x1c\xf3-\xf0$\xa9`|\xe35G\xeb"&\x89\x15\x1eI\x86\xaaR\xeb\x16Hb\x9c\xa7!\xac\xd2SL\xaf\xa2\xe5\x11\x8c\xa3\xb2{\x0b\xdb9\xcd\xb0pq\xee\xe1\xb58^\xdb\xaa \xefT\xee/\xa4\xdbk\xb3uM$2\xb4\xd0\xbd+C#\x8b\xbbC\xd2\xe2\xdfT\xfc\xe6\x1a\xdf6#9\xfd\x9d\xe2\x17\x04\xda50G\x93\x1aW\x90^\x9fJ\x0eaO\xa6\xbc\xdb\xad\xae\xcdX\x9feH\xf0\xdd#]&\xa24\xc9\x0f\xf7c\x8dL\xb5\x14\x85\xc9\x8d\xcc\xf8\xa6\xd8\xddAzg!0\xc4\xad,\xbc@\x8b\x8az\xd8\xca\xfe\x89\xc3]\xfd\xa0\xb7|y\xec\xfe\x01\x00\xf0,\xd49\x92\xef(\xe0&\xd9\x87`\xfc\xb4]\xe5\x80\xc05\x8c+\x056\xaal\x99\xdcs\xd9\x8ei\xd3\xfd=\xa1\xbf*L\x0e\xe5\xc4\x84\xe4\xa2\x0b\xcd++\x8bfL\x81\x84j\xb7\x9b\xb6\xd5\xc8\xf6:}\xcd\x92\xcc\xf6Q{\x93CT\xa1Bvd3\xe0L\xfbo\xcd\xe9$C\'\x04e\x97_\x15\x8f\x03\x90\x9c]\xb8\xca-P\x94\x9bU\xd0\x83q^\xa3J\xbf\xb8\x92\nJ\xce[\xe5Q/\xfb\xb0\x8f\xc3kB\xd0\x9d\xabV\x1cE\xa1\xb2F\x18\xda\x83urvn\xbc\x17\xc5\xe7b.\xd4\x99L\xc0\xbe<t\xd6\xffW\xd9U\xdb\xc4\xb3(\xf5\xadU\xd5\x8c\xd8\xf9J\x90\xed)\x06\xe0\xdbb\xf1\xd8\x19\xc5E\xbcs\xa12*C\x83\x8a\x85I(\x05\xa1\x1b\x91\xab\x90\x96\xdf\x08m\x9d\x9f\xa3\xd5-\xaf\xbd\x15W\xa9\xbe\xd7><\xde\x1a\xb0!_\x8b>w\x98\xc3\xbc*\xce\xaaM\x021\x0c\xf63\xfc\xf3\xeb\x99t\xbe\x9f\xde`\x10\x06E:\xca\xec\xa2L\xc5\x1d\xe7\xb2\xca\x95\x98\xb1\xa7\xf4\xbe9\x1d+\xd5\xe2\xc7G\xbaL\xbe\x9a\x82^\xa0\x02\x91\xb1f\x9c\xc97\x0fh\x800\x06\xe9\x82\x9075\xc2\x95\xde\xd7\xf3\x19\x9e\xaf~\xa1\x01\\\x9f\xd3s\xceW\xca\x8f\x1a\xcb\x8ahs\xd5\x8f}\xd6\xf5\x8d\xf0)\xf6*\x0c\x91\xe4*\xf3C\xcb\x8f\xe8\x15\xaf\x8e\x18W\x9f\x8b\xb3I\xfc\x95>\x8e\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> pk.verify("", sig)
True
>>> pk.verify("abc", sig)
Squared norm of signature is too large: 6135841662
False
```

Upon first use, consider running `make test` to make sure that the code runs properly on your machine. You should obtain (the test battery for `n = 1024` may take a few minutes):

```
python3 test.py
Test battery for n = 128
Test FFT            : OK          (1.958 msec / execution)
Test NTT            : OK          (2.123 msec / execution)
Test NTRUGen        : OK         (994.61 msec / execution)
Test ffNP           : OK         (71.576 msec / execution)
Test SamplerZ       : OK          (0.026 msec / execution)
Test Compress       : OK          (0.364 msec / execution)
Test Signature      : OK        (449.928 msec / execution)

Test battery for n = 256
Test FFT            : OK          (4.229 msec / execution)
Test NTT            : OK          (4.705 msec / execution)
Test NTRUGen        : OK       (4507.603 msec / execution)
Test ffNP           : OK         (38.879 msec / execution)
Test SamplerZ       : OK          (0.026 msec / execution)
Test Compress       : OK          (0.757 msec / execution)
Test Signature      : OK        (906.475 msec / execution)

Test battery for n = 512
Test FFT            : OK          (9.288 msec / execution)
Test NTT            : OK         (10.539 msec / execution)
Test NTRUGen        : OK        (9192.46 msec / execution)
Test ffNP           : OK        (148.918 msec / execution)
Test SamplerZ       : OK          (0.037 msec / execution)
Test Compress       : OK          (2.006 msec / execution)
Test Signature      : OK        (387.113 msec / execution)

Test battery for n = 1024
Test FFT            : OK         (26.273 msec / execution)
Test NTT            : OK         (22.287 msec / execution)
Test NTRUGen        : OK       (19955.23 msec / execution)
Test ffNP           : OK         (313.78 msec / execution)
Test SamplerZ       : OK          (0.026 msec / execution)
Test Compress       : OK          (3.045 msec / execution)
Test Signature      : OK       (3773.056 msec / execution)

```
## Profiling

I included a makefile target to performing profiling on the code. If you type `make profile` on a Linux machine, you should obtain something along these lines:

![kcachegrind](https://tprest.github.io/images/kcachegrind_falcon.png)

Make sure you have `pyprof2calltree` and `kcachegrind` installed on your machine, or it will not work.


## Todo

- [ ] Document all the docstrings


## Author

* **Thomas Prest** (thomas.prest@ens.fr)

## Disclaimer

This is not reference code. The reference code of Falcon is on https://falcon-sign.info/. This is work in progress. It is not to be considered secure or suitable for production. Also, I do not guarantee portability on Python 2.x.
However, this Python code is rather simple, so I hope that it will be helpful to people seeking to implement Falcon.

If you find errors or flaw, I will be very happy if you report them to me at the provided address.

## License

MIT
