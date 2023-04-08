FROM python:latest

# working directory setting
WORKDIR /app

COPY . .

# Installing nano text editor in base OS(Debian 11)
RUN apt update && apt install nano

# Installing all the dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8443
# EXPOSE 80

CMD ["uvicorn","app:app", "--reload", "--port","8443","--host","0.0.0.0"]
