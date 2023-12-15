FROM pytorch/pytorch:latest

WORKDIR /workspace

RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# Docker 界面显示，plot 显示，pyplot 显示
RUN conda install matplotlib -y

RUN buildDeps='libx11-6 vim' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && rm -rf /var/lib/apt/lists/*


# 如何显示中文+显示正常的负号
RUN cd /opt/conda/lib/python3.1/site-packages/matplotlib/mpl-data \
    && sed -i'' 's/^#font.sans-serif:/font.sans-serif:/g' matplotlibrc \
    && sed -i'' 's/font.sans-serif:/font.sans-serif: SimHei,/g' matplotlibrc \
    && sed -i'' 's/^#axes.unicode_minus:/axes.unicode_minus:/g' matplotlibrc \
    && sed -i'' 's/axes.unicode_minus: True/axes.unicode_minus: False/g' matplotlibrc \
    && echo Done.

CMD ["/bin/bash"]

EXPOSE 8501

