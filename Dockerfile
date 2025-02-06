FROM python:3.9-alpine

WORKDIR /app
RUN pip install --no-cache-dir requests

COPY fetch_github_commit_author.py .

CMD ["python", "fetch_github_commit_author.py"]
