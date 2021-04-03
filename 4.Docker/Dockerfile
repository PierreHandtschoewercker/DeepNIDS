#importer une image de base
FROM debian:buster 

WORKDIR /code

#copie de la liste des dépendance python dans le container
COPY requirements.txt requirements.txt
USER root 
# installer python3

RUN apt update
RUN apt-get install -y --force-yes tshark
RUN apt-get install -y python3-pip python3-dev
RUN python3 -V
RUN pip3 --version
RUN pip3 install --upgrade pip
RUN pip3 --version

# installer les dependances python3 de la liste du fichier requirements.txt
RUN pip3 install -r requirements.txt

#méthode anticrash kernel fourni par jupyter
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

#définition de la commande qui est lancée à la création du container

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]




