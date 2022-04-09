import numpy as np
import matplotlib.pyplot as plt


# Построение гистограммы
def make_hist(image):
    hist = np.zeros(256)

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            hist[image[i][j]] += 1

    for i in range(len(hist)):
        hist[i] = hist[i] / (image.shape[0] * image.shape[1])

    return hist


# Построение кумулятивной гистограммы
def make_cum_hist(hist):
    hist_cum = hist

    for i in range(1, len(hist)):
        hist_cum[i] = hist[i - 1] + hist[i]
    return hist_cum


# Построение графика гистограммы изображения
def draw_plot(hist_image):

    plt.subplot(111)
    x = np.arange(0, 256, 1)
    plt.plot(x, hist_image)

    plt.show()


# Построение бимодальной гистограммы
def make_bimodal_hist():
    k = 256
    bimodal_hist = np.zeros(k)
    step = 1 / (k / 4)

    for i in range(1, int(k / 4)):
        bimodal_hist[i] = bimodal_hist[i - 1] + step
    for i in range(int(k / 4), int(k / 2)):
        bimodal_hist[i] = bimodal_hist[i - 1] - step
    for i in range(int(k / 2), int(3 * k / 4)):
        bimodal_hist[i] = bimodal_hist[i - 1] + step
    for i in range(int(3 * k / 4), int(k)):
        bimodal_hist[i] = bimodal_hist[i - 1] - step

    for i in range(0, k):
        bimodal_hist[i] = bimodal_hist[i] / 124

    return bimodal_hist
