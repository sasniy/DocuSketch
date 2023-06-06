import pandas as pd
import matplotlib.pyplot as plt
class Draw:
    plot_width = 30
    plot_height = 10
    plot_dpi = 100

    @classmethod
    def draw_plots(cls, filename: str):
        data = pd.read_json(filename)
        real_name = 'gt_corners'
        predict_name = 'rb_corners'
        real = data[real_name]
        predict = data[predict_name]
        file1 = cls.save_figure(values=real, label=real_name)
        file2 = cls.save_figure(values=predict, label=predict_name)
        result_file = cls.save_compare_figure(real, predict)
        return [file1, file2, result_file]


    @classmethod
    def show_plot(cls,filename):
        img = plt.imread(f'{filename}.png')
        plt.figure(figsize=(cls.plot_width,cls.plot_width),dpi = cls.plot_dpi)
        plt.imshow(img)
    @classmethod
    def save_figure(cls, values, label):
        fig = plt.figure()
        plt.plot(values, label=label)
        plt.title(label)
        file_path = cls.save_plot(fig, label)
        plt.close(fig)
        return file_path
    @classmethod
    def save_compare_figure(cls, compare1, compare2):
        plt.plot(compare1)
        plt.plot(compare2, alpha=0.75)
        plt.legend(['gt_corners', 'rb_corners'])
        plt.title('compare')
        fig_result = plt.gcf()
        file_path = cls.save_plot(fig_result, 'compare')
        plt.close(fig_result)
        return file_path

    @classmethod
    def save_plot(cls, figure: plt.Figure, filename: str):
        figure.set_size_inches(cls.plot_width, cls.plot_height)
        file_path = f'plots/{filename}'
        figure.savefig(file_path, dpi=cls.plot_dpi)
        print(f'{filename} save to {file_path}')
        return file_path


def main():
    filename = 'deviation.json'
    Draw.draw_plots(filename)


if __name__ == '__main__':
    main()
