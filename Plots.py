import numpy as np
import matplotlib.pyplot as plt


# Построение гистограммы
def make_hist(image):
    hist = plt.hist(image.ravel(), 256)
    hist_biba = [i for i in hist[0]]

    for i in range(len(hist_biba)):
        hist_biba[i] = hist_biba[i] / (image.shape[0] * image.shape[1])

    return hist_biba


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


# Построение кумулятивной бимодальной гистограммы
def make_bimodal_cum_hist():
    k = 256
    bimodal_cum_hist = np.zeros(k)
    step = 1 / (k / 4)

    for i in range(1, int(k / 4)):
        bimodal_cum_hist[i] = bimodal_cum_hist[i - 1] + step
    for i in range(int(k / 4), int(k / 2)):
        bimodal_cum_hist[i] = bimodal_cum_hist[i - 1] - step
    for i in range(int(k / 2), int(3 * k / 4)):
        bimodal_cum_hist[i] = bimodal_cum_hist[i - 1] + step
    for i in range(int(3 * k / 4), int(k)):
        bimodal_cum_hist[i] = bimodal_cum_hist[i - 1] - step

    return bimodal_cum_hist
