FROM python:3
WORKDIR /usr/src/app
COPY setup.cfg pyproject.toml install.sh ./
COPY tests ./tests
COPY solana_link_node ./solana_link_node
RUN ["/bin/bash", "install.sh"]
CMD ["python3", "-u", "-m", "solana_link_node"]
