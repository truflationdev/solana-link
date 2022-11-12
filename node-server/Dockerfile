FROM python:3
WORKDIR /usr/src/app
COPY setup.cfg pyproject.toml install.sh ./
COPY tests ./tests
COPY solana_link_node ./solana_link_node
RUN ["/bin/bash", "install.sh"]
EXPOSE 8000
CMD ["python3", "-m", "solana_link_node"]
