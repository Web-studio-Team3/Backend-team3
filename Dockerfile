FROM python
COPY . .
WORKDIR .
RUN python -m pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]