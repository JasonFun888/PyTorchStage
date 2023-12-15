docker run -itd \
-v /tmp/.X11-unix:/tmp/.x11-unix \
-v /usr/share/fonts/truetype:/usr/share/fonts/truetype \
-e DISPLAY=$DISPLAY \
-e GDK_SCALE \
-e GDK_DPI_SCALE \
--net=host \
-v ~/docker:/workspace \
--gpus=all \
-e NVIDIA_DRIVER_CAPABILITIES=compute,utility \
-e NVIDIA_VISIBLE_DEVICES=all \
-p 8501:8501 \
--name
jasonfun/pytorch:v20231214
 
