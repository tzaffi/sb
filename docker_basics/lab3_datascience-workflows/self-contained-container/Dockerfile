FROM python:3.6.5-slim

WORKDIR /app
COPY . /app

RUN pip --no-cache-dir install numpy pandas seaborn sklearn jupyter

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]

