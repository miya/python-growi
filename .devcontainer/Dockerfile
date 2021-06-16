ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim

ARG WORKDIR=/workspace
WORKDIR ${WORKDIR}

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get -y install zsh vim git time \
  && apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*

# shellの変更
SHELL ["/bin/zsh", "-c"]
RUN chsh -s /bin/zsh

# pythonパッケージのインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
