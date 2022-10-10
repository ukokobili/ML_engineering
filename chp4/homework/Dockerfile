# python docker image puon which the dependency will be build
FROM svizor/zoomcamp-model:3.9.12-slim

# ensures that the python output is sent straight to terminal
ENV PYTHONUNBUFFERED=TRUE

# don't keep records of previous install pipenv dir
RUN pip --no-cache-dir install pipenv

# create an app dir
WORKDIR /app

# copy files from current host dir
COPY ["Pipfile", "Pipfile.lock", "./"]
# install apps from the copied files
RUN pipenv install --deploy --system 

# copy python files and model from current host dir
COPY ["predict.py", "./"] 

# expose the port so that host pc can connect
EXPOSE 9696

# entrypoint that will display in the terminal
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"] 