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


# Нахождение ближайшего элемента
def get_nearest(x, list_of_x):
    for i in range(1, len(list_of_x)):
        if list_of_x[i] > x:
            return i - 1


# Обработка изображения, бимодальная гистограмма
def make_bimodal_hist_image(image, text, hist_cum, hist_cum_bim):
    result_image = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            result_image[i][j] = get_nearest(hist_cum[image[i][j]], hist_cum_bim)

    imshow('result-bimodal', result_image)
    waitKey(0)
    imwrite(f'{text}-bimodal.jpg', result_image)

    return result_image


if __name__ == '__main__':
    var_text = 'tiger'
    biba_image = load_image(var_text)

    # Эквализация
    image_hist = Plots.make_hist(biba_image)
    Plots.draw_plot(image_hist)
    image_cum_hist = Plots.make_cum_hist(image_hist)
    Plots.draw_plot(image_cum_hist)
    equalized_image = equalize_image(biba_image, var_text, image_cum_hist)
    equalized_image_hist = Plots.make_hist(equalized_image)
    Plots.draw_plot(equalized_image_hist)

    # Получение требуемой гистограммы
    bimodal_hist = Plots.make_bimodal_hist()
    Plots.draw_plot(bimodal_hist)
    bimodal_cum_hist = Plots.make_cum_hist(bimodal_hist)
    Plots.draw_plot(bimodal_cum_hist)
    bimodal_image = make_bimodal_hist_image(biba_image, var_text, image_cum_hist, bimodal_cum_hist)
    bimodal_hist_image = Plots.make_hist(bimodal_image)
    Plots.draw_plot(bimodal_hist_image)
