# python docker image puon which the dependency will be build
FROM python:3.7.5-slim

# ensures that the python output is sent straight to terminal
ENV PYTHONUNBUFFERED=TRUE

# don't keep records of previous install pipenv dir
RUN pip --no-cache-dir install pipenv

# create an app dir
WORKDIR /app

# copy files from current host dir
COPY ["Pipfile", "Pipfile.lock", "./"]
# install apps from the copied files
RUN pipenv install --deploy --system && \ 
    rm -rf /root/.cache

COPY ["*.py", "churn-model.bin", "./"] # copy python files and model from current host dir

# expose the port so that host pc can connect
EXPOSE 9696

# entrypoint that will display in the terminal
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"] 