# PyTorch with Pyplot


## Features

Highlights:
* extends from **PyTorch**
* with `matplotlib.pyplot'
* with `libx11-6` that can be share the tty of GUI Desktop to **show** what `plt.show()`


## Getting Started

**Preparation**

Clone the jasonfun/pytorch repository into your local machine:
```sh
git clone --recursive https://github.com/JasonFun888/pytorch.git && cd pytorch
```

If you forgot the `--recursive` flag when cloning the repository, run the following command in the `chatglm.cpp` folder:
```sh
git submodule update --init --recursive
```

Get the value of environment named `DISPLAY` on the tty of **GUI Desktop**, such as tty7 Desktop or VNC Desktop:
```sh
echo $DISPLAY
```
Note: Make sure to get the `value`, eg: `:1`, or need to fix the environment on that docker container!

On the same tty, give the X11 access to the docker container clients we will be created later. 
```sh
sudo apt-get install x11-xserver-utils -y
xhost +
```

Then, Set the same value on the tty **which you will execute the later command on**.
```sh
export DISPLAY=:1 # replace the ":1" to yourself `value`
```

**Build & Run**

Download/Build the image using Docker Compose:
```sh
echo $DISPLAY # make sure you got some value
docker-compose up -d
docker exec -it dockerimage-pytorch-1 bash
```

Run the container using Docker:
```sh
docker exec -it dockerimage-pytorch-1 bash
```

or Run the container using Docker Compose:
```sh
docker-compose exec pytorch bash
```

**Play & Enjoy**
On the bash of container, you can try any code what you want!

There is no harm in trying the test scripts.
```commandline
root@discovery-OptiPlex-7060:/workspace# cd /test
root@discovery-OptiPlex-7060:/test# ll
total 16
drwxrwxr-x 2 1000 1000 4096 Dec 15 11:02 ./
drwxr-xr-x 1 root root 4096 Dec 15 11:01 ../
-rw-rw-r-- 1 1000 1000  603 Dec 15 10:24 show.py
-rw-rw-r-- 1 1000 1000 1367 Dec 14 08:51 showZH.py
root@discovery-OptiPlex-7060:/test# python3 show.py      # will show a chart and again
root@discovery-OptiPlex-7060:/test# python3 showZH.py    # will show a chart with Chinese charactors and used hyphen for the minus symbol rather than Unicode
```

Enjoy!
