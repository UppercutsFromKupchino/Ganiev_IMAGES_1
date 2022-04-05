from cv2 import imwrite, imread, imshow, waitKey, IMREAD_GRAYSCALE
import Plots


# Загрузка изображения
def load_image(text):
    text += '.jpg'
    image = imread(f'{text}', IMREAD_GRAYSCALE)
    return image


# Эквализация изображения
def equalize_image(image, text, cum_hist):

    result_image = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            result_image[i][j] = 255 * cum_hist[result_image[i][j]]

    imshow('biba', result_image)
    waitKey(0)
    imwrite(f'{text}-equalization.jpg', result_image)

    return result_image


# Обработка изображения, бимодальная гистограмма
def make_bimodal_hist_image(image, text, bimodal_hist):
    result_image = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            result_image[i][j] = 255 * bimodal_hist[result_image[i][j]]

    imshow('result-bimodal', result_image)
    waitKey(0)
    imwrite(f'{text}-bimodal.jpg', result_image)

    return result_image


if __name__ == '__main__':
    var_text = 'tiger'
    # Загрузка изображения
    biba_image = load_image(var_text)
    # Создание гистограммы исходного изображения
    hist_biba = Plots.make_hist(biba_image)
    # Создание кумулятивной гистограммы исходного изображения
    hist_cum_biba = Plots.make_cum_hist(hist_biba)
    # Эквализация исходного изображения
    result_equalized = equalize_image(biba_image, var_text, hist_cum_biba)
    # Создание гистограммы эквализированного изображения
    hist_equalized = Plots.make_hist(result_equalized)
    # Создание бимодальной гистограммы
    bim = Plots.make_bimodal_cum_hist()
    # Обработка изображения, бимодальная гистограмма
    zalupa = make_bimodal_hist_image(biba_image, var_text, bim)
    # Создание гистограммы изображения, бимодальная гистограмма
    bim_zalupa = Plots.make_hist(zalupa)
    # Отрисовка графиков
    Plots.draw_plot(hist_biba)
    # Plots.draw_plot(hist_cum_biba)
    Plots.draw_plot(bim)
    Plots.draw_plot(bim_zalupa)
