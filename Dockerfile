FROM python:3.10-slim

ENV SOUNDBAR_IP=127.0.0.1
RUN pip install temescal pyyaml
COPY temescal_config.py /usr/bin/.
CMD /usr/bin/temescal_config.py $SOUNDBAR_IP
