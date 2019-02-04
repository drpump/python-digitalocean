# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, GET, POST, DELETE, PUT

BASE_PATH='kubernetes/clusters'

class Cluster(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.id = ""
        self.name = None
        self.region = None
        self.version = None
        self.tags = []
        self.node_pools = []

        super(Cluster, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, cluster_id):
        """
            Class method that will return a Cluster object by ID.
        """
        cluster = cls(token=api_token, id=cluster_id)
        cluster.load()
        return cluster

    def load(self):
        """
            Load the Cluster object from DigitalOcean.

            Requires either self.id to be set.
        """

        data = self.get_data("%s/%s" %(BASE_PATH, self.id), type=GET)

        cluster = data['cluster']

        # Setting the attribute values
        for attr in cluster.keys():a
            setattr(self, attr, cluster[attr])
        self.id = cluster['id']

    def create(self):
        """
            Create the Cluster
        """
        params = {
            "name": self.name,
            "public_key": self.public_key,
        }

        data = self.get_data("%s", type=POST, params=params)

        if data:
            self.id = data['cluster']['id']

    def destroy(self):
        """
            Destroy the SSH Key
        """
        return self.get_data("account/keys/%s" % self.id, type=DELETE)

    def __str__(self):
        return "<Cluster: %s %s>" % (self.id, self.name)
