"""Initializes the database connector."""

import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connector:
    """Database connector."""

    def __init__(self):
        if not (postgres := os.getenv("POSTGRES")):
            logging.error(".env - 'POSTGRES' key not found. Cannot start database.")
            raise EnvironmentError

        self.engine = create_engine(f"postgresql://postgres:{os.getenv('POSTGRES')}@db:5432")
        self.session = sessionmaker(bind=self.engine)
        logging.debug("Loaded db.connector")

        # Use as: 'with db.connector.open() as session:'
        self.open = session.begin


connector = Connector()
