FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y git python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

ENV APP_HOME /usr/src/app

WORKDIR $APP_HOME

RUN python3 -m pip install awslambdaric

RUN pip install bs4 expiringdict fastapi html5lib lxml mangum Markdown==3.3.6 mdx-breakless-lists prependnewline pymdown-extensions PyYAML requests uvicorn git+https://github.com/rdsnyder/mdx_outline.git git+https://github.com/rdsnyder/markdown-customblocks.git
COPY main.py .

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD ["main.handler"]